"""
The collatz sequence AKA the simplest impossible math problem
"""

def collatz(number):
    #check if the number is even
    if number % 2 == 0:
        for i in range(1, number): #print loop to show each number after every calculation
            number = number // 2
            if number == 1:
                break # stop when the number is 1 - otherwise it prints 0 up to the number
            print(number)
        return number
    else: #check if the number is odd (not even)
        for i in range(1, number): #print loop to show each number after every calculation
            number = number * 3 + 1
            if number == 1:
                break  # stop when the number is 1 - otherwise it prints 0 up to the number
            print(number)
        return number

value  = int(input("Enter a number: "))
sequence = collatz(value)
print(sequence)