def sum_of_elements(a_list):
    total = 0;

    for i in a_list:
        total += i;

    return total


a_list = [3,5,6,7,1,4,10]

result = sum_of_elements(a_list)

print("Sum of Elements of a_list is: ", result)
        
