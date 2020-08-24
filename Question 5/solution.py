# In number theory, a happy number is a number which eventually reaches 1 when replaced by the sum of the square of each digit
# Read more here https://en.wikipedia.org/wiki/Happy_number
# Since the conjecture is that every number ends either in 1 or 81 , the count of numbers which end in 81 will be the count of total
# numbers - the number of happy numbers
# Below function checks if the number is happy or not using hash maps for a more efficient calculation
def isHappy(number):
	hashSet = set()
	hashSet.add(number)
	
	while True:
		number = sum(int(i) ** 2 for i in str(number))
		
		if number == 1:
			return True
		
		if number in hashSet:
			return False
		
		hashSet.add(number)

# Calculate the solution based on the flag and the number given
def calcTotalHappy(n,flag):
	num = 0
	if flag == 1:
		for number in range(1,n):
			if isHappy(number):
				num+=1
	else:
		for number in range(1,n):
			if not isHappy(number):
				num+=1
	return num


if __name__ == "__main__":
	n = int(input())
	t = int(input())
	print(calcTotalHappy(n,t))