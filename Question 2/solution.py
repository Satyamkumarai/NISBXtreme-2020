
# Fast fibonacci algorithm 
# You can read up on more of the math behind this here:
# http://en.wikipedia.org/wiki/Fibonacci_number#Matrix_form
def fibonacci(n):
    v1, v2, v3 = 1, 1, 0   
    for rec in bin(n)[3:]:  
        calc = v2*v2
        v1, v2, v3 = v1*v1+calc, (v1+v3)*v2, calc+v3*v3
        if rec=='1':
			v1, v2, v3 = v1+v2, v1, v2
    return v2

# Function to generate the sum of N fibonacci numbers
# Sum(F(n)) = F(n+2) -1
# You can get more information on the above from here 
# https://en.wikipedia.org/wiki/Fibonacci_number#Combinatorial_identities
def fibonacciSummation(n):
	return fibonacci(n+2)-1
	

if __name__ == "__main__":
	n = int(input())
	print(fibonacciSummation(n))