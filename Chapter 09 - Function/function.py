
# Null function

# def function():
#     return None



x = int(input('Enter value of x: '))
y = int(input('Enter value of y: '))
z = int(input('Enter value of z: '))

def add(a,b):
    return a + b

def subtract(a,b):
    return a - b


sum = add(x, y)
print('x + y = ',sum)

final_result = subtract(sum, z)
print('(x + y) - z = ',final_result)




