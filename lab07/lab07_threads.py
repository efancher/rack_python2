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
import random
work_to_do = list() 
connections = dict()
cv = threading.Condition()
def test_function():
    print "test 1"

def test2_function():
    print "test 2"

def test3_function():
    print "test 3"


def boss():
    with cv: 
        work_to_do.append(random.choose([test_function, test2_function, test3_function])
        cv.notify()

def worker():
    with cv:
        #do something
        pass   
 

def connection_mgr():
   pass

def connection_mgr():
   pass




