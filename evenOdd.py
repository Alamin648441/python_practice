n = input("Enter a number: ")

try:
    num = int(n)
    
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")
except ValueError:
    print("Invalid input, please Enter any number only .")