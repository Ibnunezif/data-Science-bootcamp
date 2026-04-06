def fibonacci (num):
    if num < 0:
        return "Not valid input"
    if num == 1 or num == 0:
        return 1
    
    return fibonacci(num-1) + fibonacci(num-2)

print(fibonacci(100))