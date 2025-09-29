import time
class Calculator:
    def show_menu(self):
        print("Select operation.")
        print("1.Add")
        print("2.Subtract")
        print("3.Multiply")
        print("4.Divide")
        print("5.Modulus")
        print("6.Power")
        print("7.Square Root")
        print("8.Factorial")
        print("9.Exit")
    def add(self ,a,b):return a+b
    def sub(self ,a,b):return a-b
    def mul(self ,a,b):return a*b
    def div(self ,a,b):
        if b==0 :
            raise ValueError("Cannot divide by zero")
        return a/b
    def mod(self ,a,b):
        if b==0 :
            raise ValueError("Cannot mod by zero")
        return a%b
    def pow(self ,a,b):return a**b
    def sqrt(self ,a):
        if a<0 :
            raise ValueError("Cannot take square root of negative number")
        return a**0.5
    def fact(self ,a):
        if a<0 :
            raise ValueError("you cannot take factorial of negative number")
        if a==0 or a ==1 :
            return 1
        result = 1
        for i in range(2,a+1):
            result *= i
        return result
    def Exit(self):
        print("Exiting...")
        end_time = time.time()
        print(f"Total time taken: {end_time - start_time} seconds")
        exit()
        4
    
cal = Calculator()
start_time = time.time()
while True:
    cal.show_menu()

    choice = input("Enter choice(1-9): ")
    if choice == '9':
        cal.Exit()
    elif choice in ['1','2','3','4','5','6']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        match choice:
            case '1':
                print(f"{num1}+ {num2} = {cal.add(num1,num2)}")
            case '2':
                print(f"{num1}- {num2} = {cal.sub(num1,num2)}")
            case '3':
                print(f"{num1}* {num2} = {cal.mul(num1,num2)}")
            case '4':
                try:
                    print(f"{num1}/ {num2} = {cal.div(num1,num2)}")
                except ValueError as e:
                    print(e)
            case '5':
                try:
                    print(f"{num1}% {num2} = {cal.mod(num1,num2)}")
                except ValueError as e:
                    print(e)
            case '6':
                print(f"{num1}** {num2} = {cal.pow(num1,num2)}")
    elif choice in ['7','8','9']:
        num = float( input("Enter number: "))
        match choice :
            case '7':
                try:
                    print(f"sqrt of {num} = {cal.sqrt(num)}")
                except ValueError as e:
                    print(e)
            case '8':
                try:
                    print(f"{num}! = {cal.fact(int(num))}")
                except ValueError as e:
                    print(e) 
                       
    else:
        print("Invalid input")
    
    
        