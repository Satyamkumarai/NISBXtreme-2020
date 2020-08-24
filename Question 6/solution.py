# Functio to find the maximal sum
# This can be solved efficiently using dynamic programming
# From the bottom up, find the maximal element and find corresponding maximal element on the above level and so on
# untill you reach the tip of the pyramiddatetime A combination of a date and a time. Attributes: ()
# You can read about a similar C# implementation here https://www.mathblog.dk/project-euler-18/
def findMaxSum(arr):
	for i in range(0,len(arr)):
		arr[i]=arr[i].split()

	for i in range(0,len(arr)):
		for j in range(0, len(arr[i])):
			arr[i][j]=int(arr[i][j])
	while(len(arr)>1):
		v=arr[-2]
		w=arr[-1]
		for i in range(0,len(v)):
			v[i]+=max(w[i],w[i+1])
		arr.pop()
	return arr[0][0]

if __name__ == "__main__":
	n=int(input())
	tri = []
	for i in range(n):
		tri.append(input())
	print(findMaxSum(tri))