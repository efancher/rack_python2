#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import argparse

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
