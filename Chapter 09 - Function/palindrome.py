# find if a string is palindrome or not



def palindrome(string):
    string = string.lower()
    reversed_string = ''

    for i in range(len(string) - 1, -1, -1):
        reversed_string += string[i]

    if string == reversed_string:
        return f'{string} is a palindrome'
    else:
        return f'{string} is not a palindrome'


print(palindrome('Madam'))
print(palindrome('Hello'))
print(palindrome('22022022'))