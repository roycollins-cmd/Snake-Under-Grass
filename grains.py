def square(number):
    sq_num = number
    if sq_num > 64:
        raise ValueError("square must be between 1 and 64")
    elif sq_num < 1:
        raise ValueError("square must be between 1 and 64")

    return number

def total():
    grain = 1
    #number = square()
    board_squares = 64
    for grain in range(0, board_squares):
        grain *= 2

    return grain

print (total())