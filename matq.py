# matq.py
# Multiplication Quiz program
# Created by : Harshit Sharma

from random import randint

print "Welcome to Maths Multiplication Quiz!"
print "--------------------------------"
ques = int(raw_input("How many questions do you wish to answer? "))
print "--------------------------------"
limit = int(raw_input("Till what positive range can you answer? (Enter a Positive number) "))

c1 = 0
for i in range(ques):
	n1 = randint(1,limit)
	n2 = randint(1,limit)
	right_ans = n1*n2
	ans = int(raw_input("What's %d times %d? : "%(n1,n2)))
	if right_ans == ans:
		print "Well done!"
		c1 = c1 + 1
	else:
		print "Sorry, answer is ",right_ans
		
print
print "---------Summary------------"
print
print "You scored", c1, "points out of a possible", ques
