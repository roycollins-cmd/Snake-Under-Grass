"""
The collatz sequence AKA the simplest impossible math problem
"""

def collatz(number):
    if number % 2 == 0:
        for i in range(1, number):
            number = number // 2
            if number == 1:
                break
            print(number)
        return number
    else:
        for i in range(1, number):
            number = number * 3 + 1
            if number == 1:
                break
            print(number)
        return number

value  = int(input("Enter a number: "))
sequence = collatz(value)
print(sequence)