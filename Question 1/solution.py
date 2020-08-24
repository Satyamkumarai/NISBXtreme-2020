# Using regex to parse the input so importing re module
from re import compile

def infix_to_postfix(string : str):
	'''
		Convert an infix expression to postfix ie Reverse Polish Notation.
		input :string: - string in infix form. 

	'''

	precedence = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 0}
	stack = []
	output = []
	oper_count, paren_count = 0, 0

	# Test infix equation for compatibility.
	
	for element in string:
		try:
			# print(element, oper_count, paren_count) # Debug
			if oper_count == 2:
				raise Exception("Multi-digit operand")
			elif element.isdigit():
				oper_count += 1
			elif element in "+-*/":
				oper_count = 0
			elif element == '(':
				paren_count += 1
			elif element == ')':
				paren_count -= 1
			else:
				raise Exception("Invalid operation")
		except Exception as instance:
			print(instance, "\nString:", string, "\nElement: ", element)
			raise
	try:
		if paren_count != 0:
			raise Exception("Mismatched parenthesis")
		elif compile(r"[+\-*/]{2,}").search(string) is not None:
			raise Exception("Sequential operations")
	except Exception as instance:
		print(instance, "\n String:", string, "\nElement: ", element)
		raise

	for element in string:
		if element.isdigit():
			output.append(element)
		elif element == '(':
			stack.append(element)
		elif element == ')':
			top_element = stack.pop()
			while top_element != '(':
				output.append(top_element)
				top_element = stack.pop()
		else:
			while (len(stack) != 0) and (precedence[stack[len(stack) - 1]] >= precedence[element]):
				output.append(stack.pop())
			stack.append(element)
	while len(stack) != 0:
		output.append(stack.pop())
	return ''.join(output)


if __name__ == "__main__":
	
	# n : integer ;number of test cases.
	n = int(input())

	# test_cases : empty array to store the n test cases.
	test_cases = []

	# input all of the test cases
	for i in range(n):
		test_cases.append(input())
	
	# convert each input into its corresponding RPN form output.
	for test in test_cases:
		print(infix_to_postfix(test))