#!/usr/bin/env python2
#!*-* coding:utf-8 *-*
from os import walk
from os import listdir
from os.path import isdir, join
import multiprocessing
from multiprocessing import (Process, Manager)
import hashlib
import time
"""

:mod:`lab08_multiprocessing` -- Multiprocessing
================================================

LAB08 Learning Objective: Use multiple processes and a Queue to synchronize
      work units for consumer.

::

  a. Ask for a directory to process (use raw_input())

  b. Create a multiprocessing.Queue for producer/consumer processes to use

  c. Find sub-directories in the given directory

  d. Producer side: 
     For each sub-directory, start a new multiprocessing.Process that walks 
     the sub-directory, recursively building a dictionary of regular files, 
     where the key is a SHA1 hash of the contents, and the value 
     is the full path name. If duplicate files are discovered, 
     print the paths.  When done, add the dictionary to the Queue.

  e. Consumer side:
     As directories become available on the Queue, merge them into a master 
     dictionary called *rollup_dict*. Once again, if duplicate files are discovered,
     print the paths.

  f. When all processes have finished (how can you tell?), report their pid
     numbers and exit codes. Also report the number of unique files in the given
     directory.

"""
queue = multiprocessing.Queue()
manager = Manager()
dir_dict = manager.dict()
def producer(dirpath):
    path_dict = dict()
    for (apath, names, filenames) in walk(dirpath):
        for afile in filenames:
            full_path = join(apath,afile)
            with open(full_path) as dp:
                sha1_dp = hashlib.sha1()
                sha1_dp.update(dp.read())
                sha1_digest = sha1_dp.digest()
                print("file {0}, hash {1}\n".format(full_path, sha1_digest))
                if sha1_digest in path_dict:
                    print("producer: file with contents exists, file1: "
                          "{0}, file2: {0},"
                          "last reference overwritten."
                          "".format(path_dict[sha1_digest],full_path))
                path_dict[sha1_digest] = full_path
    queue.put(path_dict)


def consumer(queue):
    while True:
        item = queue.get()
        if item:
            for key in item.keys():
                if key in dir_dict:
                    print("consumer: file with contents exists, file1: "
                          "{0}, file2: {0},"
                          "last reference overwritten."
                          "".format(dir_dict[key],item[key]))
                dir_dict[key] = item[key]
        print("sleeping 2")
        time.sleep(2)
        

if __name__ == "__main__":
    s = raw_input('--> ')
    onlydirs = [ join(s,adir) for adir in listdir(s) if isdir(join(s,adir))]
    producers = list()
    for adir in onlydirs:
        # start new producer with adir
        producer_p = Process(target=producer, args=((adir),))
        producers.append(producer_p)
        producer_p.daemon = True
        producer_p.start()
    # consume?
    consumer(queue)
    for producer_p in producers:
        producer_p.join()
        print("pid: {0}, exit code: {1}",format(producer_p.pid, producer_p.exitcode))
    #for (dirpath, dirnames, filenames) in walk(s):
    #    print "dirpath {0}".format(dirpath)
        # print "dirnames {0}".format(dirnames)

