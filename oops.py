#1. Write a class in Python for modeling Bank Account with following requirements - 
	#- Add essential class attributes like name of the bank etc
	#- Add required instance attributes like, account number, holder name, initial amount etc
	#- add following instance methods - 
	#	- deposit_money - take user input amount
	#	- withdrawl_money - take user input amount
	#	- show_balance - this should print the current balance
	#	- show_statement - this should print last 5 transaction
  
	#- Money should not be withdrawn when there is zero balance

class bank_account:
   
   def __init__(self,bank_name,acc_no,Account_holder_name,initial_amt):

    self.bank_name = bank_name
    self.Account_holder_name = Account_holder_name 
    self.acc_no = acc_no
    self.initial_amt = initial_amt
     
    print("*"*50)
    print("BANK_ACCOUNT".center(40))
    print("*"*50)
    
    
    print("Bank Name :-",self.bank_name.upper())  #class attribute
    print("account holder name:-",self.Account_holder_name.capitalize())
    print("account no:-",self.acc_no)
    

    print("initial ammount:-",self.initial_amt)   
    print(''' choose one option:-
           1) deposit ammount
           2)withdrawl ammount
           3)balance amount
           4)exit
             ''')
    
     
   def deposit_money(self):
     deposit_amt = int(input("enter amount to deposit :"))
     self.initial_amt += deposit_amt
     print("deposit ammount:-",deposit_amt)
     self.show_balance()
     

      
   def withdrawl_money(self):
     withdrawl_amt = int(input("enter amount to be withdrawl:-"))
     
     if self.initial_amt>withdrawl_amt:
       self.initial_amt -= withdrawl_amt
     else:
       print("insufficient balance")
     print("withdrawl ammount:-",withdrawl_amt)
     self.show_balance()
       
    
   def show_balance(self):
     balance_amt = self.initial_amt
     print("balance amount:-",balance_amt)

   def show_statement(self):
     choice = int(input("enter choice:-"))
     if choice == 1:
       self.deposit_money()
       self.show_statement()
     elif choice == 2:
       self.withdrawl_money()
       self.show_statement()
     elif choice == 3:
       self.show_balance()  
       self.show_statement()
     elif choice == 4:
        exit  
     else:
       print("invalid choice") 
       self.show_statement() 
       

bank_name =input("Bank Name:-")
correct  = False
while not correct:
       acc_no = input("Account Number:-")
       if len(acc_no)<=11:
          print("ok you can continue")
          correct = True
       else:
          print("please enter your 11 digit number")
   
     
Account_holder_name = input("Account Holder Name:-")
initial_amt = 0

obj1 = bank_account(bank_name,acc_no,Account_holder_name,initial_amt)
obj1.show_statement()
   
            