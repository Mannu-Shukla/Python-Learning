""""                            topic=input and output
 in that topic we study about the input function how to take the input from the users and how to give the output and study about f string for
           output function and input function always stores the value in string data type 
                              dificulty=easy
                         starting date=17th july 2026
                         ending date =18th july 2026                                                 """


################Question 1. Create a program that:Takes the user's name as input. Prints: Hello, <name>#########

name=input("enter your name:")
print(f"hello {name}")

################Question 2. Create a program that:Takes two numbers as input.Prints their:,   Sum    Difference    Product     Quotient##############

num1=int(input("enter you first number:"))
num2=int(input("enter your second number"))
print(f"sum:{num1+num2}")
print(f"difference:{num1-num2}")
print(f"product:{num1*num2}")
print(f"quotient:{num1/num2}")

################Question 3. Create a program that: Takes the user's first name and last name as input.Prints the full name in one sentence using an f-string.###########

fname=input("enter your first name")
lname=input("enter your last name")
print(f"{fname} {lname}")
print(f"{fname+" "+lname}")

###############Question 4.
#                         Print the following output using escape characters:
#                         Python
#                            Java
#                                C++
print("pyhton\n\tjava\n\t\tc++")

##############Question 5. Print the following on one line using sep and end:
#                         Apple | Mango | Orange.

print("Apple","Mango","Orange",sep="  |  ",end=".")