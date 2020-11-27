'''Write a program to allow users to input three numbers.
Your program should display:
1. The three numbers entered by the user
2. The smallest of these 3 numbers
3. The middle of these 3 numbers
4. The largest of these 3 numbers.'''
largest = 0
smallest = 0
mid = 0
number1 = int(input("Enter the first number:"))
number2 = int(input("Enter the second number:"))
number3 = int(input("Enter the third number:"))
if number1 >= number2 and number1 >= number3:
    largest = number1
    if number2 > number3:
        mid = number2
        smallest = number3
    else:
        mid = number3
        smallest = number2
if number2 >= number1 and number2 >= number3:
    largest = number2
    if number1 > number3:
        mid = number1
        smallest = number3
    else:
        mid = number3
        smallest = number1
if number3 >= number2 and number3 >= number1:
    largest = number3
    if number1 > number2:
        mid = number1
        smallest = number2
    else:
        mid = number2
        smallest = number1

print("You have entered %d,%d and %d" %(number1,number2,number3))
print("The smallest number is: ", smallest)
print("The middle number is: ", mid)
print("The larget number is: ", largest)
