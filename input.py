
#1)Write a program to accept two numbers from the user and calculate multiplication

num1 = int(input("enter 1st no-"))
print(num1)
num2 = int(input("enter 2nd no-"))
print(num2)

mul = num1 * num2
print(mul)

#2)Display three string “Name”, “Is”, “James” as “Name**Is**James” using print()

s1 = "Name"
s2 = "Is"
s3 = "James"
print('"',s1,'**',s2,'**',s3,'"')

#3) Accept a list of 5 float numbers as an input from the user
  #Output: [78.6, 78.6, 85.3, 1.2, 3.5]
l1 = []

for i in range(5):
 ele = float(input("enter element"))
 l1.append(ele)
print(l1)

#4) Write a program to take three names as input from a user in the single input() function call.

for i in range(3):
 str = input("enter name")
 print(str)

#5)Write a program to use string.format() method to format the following three variables as per the expected output
#Given:total_money = 1000
      #quantity = 3
       #price = 450
   # Output: I have 1000 dollars so I can buy 3 football for 450.00 dollars.

   