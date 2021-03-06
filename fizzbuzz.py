def fizzbuzz():
    res = ""
    for num in range(1, 101):
        if (num % 15 == 0):
            res += "FizzBuzz"
        elif (num % 5 == 0):
            res += "Buzz"
        elif (num % 3 == 0):
            res += "Fizz"
        else:
            res += str(num)
    #print(res)
    return res

fizzbuzz()