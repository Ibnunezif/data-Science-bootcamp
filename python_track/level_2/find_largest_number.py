def largest_number(list_data): # accepts list as an input
    largest = float("-inf") #initialize largest number with a very small number

    for nums in list_data:
        largest = max(largest,nums) # maximize largest number

    return largest # return once computed

while True:
    print("Give me space separated number (e.g 2 3 4 5) then press Enter")
    number = list(map(int,input().split()))
    print(f"The largest nnumber is = {largest_number(number)}")
