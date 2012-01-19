#!/usr/bin/python
# Filename: while.py

number = 23
running = True
while running:
	myguess = raw_input('Enter an interger: ')
	if not myguess.isdigit():
		if myguess == 'quit' or myguess == 'exit':
			print 'Bye'
			break
		print 'Input is not interger!'
		continue
	guess = int(myguess)
	if guess == number:
		print 'Congratulations, well done.'
		running = False
	elif guess < number:
		print 'No, it is higher than that'
	else:
		print 'No, it is lower that that'
else:
	print 'The whiile loop is over.'

print 'Done'

