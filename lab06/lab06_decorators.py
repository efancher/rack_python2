#!/usr/bin/env python
#!*-* coding:utf-8 *-*

"""

:mod:`lab06_decorators` -- Python Decorators
=============================================

LAB06 Learning Objective: Familiarization with function decorators

Decorators are called with an argument of the underlying function. The decorator replaces
 the called function with another function (that usually calls the underlying function at
 some point).

#. Create a list with random first names including "Bob".

#. Write a function party() that takes a single list argument (invitees) and prints it.

#. Write a decorator named @bouncer for party(). Bouncer prints "Looking for Bob..."
   and removes anyone named Bob from the invitee list, then calls party() with the new
   list. Print "Dropping Bob..." if he is found. Include a one line docstring.

#. Call party(invitee_list) to test.

#. Add a call to inspect.getmembers() on the bouncer object. Print the resulting list of
   tuples skipping cases where the 2nd element of the tuple is a dictionary.

"""

party_list = ["Joe", "Sam", "Louie", "Katie", "Cassandra", "Bob", "Shelly", "Linda", "Lisa"]
def bouncer(party_function):
    "Exclude that dirty scoundrel Bob."
    def new_function(party_list):
        print "In new function"
        new_party_list = []
        for invitee in party_list:
            if invitee == "Bob":
                print "Dropping Bob"
            else:    
                new_party_list.append(invitee)
        party_function(new_party_list)
    return new_function

print("test")
@bouncer
def party(party_list):
    for invitee in party_list:
        print(invitee)

party(party_list)
