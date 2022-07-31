maximum_limit = int(input("Please Enter the Maximum Value : "))

total = 0

for number in range(1, maximum_limit + 1):
    
    if(number % 2 == 0):
        total += number


print("The Sum of Even Numbers: ", total)
