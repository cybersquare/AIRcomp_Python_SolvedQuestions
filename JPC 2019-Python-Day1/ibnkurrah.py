'''Design a program to compute the first 15 Ibn Kurrah numbers. Ibn Kurrah numbers are of the form:
3*2n -1
for n ≥ 0.
Your program should display 5 Ibn Kurrah numbers per line as in the sample below.
Sample Run:
2 5 11 23 47
95 191 383 767 1535
3071 6143 12287 24575 49151'''
import math


for i in range(15):

    power = math.pow(2,i)
    ibn = 3*power-1
    print(ibn, end=' ')
    # listIbn.append(ibn)
    # print(listIbn)
    if i == 4 or i == 9 or i == 14:
        print("\n")
  


    
        
    


  
   

