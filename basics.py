
#1)Write a program to iterate the first 10 numbers and in each iteration, print the sum of the current and previous number.

sum = 0
previous_no = 0
for i in range(10):
  current_no = i 
  previous_no = abs(current_no - 1)
  sum = current_no + previous_no 
  print("Current Number:",current_no, " Previous Number:", previous_no, "Sum:",sum)


#2)Write a program to accept a string from the user and display characters that are present at an even index number.

Given = "I am Learning Python"

for i in Given[0::2]:
  print(i)


#3) Check if the first and last number of a list is the same
#Given:  numbers_x = [10, 20, 30, 40, 10]
         #numbers_y = [75, 65, 35, 75, 30]

list1 = [10, 20, 30, 40, 10]
list2 = [75, 65, 35, 75, 30]

if list1[0]==list1[-1]:
  print("Result is True")
else:
  print("Result is False")  
if list2[0]==list2[-1]:
  print("Result is True")  
else:
  print("Result is False")    
  

#5)Write a program to check if the given number is a palindrome number.
   #Note: A palindrome number is a number that is same after reverse. For example 545, is the palindrome numbers

num =(input("number is palindrom or not:"))
print(num[:3])
print(num[::-1])
if num == num[::-1]:
   print("number is palindrom")
else: 
   print("number is not palindrom") 


def palindrom(num):
   rev = num
   if num == rev[::-1]:
      return num
   
number =(input("enter number:-"))
print("number-",number)
print("number-",number[::-1])
if palindrom(number):
   print("number is palindrom")
else: 
   print("number is not palindrom") 






