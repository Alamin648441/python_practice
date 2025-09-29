def fibonacci(n):
    print(f"Call fibonacci({n})")  
    if n < 0:
        print("Invalid input")
        return -1
    elif n == 0:
        print("Return 0")
        return 0
    elif n == 1:
        print("Return 1")
        return 1
    else:
        result = fibonacci(n-1) + fibonacci(n-2)
        print(f"Return fibonacci({n}) = {result}")
        return result

print(fibonacci(6))
