from math import ceil
from random import randint

# This problem can be easily solved with some math. We can figure that the 
# Corners of a square of size s have values: s^2−3s+3, s^2−2s+2, s^2−s+1, s^2.
# so we can easily capture the corner / diagonal numbers without having to generate the entire spiral
# The only other issue is a efficient primality test. I decided to go with the fermat test as it is quite fast.

# Read more here
# https://en.wikipedia.org/wiki/Fermat_primality_test
def FermatPrimalityTest(number):
    ''' if number != 1 '''
    if (number > 1):
        ''' repeat the test few times '''
        for time in range(3):
            ''' Draw a RANDOM number in range of number ( Z_number )  '''
            randomNumber = randint(2, number)-1
            
            ''' Test if a^(n-1) = 1 mod n '''
            if ( pow(randomNumber, number-1, number) != 1 ):
                return False
        
        return True
    else:
        ''' case number == 1 '''
        return False  


def generateCornerNumbers(s):
	''' generate the corner numbers for a square spiral matrix of size s 
		the corner numbers are given with the formula: 
		 s^2−3s+3, s^2−2s+2, s^2−s+1, s^2 '''

	a = pow(s,2) - 3*s + 3
	b = pow(s,2) - 2*s + 2
	c = pow(s,2) - s + 1
	d = pow(s,2)
	return [a,b,c,d]


def generateDiagonalRatio(N):
	''' Generate the diagonal numbers for a square spiral matrix of size N 
		and calculate the ratio of prime numbers to total numbers.
	'''
	diagonals = []
	for i in range(N,1,-2):
		diagonals += generateCornerNumbers(i)
	if N%2:
		diagonals.append(1)
	primes = 0
	for num in diagonals:
		if FermatPrimalityTest(num):
			primes+=1
	return(ceil(100*primes/len(diagonals)))

if __name__ == "__main__":
	num = int(input())
	print(f"{generateDiagonalRatio(num)}%")
