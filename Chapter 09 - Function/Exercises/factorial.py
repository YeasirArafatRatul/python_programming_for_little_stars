
# 5! = 5*4 = 20*3 = 60*2=120*1 =120

a = int(input("Enter Number: "))


def factorial(a):
    """
    this function will take a number and return the factorial value of that number.
    """
    factorial = 1

    while a > 0:
        factorial = factorial * a
        a -= 1
    return factorial

result = factorial(a)
print(f"Factorial is = {result}")





