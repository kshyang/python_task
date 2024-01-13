'''Write a function that accepts a positive integer as a parameter and then returns a
representation of that number in binary (base 2).'''

def decimal(num):
    number = ''
    while num > 0:
        number = str(num % 2) + number
        num = num // 2
    print(number)
    
if __name__ == "__main__":
    num = int(input("Enter a positive integer: "))
    if num < 0:
        print("Please enter a positive integer.")
    else:
        decimal(num)
        

#Question no 2
'''Write and test a function that takes an integer as its parameter and returns the
factors of that integer. (A factor is an integer which can be multiplied by another to
yield the original).'''

def get_factors(num):
    factors = []
    for i in range(1, abs(num) + 1):
        if num % i == 0:
            factors.append(i)
    return factors

if __name__ == "__main__":
    try:
        num = int(input("Enter an integer: "))
        result = get_factors(num)
        print(f"The factors of {num} are: {result}")
    except ValueError:
        print("Invalid input")


#Question no 3
'''Write and test a function that determines if a given integer is a prime number. A
prime number is an integer greater than 1 that cannot be produced by multiplying
two other integers.'''

def is_prime(number):
    """Determine whether the input number is prime or not."""
    for i in range(2, number):
        if number % i == 0:
            print(f"The {number} is not prime number.")
            break
    else:
        print(f"The {number} is prime number.")


if __name__ == "__main__":
    try:
        number = int(input("Enter a number: "))
        if number < 2:
            print(f"{number} is not a prime number")

        else:
            is_prime(number)

    except ValueError:
        print("Invalid input")


#Question no 4
'''Computers are commonly used in encryption. A very simple form of encryption
(more accurately "obfuscation") would be to remove the spaces from a message
and reverse the resulting string. Write, and test, a function that takes a string
containing a message and "encrypts" it in this way.'''

def encrypt_message(msg):
    msg = "".join(reversed(msg.split()))
    print (msg)

if __name__ == "__main__":
    try:
        msg = input("Enter a message: ")
        encrypted_msg = encrypt_message(msg)

    except ValueError:
        print("Invalid value.")


#Question no 5
'''Another way to hide a message is to include the letters that make it up within
seemingly random text. The letters of the message might be every fifth character,
for example. Write and test a function that does such encryption. It should
randomly generate an interval (between 2 and 20), space the message out
accordingly, and should fill the gaps with random letters. The function should
return the encrypted message and the interval used.
For example, if the message is "send cheese", the random interval is 2, and for
clarity the random letters are not random:
send cheese
s e n d c h e e s e
sxyexynxydxy cxyhxyexyexysxye'''

import random
def hidden(word):
    sum = ''
    for i in word:
        c = random.randint(2,21)
        if  i != ' ':
            sum = sum + i + 'x' * c
        else:
            sum += i
    
    return sum

message = input("Enter a message: ")
print(hidden(message))

#Question no 6
'''Write a program that decrypts messages encoded as above.'''

message = "sxyexynxydxy cxyhxyexyexysxye"
print("Encoded message:")
print()
