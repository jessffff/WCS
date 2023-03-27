# Square of a number
def square(num):
    return num ** 2


# Cube of a number
def cube(num):
    return num ** 3



# Absolute value
def absolute_value(num):
    if num < 0:
        return -num
    else:
        return num



# Factorial of a number
def factorial(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result



# Mode of a list of numbers
def mode(numbers):
    count_dict = {}
    for num in numbers:
        if num not in count_dict:
            count_dict[num] = 1
        else:
            count_dict[num] += 1
    max_count = 0
    mode = None
    for num, count in count_dict.items():
        if count > max_count:
            max_count = count
            mode = num
    
    return mode



# Average of a list of numbers
def average(numbersN):
    total = 0
    for num in numbersN:
        total += num
    return total / len(numbersN)


# Minimum of a list of numbers
def minimum(numbersM):
    min_num = numbersM[0]
    for num in numbersM:
        if num < min_num:
            min_num = num
    return min_num



# Maximum of a list of numbers
def maximum(numbersS):
    max_num = numbersS[0]
    for num in numbersS:
        if num > max_num:
            max_num = num
    return max_num


def mode2(numbers):
    count_dict = {}
    for num in numbers:
        if num not in count_dict:
            count_dict[num] = 1
        else:
            count_dict[num] += 1
    
    max_count = 0
    modes = []
    for num, count in count_dict.items():
        if count > max_count:
            max_count = count
            modes = [num]
        elif count == max_count:
            modes.append(num)
    
    return modes

