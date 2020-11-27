'''Write a program to display numbers between 100 and 999 with different digits. Examples: 102, 465, 798 and not like 101,
252 , 373.... Your program should count them.
102 103 104 105 106 107 108 109 120 123
124 125 126 127 128 129 130 132 134 135
...
954 956 957 958 960 961 962 963 964 965
967 968 970 971 972 973 974 975 976 978
980 981 982 983 984 985 986 987
There are ??? numbers with different digits between 100 and 999!
Note: your program should display the right number instead of ??? in the previous line.'''


num = 0
count =0
for i in range(100, 1000):
    numStr = str(i)
    if numStr[0]!=numStr[1] and numStr[0]!=numStr[2] and numStr[1]!=numStr[2]:
        print(i, end=' ')
        count = count+1
print("\n")
print("There are %d numbers with different digits between 100 and 999!" %count)
