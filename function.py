#1. Write a function to print multiplication table of a number given by user.
  #  Output:
#     Enter the number of which the user wants to print the multiplication table:  13
 #       The Multiplication Table of:  13
  #      13 x 1 = 13
   #     13 x 2 = 26
    #    13 x 3 = 39
     #   13 x 4 = 52
      #  13 x 5 = 65
      #  13 x 6 = 78
      #  13 x 7 = 91
      #  13 x 8 = 104
      #  13 x 9 = 117
      #  13 x 10 = 130

num1 = int(input("enter number:-"))

def table(num1):
  for i in range(1,11):
    res = i * num1
    print(num1 ,"*",i,"=",res)

table(num1)    

print("--------------------------------------------------------")

#2. Write a program to convert given list into a single string, list may contain integers.

list = [1,2,3,4,5,6]

typecast = str(list)
print(typecast)
print(type(typecast))

print("--------------------------------------------------------")

#3. Write a calculator in Python. with following requirements
    # Take two number input from user
    # Ask the operation the user want to perform with above two numbers
    # Allowed operations are - addition, subtraction, multiplication, division, square
    # Show the result of a operation to the user


num1 = int(input("enter 1st no:-"))
num2 = int(input("enter 2nd no:-"))

opr = input("enter which operation do you like to perform:-")

def add(num1,num2):
  addition = num1 + num2
  print("addition of two val:",addition) 

def sub(num1,num2):
  substracation = num1 - num2
  print("substracation of two val:",substracation) 

def mul(num1,num2):
  multiplication = num1 *num2
  print("multilication of two val:",multiplication) 

def div(num1,num2):
  division = num1 / num2
  print("division  of two val:",division ) 

if opr == "+":
  add(num1,num2)
elif opr == "-":
  sub(num1,num2)
elif opr == "*":
  mul(num1,num2)
elif opr == "/":
  div(num1,num2)
else:
  print("invalid operator")     

print("--------------------------------------------------------") 


#4) Write a function that accepts a number and return cube of it.

num2 = int(input("enter number:-"))

def cube(num2):
  res = num2**3
  print("cube of the given no:-",res)

cube(num2)