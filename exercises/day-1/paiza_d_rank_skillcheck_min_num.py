def min_num(numbers: list):
    result = numbers[0]
    for num in numbers:
        if num < result:
            result = num
    return result

if __name__ == '__main__':
    print(min_num([10, 2, 100, 5, 7]))

