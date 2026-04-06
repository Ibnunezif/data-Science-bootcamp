# Create a dictionary to store calculated values (our "memo")
memo = {}

def fibonacci(num):
    if num < 0:
        return "Not valid input"
    if num == 0 or num == 1:
        return 1
    
    # Check if we have already calculated this number before
    if num in memo:
        return memo[num]
    
    # Calculate, store in memo, and then return
    memo[num] = fibonacci(num-1) + fibonacci(num-2)
    return memo[num]

while True:
    print("Give me the number: ",end="")
    number = int(input())
    print(f"the answer is {fibonacci(number)}")