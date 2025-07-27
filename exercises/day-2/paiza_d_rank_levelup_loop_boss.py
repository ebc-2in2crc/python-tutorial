if __name__ == '__main__':
    for i in range(101):
        if i % 15 == 0:
            print("FizzBuzz")
        if i % 3 == 0:
            print("Fizz")
        if i % 5 == 0:
            print("Buzz")
        else:
            print(i)