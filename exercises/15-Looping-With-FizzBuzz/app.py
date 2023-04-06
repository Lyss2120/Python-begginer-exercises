def fizz_buzz():
    # your code here
    for x in range(1, 101):
        if (x % 5 == 0):
            if (x % 3 == 0):
                print("FizzBuzz")
            else:
                print("Buzz")
        else:
            if (x % 3 == 0):
                print("Fizz")
            else:
                print(x)


fizz_buzz()