#! /usr/bin/env python

import random

f = open("highScore.txt", "r+") #read & write the score

highScore = f.read()

print("Coin guessing game. All time high score is {}".format(highScore))
print("Start to throw!")

score = 0

while True:
	sides = random.choice(["heads", "tails"])
	guess = (raw_input("Please predict heads or tails ^_^: ").lower())[0]
	
	while True:
		if guess != "h" and guess != "t":
			guess = (raw_input("Choose from heads and tails: ").lower())[0]
		else:
			break
			
	if guess == sides[0]:
		score += 1
		print("It is {}. You are right! Your score is {}. ".format(sides,score))
	else:
		break
			
if score >= int(highScore):
	f.seek(0)
	f.write(str(score))
	print("You win!")

f.close()






















#coin = random.randint(1,2)
#answer = raw_input("Predict heads or tails?")

#if coin == 1:
	#for answer.lower = heads
		#print("The coin is: Heads. You have {}.getScore") 
	#for answer.lower = tails
		#print("The coin is: Heads. Game over.\n Your score is {}. ".finalScore + The high score is

#else:
	#print("The coin is: Tails.")
	
