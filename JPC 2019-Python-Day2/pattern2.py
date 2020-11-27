'''Write a program to display the following pattern where the user will choose the character to display and
the number of the rows.'''

char = input("What is the character you want to use in the pattern?")
rows = int(input("How many rows you want in the pattern?"))
for i in range(rows, 0, -1):
    for j in range(0, i):
        print(char, end=' ')
    print(" ")