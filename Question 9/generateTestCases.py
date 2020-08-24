import numpy as np

if __name__ == "__main__":
	n=int(input())
	for i in range(n):
		with open(f"test{i}.txt",'w') as file:
			length = np.random.randint(10,100000)
			file.write(f"{length}\n")
			numbers = np.random.randint(0,100000000000,length,dtype=np.int64)
			for item in numbers:
				file.write(f"{item}\n")