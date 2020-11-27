'''Write a program to ask a user to enter a positive integer in the range [0,10] using the keyboard. Your program should
compute and display on the monitor its double factorial. The double factorial n!! of a positive integer n is defined
as follows:

1) 0!!=l , 1!!=1
2) and for n >1 the double factorial is
a) n !! = n * (n - 2) (n - 4)* . .. 3* 1 if n is odd or
b) n !! = n * (n - 2) (n - 4)* . .. 4* 2 if n is even'''

doublefact = 0
def doublefactorial(n): 
    if (n == 0 or n == 1): 
        return 1 
    return n * doublefactorial(n - 2)
number = int(input("Enter one positive number in the range [0,10]:"))
if number >= 0 and number <= 10:
    doublefact = doublefactorial(number)
    print("%d!!=%d" %(number, doublefact))
else:
    print("%d is not in the range [0,10]" %number)

    
