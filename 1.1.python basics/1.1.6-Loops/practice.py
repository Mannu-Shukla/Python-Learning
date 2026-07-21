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

###################QUESTION 7. Sum of Numbers Take a number n from the user and print the sum from 1 to n.

num=int(input("enter the nth number::"))
sum=0
for i in range(num+1):
    sum=sum+i
print(sum)

###################QUESTION 8. Take a number from the user and print its factorial.

num=int(input("enter the nth number::"))
product=1
for i in range(num,0,-1):
    product=product*i
print(product)

###################QUESTION 9. Count Digits..Take a number from the user and count how many digits it has.dpnt make string

num=int(input("enter the digit"))
count=0
while num>0:
    num=num//10
    count=count+1

###################QUESTION 10. Reverse a Number Take a number from the user and print it in reverse.dont make string

num=int(input("enter the digit::"))
reverse=0
while num>0:
    lstdigit=num%10
    num=num//10
    reverse=(reverse*10)+lstdigit
print(reverse)



##################QUESTION 10. Create a password program with these rules:

#                             The correct password is "python123".
#                             The user gets only 3 attempts.
#                             If the password is correct:
#                             Access Granted
#                             If all 3 attempts are wrong:
#                             Too many failed attempts.
#                             Access Denied.


for att in range(3):
    password=input("enter the password::")
    if password=="python123":
        print("access granted")
        break
    elif att==2:
        print("too many failed attempt.")
        print("acces denied.")
    elif password!="python123":
        print("wrong password")

###################QUESTION 11. FizzBuzz.....Print numbers from 1 to 30.

#                               Rules:

#                               If a number is divisible by 3, print Fizz.
#                               If divisible by 5, print Buzz.
#                               If divisible by both 3 and 5, print FizzBuzz.
#                               Otherwise, print the number.

for i in range(1,31):
    if i%3==0 and i%5==0:
        print("frizzbuzz")
    elif i%3==0:
        print("fizz")
    elif i%5==0:
        print("buzz")
    
    else:
        print(i)

##################QUESTION 12. Print:
#                              *
#                              **
#                              ***
#                              ****
#                              ***** 
#                              ******

for i in range(1,7):
    for j in range(i):
        print("*",end="")
    print()

##################QUESTION 13. Print:
#                              12345
#                              12345
#                              12345
#                              12345

for i in range(1,6):
    for j  in range(1):
        print("12345",end="")
    print()
