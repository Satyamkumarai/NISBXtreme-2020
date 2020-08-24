# Solution to find the remaining person in the circle 
# Read more here https://en.wikipedia.org/wiki/Josephus_problem
def josephus( n,  k):
	res = 0;
	for i in range(1,n+1):
		res =(res+k)%i
	return res+1

if __name__ == "__main__":
	n = int(input())
	k = int(input())
	print(josephus(n,k))