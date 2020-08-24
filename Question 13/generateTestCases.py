import random
import numpy as np

def makeMatrix(s):
	matrix = ''
	for i in range(s):
		numbers = [random.randint(0,690) for i in range(s)]
		row = " ".join(map(str,numbers))
		matrix+=row
		if(i!=s-1):
			matrix+="\n"
	return matrix

if __name__ == '__main__':
	x = int(input())

	for i in range(x):
		s = random.randint(0,100)
		with open(f"input{i}.txt",'w') as file:
			file.write(f"{s}\n")
			file.write(makeMatrix(s))