#num = int(input('Enter a number: '))

def is_prime(num):
    """
    This function returns if a number is prime or not
    """
    if num == 1:
        return True
    # If given number is greater than 1
    if num > 1:
      
        # Iterate from 2
        for i in range(2, num):
      
            # If num is divisible by any number between
            # 2 and n / 2, it is not prime
            if (num % i) == 0:
                return "Not Prime"

        return "Prime"
      
    else:
        return "Not Prime"


for i in range(50):
    print(f"{i} is : {is_prime(i)}")
