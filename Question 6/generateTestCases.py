import numpy as np

def generateCase(n:int):
	try:
		N = np.random.randint(5,200)
		with open(f"input{n}.txt",'w') as file:
			file.write(f"{N}\n")
			for i in range(1,N+1):
				nums = np.random.randint(0,500,i)
				nums = list(map(str,nums))
				inp = " ".join(nums)
				inp+="\n"
				file.write(inp)
	except Exception as e:
		print(f"ERROR {str(e)}")

if __name__ == "__main__":
	n = int(input())
	for i in range(n):
		generateCase(i)