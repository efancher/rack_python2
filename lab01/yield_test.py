#!/usr/bin/env python2
# -*- coding: utf-8 -*-
in_scope =10 
def y_func(x):
    num = 0
    while num < x:
        yield in_scope*num
        num +=1

new_gen = y_func(1000)
print("first: {0}".format(next(new_gen)))

print("second: {0}".format(next(new_gen)))

print("third: {0}".format(next(new_gen)))
print("updating in_scope")
in_scope=10000

print("fourth: {0}".format(next(new_gen)))

