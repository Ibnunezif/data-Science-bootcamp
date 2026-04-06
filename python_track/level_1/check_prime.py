def is_prime(number):
    if number <= 1:
        return False # edge case 0,1 are not prime 
    
    i = 2
    # Check divisors up to the square root of num
    while i * i <= number:
        if number % i == 0:  # If divisible by i, it's not prime
            return False
        i += 1

    return True #Since there is no any devisor for the number then the number is prime


while True : # always run until
    num = int(input())
    print(is_prime(num)) 
    
