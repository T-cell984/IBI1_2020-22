# What does this piece of code do? To randomly choose a number that is less than 50
# Answer: a number that is less than 50

# Import libraries
# randint allows drawing a random number, 
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil


p=False
while p==False:
	p = True
	n = randint(1,100)
	if n >= 50:
		p = False
#if n is a randint which is larger than 50 or equals to 50, then it will select another n until n < 50
print(n)
