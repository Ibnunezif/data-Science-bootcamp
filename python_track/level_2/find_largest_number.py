def largest_number(list_data): # accepts list as an input
    largest = float("-inf") #initialize largest number with a very small number

    for nums in list_data:
        largest = max(largest,nums) # maximize largest number

    return largest # return once computed

print(largest_number([7,8,45,3,-9,67,569,12]))