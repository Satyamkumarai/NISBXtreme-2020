import numpy as np

def generateTestCases(n,length):
	with open(f"test{n}.txt",'w') as file:
		file.write(f"{length}\n")
		for i in range(length):
			line = str(np.random.randint(0,500,4))[1:-1]+"\n"
			res = file.write(line)
		print(f"Test Case {n} Generated")

if __name__ == "__main__":
	n = int(input())
	# arr = np.random.randint(0,5000,n)

	''' Test case points values given in hackerrank '''
	arr=[30,400,420,690,2000,3500]


	for i in range(n):
		generateTestCases(i,arr[i])
	print("DONE")
