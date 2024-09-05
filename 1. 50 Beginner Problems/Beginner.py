"""
A collection of 50 problems to solve using only Google and my own code. This is being done for
Practice and a better mastery of the language.

EASY PROBLEMS
"""

# 1. Print the text "Hello, World!" to the console.
def HellowWorld():
    print('Hello, World!')


# 2. Input two numbers and print their sum.
def AddTwoNumbers(firstNum, secondNum):
    return int(firstNum + secondNum)

# 3. Given the radius, calculate and print the area of a circle.
def AreaOfACircle(radius):
    return (3.14159 *(float(radius) ** 2.0))

#print(AreaOfACircle(35))

# 4. Calculate simple interest given principal, rate, and time.
def SimpleInterest(principal, rate, time):
    return (principal * rate * time) / 100

#print(SimpleInterest(10000.00, 3.875, 5))

# 5. Input a number and print whether it's odd or even.
def OddOrEven(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

#print(OddOrEven(20))

# 6. Given two numbers, print the larger one.
def MaxNumber(firstNum, secondNum):
    if firstNum > secondNum:
        print(firstNum)
    else:
        print(secondNum)

#MaxNumber(35, 36)

# 7. Input a temperature in Celsius and convert it to Fahrenheit.
def CelsiusToFarenheit(celsius):
    return celsius * (9 / 5) + 32

#print(CelsiusToFarenheit(32))

# 8. Input a number and print if it’s positive, negative, or zero.
def PosNegZero(number):
    if number == 0:
        return "Zero"
    elif number < 0:
        return "Negative"
    else:
        return "Positive"

#print(PosNegZero(-0.001))

# 9. Input a number and print its multiplication table up to 10
def MultTable(number):
    for i in range(11):
        print(f"{i} * {number} = {int(i) * int(number)}")

#MultTable(256)

# 10. Calculate and print the factorial of a number.
def ShowFactorial(number):
    r = range(number + 1)
    reversed_r = reversed(r)
    total = 1
    digits = f'{number}! = '
    for num in reversed_r:
        if num > 0:
            if num == 1:
                digits += f"{num} "
            else:
                digits += f"{num} x "
            total = num * total
        elif num == 0:
            digits += f" = {total}"
    print(f"{digits}")   

#ShowFactorial(1)


"""
INTERMEDIATE PROBLEMS
"""


