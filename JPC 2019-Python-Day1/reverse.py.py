'''Write a program to take from a user an integer number of 4 digits (this means that this number should be
between 1000 and 9999). Your program should reverse it.'''


n = int(input("Enter a positive number in the range [1000, 9999]:")) 
temp = n
rev = 0
if n >= 1000 and n <= 9999:
    while(n > 0): 
        a = n % 10
        rev = rev * 10 + a 
        n = n // 10
    print("The reverse of %d is %d" %(temp,rev)) 
else:
    print("Your number does not have 4 digits! Please try again.")
    

  