#!/usr/bin/env python
#-*- coding=utf-8 -*-

"""

:mod:`lab07_threads` -- Threads
=========================================

LAB07 -- Learning Objective: Familiarization with threading module and 
         boss/worker pattern.
         Optional Objective: Use eventlet's greenthread instead.

::

 1. Read the doc for the threading module.

 2. Create a boss/worker model by threading the following functions: 

    a) boss(): generates random work using the (3) patent find functions from lab04, 
       then inserts the new work (as functions) in a data structure for worker 
       threads. Use a Condition variable to synchronize access to the work data structure.

    b) worker(): Run in daemon mode. Waits for an Event called *connections_avail_event*, 
       then obtains and saves a *connection* object from a dictionary using it's thread 
       id or name as the key. Use thread local storage to save connection object. 
       Removes work from the work data structure managed by boss thread when *notified*. 
       Executes the work item (a function). 

    c) connection_mgr(): Waits for an Event called *init_complete_event*, then obtains 
       and inserts a connection object for database access. The connection object can 
       be any object i.e. can be simulated.

  3. Create mainline code to initialize at least 4 worker threads, the boss, and 
     connection_mgr threads. Test by generating at least 10 work items.


"""
import threading
from threading import Thread
import random
import time

work_to_do = list() 
connections = dict()
cv = threading.Condition()
def test_function():
    time.sleep(random.randint(4,8))
    print "test 1"

def test2_function():
    time.sleep(random.randint(4,8))
    print "test 2"
    
def test3_function():
    time.sleep(random.randint(10,15))
    print "test 3"

class Boss(Thread):
    def __init__(self, number_to_produce):
        ''' Constructor. '''
        
        Thread.__init__(self)
        self.number_to_produce = number_to_produce

    def run(self):
        for i in range(1,self.number_to_produce+1):
            time.sleep(random.randint(3,6))
            with cv: 
                print(self.getName())
                print("produced {0} items".format(i))
                work_to_do.append(random.choice([test_function, test2_function, test3_function]))
                cv.notifyAll()

class Worker(Thread):
    def run(self):
        while(True):
            with cv:
                while len(work_to_do) == 0:
                    cv.wait()
                print(self.getName())
                func = work_to_do.pop() 
                func()
 

if __name__ == "__main__":

    worker_objects = list()    
    
    for i in range(4):
        new_thread = Worker()
        new_thread.setName("Worker thread {0}".format(i))
        worker_objects.append(new_thread)
        new_thread.start()
    
    
    boss = Boss(10)
    boss.start()


