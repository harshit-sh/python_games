# rps.py
# Rock Paper Scissors program
# Created by : Harshit Sharma

import random

print "Welcome to Rock,Paper,Scissors!"
print '-------------------------'
nh = raw_input("What's your name ? : ")
print
l = ["rock","paper","scissors"]
comp = random.choice(l)
points = int(raw_input("How many points for a win? : "))


human = ""
def f():
	hum = raw_input("Choose (r)ock , (p)aper , or (s)cissors ('r' or 'p' or 's'): ")
	if hum == "r":
		human = "rock"
	elif hum == "p":
		human = "paper"
	elif hum == 's':
		human = "scissors"
	return human
	
human1 = f()
count_comp = 0
count_human = 0

while (count_comp != points and count_human != points):
	if (comp == "rock" and human1 == "scissors")or(comp == "scissors" and human1 == "paper")or(comp == "paper" and human1 == "rock"):
		count_comp = count_comp + 1
		print nh,":", human1,"   Computer : " , comp ,"    Computer wins!"
		print nh," : ", count_human,"    Computer : ",count_comp 
		
		if (count_comp != points and count_human != points):	
			comp = random.choice(l)
			human1 = f() 
			
	elif(human1 == "rock" and comp == "scissors")or(human1 == "paper" and comp == "rock")or(human1 == "scissors" and comp == "paper"):
		count_human = count_human + 1
		print nh,":",human1,"    Computer : ", comp , "    You win!"
		print nh,":",count_human,"    Computer : ",count_comp 
		if (count_comp != points and count_human != points):
			comp = random.choice(l)
			human = f()
			
	else: 
		print nh,":",human1,"    Computer : ", comp 
		print "Let's try again"
		if (count_comp != points and count_human != points):
			comp = random.choice(l)
			human1 = f()

