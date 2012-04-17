#!/usr/bin/env python
# Filename: func_param.py
import sys

def printMax(a,b):
	'''Hello, this function prints the maximum number of two input.
	 The two values must be integers.'''
	if a>b:
		print a,'is maximum'
	else:
		print b,'is maximum'

x1 = raw_input('Please input the first number: ')
if not x1.isdigit():
	print "Please input a integer!!"
	sys.exit(1)		

y1 = raw_input('Please input the second number: ')
if not y1.isdigit():
	print "Please input a integer!!"
	sys.exit(1)		

x = int(x1)
y = int(y1)

printMax(x,y) # give variables as arguments
print printMax.__doc__
