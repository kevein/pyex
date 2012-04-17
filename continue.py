#!/usr/bin/python
# Filename: continue.py

while True:
    s = raw_input('Enter something : ')
    if s == 'quit':
        break
    if len(s) < 3:
        print 'Input is not of sufficient length: %d' % len(s)
        continue
    print 'Input length is %d' % len(s)
    
