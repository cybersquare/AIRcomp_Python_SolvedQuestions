'''
Write a program to display the following pattern 
where the user will choose the character to display.'''

char = input("What is the character you want to use in the pattern?")
for i in range(5):
    for j in range(i):
        print(char, end='')
    print(" ")
    