'''Write a program to find the highest number in a sequence of numbers a user will input.
You do not know how many numbers the user will enter but if the user enters -1 your program will
stop taken the input from the user.'''
number = 0
listnums = []
endnum = -1
while number!=endnum:
    number = int(input("Enter an integer number: "))
    listnums.append(number)
print("The largest number in the sequence is ", max(listnums))
