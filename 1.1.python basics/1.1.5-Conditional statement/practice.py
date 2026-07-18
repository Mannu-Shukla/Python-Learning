""""                            topic=conditional statement
 in that topic we study about the condition by which we gave the power to code take decision based on condition which we gave
                              dificulty=medium
                         starting date=17th july 2026
                         ending date =18th july 2026                                                 """

#########QUESTION 1. Write a program that:
#                    Takes the user's age as input.
#                    Prints:
#                    "Eligible to Vote" if the age is 18 or above.
#                    Otherwise prints "Not Eligible to Vote".

age=int(input("enter your age:"))
if age>=18:
    print("eligible to vote")
else:
    print("not eligible to vote")


#########QUESTION 2. Write a program that:
#                    Takes a number as input.
#                    Prints whether it is Even or Odd.

num=int(input("enter your number:"))
if num%2==0:
    print(f"your number {num} is even.")
else:
    print(f"your number {num} is odd.")

#########QUESTION 3. Take marks as input.
#                    Print:
#                    A → 90–100
#                    B → 75–89
#                    C → 60–74
#                    Fail → Below 60

marks=int(input("enter your marks:"))
if marks>=90 and marks<=100:
    print("you got A")
elif marks>=75 and marks<=89:
    print("you got B")
elif marks>=60 and marks<=74:
    print("you got C")
elif marks<60:
    print("you failed")

########QUESTION 4. Take three numbers as input.
#                    Print the largest number.
#                    ❌ Do not use max().
#                    Use only if, elif, and else.

n1=int(input("enter the first number:"))
n2=int(input("enter the second number:"))
n3=int(input("enter the third number:"))
if n1>n2:
    if n1>n3:
        print(f"the {n1} is largest number you have entered.")
    else:
        print(f"the {n3} is the largest number you have entered.")
elif n2>n1:
    if n2>n3:
        print(f"the {n2} is largest number you have entered.")
    else:
        print(f"the {n3} is the largest number you have entered.")
elif n3>n1:
    if n3>n2:
        print(f"the {n3} is largest number you have entered.")
    else:
        print(f"the {n2} is the largest number you have entered.")
elif n1==n2==n3:
    print("all numbers are same.")

#########QUESTION 5.Create a simple login system.
#                   Requirements:
#                   Username = admin
#                   Password = 1234

#                   If both are correct:

#                   Login Successful

#                   If the username is wrong:

#                   Invalid Username

#                   If the password is wrong:

#                   Invalid Password

#                   If both are wrong:

#                   Invalid Username and Password

username=input("enter the username::")
password=input("enter you password::")

if username=="admin" and password=="1234":
    print("login successful.")
elif username=="admin" and password!="1234":
    print("invalid password.")
elif username!="admin" and password=="1234":
    print("invalid username.")
else:
    print("invalid username and password.")






