# Calculate the factorial of a number by reducing the number of succesive multiplications
# Read more here
# https://www.hackerearth.com/practice/notes/efficient-factorials-calculation/
def calculate_factorial_multi_half(number):
	
	if number == 1 or number == 0:
		return 1

	handle_odd = False
	upto_number = number

	if number & 1 == 1:
		upto_number -= 1
		handle_odd = True

	next_sum = upto_number
	next_multi = upto_number
	factorial = 1

	while next_sum >= 2:
		factorial *= next_multi
		next_sum -= 2
		next_multi += next_sum

	if handle_odd:
		factorial *= number

	return factorial

if __name__ == "__main__":
	n = int(input())
	print(str(calculate_factorial_multi_half(n))[:5])