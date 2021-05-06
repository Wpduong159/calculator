# -*- coding: utf-8 -*-

def main():
	# Let's welcome the user
	print("Welcome to this simple calculator!\n")

	# Let's get the first number, and assign it to a variable
	firstNumber = float(input("What is the first number: "))

	# Now the operation
	operationSymbol = input("What is the operation: ")

	# And now the second number
	secondNumber = float(input("What is the second number: "))

	# Let's initialize a variable that will hold our answer
	result = 0

	# We will use a series of if statements to
	# determine what operation will take
	# place

	# Now let's complete the operations

	# First, addition
	if operationSymbol == '+':
		result = firstNumber + secondNumber
	# Second, subtraction
	elif operationSymbol == '-':
		result = firstNumber - secondNumber
	# Third, multiplication
	elif operationSymbol == '*':
		result = firstNumber * secondNumber
	# Fourth, division
	elif operationSymbol =='/':
		result = firstNumber / secondNumber
	# This says that there is an invalid operation symbol
	# The program then will shut down
	else:
		print("Error completing operation; Exiting...")
		return


	# Now we can print the equation with the input
	print("{} {} {} = {}".format(firstNumber, operationSymbol, secondNumber, result))

	# Let's prepare to shut down the program
	print("\nThank you, bye")

	# Let's return the main function to shut
	# down the program
	return


main()
