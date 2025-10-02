import time
class bank :
    def  __init__(self,account_number,account_holder,balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        
        print(f"Deposited {amount}. New balance is {self.balance}.")
        
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")
    
    def check_balance(self):
        print(f"Current balance is {self.balance}.")
    
    def account_details(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: {self.balance}")
             
    def message(self):
        print('''
              1. Deposit
              2. Withdraw
              3. Check Balance
              4. Account Details
              5. Exit''')
        
    def exit(self):
        end_time = time.time()
        print("Exiting...")
        print("Thank you for using the Bank System. Goodbye!")
        print(f"Total transaction time : {(end_time - start_time):.3f} s")
        exit()
        
start_time = time.time()
print("Welcome to the Bank System")
acc_holder = input("Enter your name: ")
attempts = 0
while attempts < 4:

     acc_num = input("Enter your account number: ")
     if acc_num.isdigit() and len(acc_num) == 4:
        break
     else:
         attempts += 1
         print("Invalid input. Please enter a numeric 4-digit account number.")

if attempts == 4:
    print("Too many invalid attempts. Exiting the program.")
    exit()

bankObj = bank(acc_num, acc_holder, 0)


while True:  
    bankObj.message()
    try:
        command = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 5.")
        continue
    
    if command == 1:
        try:
         amount = float(input("Enter amount to deposit: "))
         amount > 0 or print("Amount must be positive.")
         bankObj.deposit(amount)
        except ValueError:
         print("Invalid amount. Please enter a numeric value.")
    elif command == 2:
        try:
            
            amount = float(input("Enter amount to withdraw: "))
            bankObj.withdraw(amount)
        except ValueError:
            print("Invalid amount. Please enter a numeric value.")
    elif command == 3:
        bankObj.check_balance()
    elif command == 4:
        bankObj.account_details()
    elif command == 5:
        bankObj.exit()
        break
    elif command > 5:
        print("Invalid choice. Please try again.")
        
   
            
