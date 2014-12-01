#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import argparse
from random import randint
parser = argparse.ArgumentParser(description='Patent database search engine')
parser.add_argument('--author',
		   nargs='*', 
                   help='last first')

parser.add_argument('--patent_num', 
                   help='patent number')

parser.add_argument('--filing_date', 
                   help='Filing Date')
args = parser.parse_args()
print(args)

def test_db_load():
   functions = [find_by_author, find_by_patent_number, find_by_filing_date]
   while True:
   	yield functions[randint(0,2)]

def find_by_author():
   pass

def find_by_patent_number():
   pass

def find_by_filing_date():
   pass

next_gen = test_db_load()
print(next(next_gen))
print(next(next_gen))

print(next(next_gen))
