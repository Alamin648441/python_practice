import time
from datetime import datetime

class Card: 
    def __init__(self, card_num, card_holder, balance=0 ):
        self.card_num = card_num
        self.card_holder = card_holder
        self.balance = balance
        self.transaction_history = []
    
    def deposit(self, amount):
        self.balance += amount
        now = datetime.now()
        self.transaction_history.append(f"Deposited {amount} New balance is {self.balance} issue Time: {now.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Deposited {amount} New balance is {self.balance :.3f}")
    
    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            now = datetime.now()
            self.transaction_history.append(f"Withdraw {amount} New balance is {self.balance} issue time: {now.strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"Withdraw {amount}\nYour New balance is {self.balance:.3f}")
    
    def show_details(self):
        print(f'''
              Card Holder name: {self.card_holder}
              Card number : {self.card_num}
              Your balance is : {self.balance}
                           
              ''')
    def balance_check(self):
        print(f"Your balance is : {self.balance:.3f}")
        
    @staticmethod
    def message():
        print('''
              1. Deposit
              2. Withdraw
              3. Account details
              4. Transaction History 
              5. Balance
              6. Exit 
              
              ''')
    @staticmethod
    def input_fun(inp_msg, dtype = str):
        while True:
            try:
                return dtype(input(inp_msg))
            except ValueError:
                print("Invalid input ! please try again ")
            
                
            
        
    def transaction_histories(self):
        print("Your transaction History is : ")
        for history in self.transaction_history:
            print(f"{history}\n")
            
            
    @staticmethod
    def exit():
        end_time = time.time()
        process_time = end_time - start_time 
              
        print("Exiting ....")
        print(f"Total processing time : {process_time}")
        print(f"Thank you for using the Bank System. Goodbye!")
        exit()
    
start_time = time.time()
print(f"Welcome to the bank system ")
holder_count = 0
while holder_count < 4:
    acc_holder = input("Enter your Name :")
    if acc_holder.isalpha() and len(acc_holder) >=4:
        break
    else:
        holder_count +=1
        print("Invalid input. Please enter your valid name .")

if holder_count == 4:
    print(f"too many time attempts . please try again letter")
    Card.exit()

h_num_c = 0
while h_num_c<4 :
    acc_num = input("Enter your valid number: ")
    
    if acc_num.isdigit() and len(acc_num) >=4 :
        break
    else:
        h_num_c += 1
        print("Invalid input. Please enter a numeric 4-digit account number.")
    
if h_num_c == 4 :
    print(f"too many time attempts . please try again letter")
    Card.exit()
    
card_obj = Card(acc_num, acc_holder, 0)

while True:
    card_obj.message()
    command = card_obj.input_fun("Enter your choice 1-6 :" , int)
    
    if command == 1:
        amount = card_obj.input_fun("Enter deposit Amount :" , float)
        card_obj.deposit(amount)
    elif command == 2:
        amount = card_obj.input_fun("Enter Withdraw Amount :",float)
        card_obj.withdraw(amount)
    elif command == 3:
        card_obj.show_details()
    elif command == 4:
        card_obj.transaction_histories()
    elif command == 5:
        card_obj.balance_check()
    elif command == 6:
        card_obj.exit()
        break
    elif command > 6:
        print("Invalid input please try again")
        