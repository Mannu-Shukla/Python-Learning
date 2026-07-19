#############QUESTION 1. Print:
#                        1
#                        2
#                        3
#                        4
#                        5
#                        using a for loop.   
for i in range(1,6):
    print(i)

##############QUESTION 2. Print all even numbers from 1 to 20.

for i in range(1,21):
    if i%2==0:
        print(i)

##############QUESTION 3. Print the multiplication table of 7.

for i in range(1,71):
    if i%7==0:
        print(i)
    
################QUESTION 4. Print the following:
#                           10
#                           9
#                           8
#                           7
#                           6
#                           5
#                           4
#                           3
#                           2
#                           1
#                           using only one for loop.

for i in range(10,0,-1):
    print(i)

##################QUESTION 5. Without using if, print:
#                             5
#                             10
#                             15
#                             20
#                             25
#                             30
#                             35
#                             40
#                             45
#                             50
#                             using only range().

for i in range(5,51,5):
    print(i)              

####################QUESTION 6. Without using nested loops, can you print:
#                               A
#                               B
#                               C
#                               D
#                               E
#                               using a for loop?          

for i in "ABCDE":
    print(i)