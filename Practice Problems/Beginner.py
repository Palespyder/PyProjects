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


# 11. Input a number and check if it’s prime.
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

#print(is_prime(7))  # Output: True


# 12. Input a number and calculate the sum of its digits.
def SumOfDigits(num):
    numString = []
    numString[:] = str(num)
    total = 0
    for i in range(len(numString)):
        total += int(numString[i])
    return total

#print(SumOfDigits(1234554251))


#13. Input three numbers and print the largest one.
def LargestOfThree(numOne, numTwo, numThree):
    nums = [numOne, numTwo, numThree]
    nums = sorted(nums)
    return nums[len(nums) - 1]

#print(LargestOfThree(175, 65, 37))

# 14. Input a string and check if it’s a palindrome.
def PalindromCheck(stringIn):
    stringOne = []
    stringOne[:] = stringIn
    stringTwo = []
    stringTwo[:] = reversed(stringIn)
    if stringOne == stringTwo:
        return "Palindrome"
    else:
        return "Not Palindrome"

#print(PalindromCheck("rotator"))

# 15. Generate and print the Fibonacci sequence up to a given number of terms.
def GenFibo(toNum):
    fib_sequence = [0, 1]  # Starting values of the Fibonacci sequence
    while len(fib_sequence) < toNum:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])  # Add the last two numbers
    return fib_sequence[:toNum]  # Return the sequence up to 'n' terms

#print(GenFibo(25))

# 16. Input a number and print it in reverse.
def ReverseNum(num):
    numSplit = []
    numSplit[:] = str(num)
    numSplit = reversed(numSplit)
    reversedNum = ''.join(numSplit)
    return int(reversedNum)

#print(ReverseNum(8675309))

# 17. Input a string and count the number of vowels.
def CountVowels(stringIn):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    newString = []
    newString[:] = stringIn
    for letter in newString:
        if letter in vowels:
            count += 1
    return count

#print(CountVowels('Jason'))

# 18. Input a year and check if it's a leap year.
def IsLeapYear(year):
    if year % 4 == 0:
        return "Leap Year"
    else:
        return "Not a Leap Year"

#print(IsLeapYear(1390))

# 19  Input a range and calculate the sum of all even numbers within it.
def SumOfRange(low, high):
    sum = 0
    for i in range(low, high + 1):
        if int(i) % 2 == 0:
            sum += int(i)
    return sum

#print(SumOfRange(1, 10))

# 20. Input two numbers and find their Least Common Multiple (LCM).
def LCM(num1, num2):
    num1List = []
    num2List = []
    for i in range(1, 101):                
        if (int(i) * num1) in num2List:
            return int(i) * num1
        else:
            num1List.append(int(i) * num1)
        if (int(i) * num2) in num1List:
            return (int(i) * num2)
        else:
            num2List.append(int(i) * num2)

#print(LCM(24, 300))

# 21. Input two numbers and find their Greatest Common Divisor (GCD). *Had to look this one up, been too long since I did these problems.
def GCD(num1, num2):
    while num2 != 0:
        num1, num2 = num2, num1 % num2
    return num1

#print(GCD(48, 18))
    
# 22. Input a number and print a right-angled triangle of stars.
def PrintTriangle(num):    
    for i in range(num + 1):        
        print("*" * i)


#PrintTriangle(14)

# 23. Input a binary number (as a string) and convert it to decimal.
def BinToDec(binaryNum):
    conversion = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384]
    binaries = []
    binaries[:] = str(binaryNum)
    list(reversed(binaries))
    r_binaries = binaries[::-1]    
    total = 0
    for i in range(len(r_binaries)):
        total += int(r_binaries[i]) * conversion[i]        
    return total

#print(BinToDec(101000111))

# 24. Input a decimal number and convert it to binary.
def DecToBin(num):
    # Handle the case of 0 explicitly
    if num == 0:
        return '0'
    
    binary_digits = []
    
    # Convert decimal to binary manually
    while num > 0:
        remainder = num % 2
        binary_digits.append(str(remainder))
        num = num // 2
    
    # The binary_digits list contains the binary digits in reverse order
    binary_digits.reverse()
    
    # Join the digits to form the final binary string
    binary_representation = ''.join(binary_digits)
    
    return binary_representation

#print(DecToBin(256))

# 25 Input a number and check if it’s an Armstrong number.
def IsArmstrongNumber(num):
    digits = []
    digits[:] = str(num)
    temp = 0
    for digit in digits:
        temp += int(digit) ** 3
    if temp == num:
        return True
    else:
        return False

# 26. Input a string and count the number of words.
def CountWords(sentence):
    words = []
    words = sentence.split(" ")
    return len(words)

#print(CountWords("The quick brown fox jumped over the lazy dog."))

# 27. Input two sorted lists and merge them into one sorted list.
def MergeLists(listOne, listTwo):
    mergedList = listOne + listTwo
    return(sorted(mergedList))

#print(MergeLists([2, 4, 1, 9, 12], [26, 3, 1, 6, 8]))


# 28. Input a list and find the second largest number.
def FindSecondLargest(listOne):
    sortedList = sorted(listOne)
    return sortedList[1]

#print(FindSecondLargest([1, 7, 9, 4, 25, 34, 12, 8, 3]))

# 29. Input a list and remove any duplicate values.
def RemoveDuplicates(listOne):    
    testSet = set(listOne)
    return testSet

#print(RemoveDuplicates([22, 21, 34, 22, 12, 12, 14, 53, 53]))
    
# 30. Input a list and check if it’s sorted in ascending order.
def ListIsSorted(listOne):
    if listOne == sorted(listOne):
        return "Sorted"
    else:
        return "Not Sorted"

#print(ListIsSorted(MergeLists([2, 4, 1, 9, 12], [26, 3, 1, 6, 8])))

# 31 Input a 2D matrix and print its transpose.
def TransposeMatrix(matrixOne):
    # Compute the transpose of the matrix
    transpose = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    return transpose

"""
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transposed = TransposeMatrix(matrix)

# Print the transposed matrix
for row in transposed:
    print(row)

"""

# 32. Input a list of numbers and print the sum.
def SumOfList(listOne):
    total = 0
    for num in listOne:
        total += num
    return total

# print(SumOfList([22, 21, 34, 22, 12, 12, 14, 53, 53]))

# 33. Input a list of numbers and sort them without using the sort() method.
def SortList(listOne):
     # Outer loop to iterate through the list n times
    for n in range(len(listOne) - 1, 0, -1):

        # Inner loop to compare adjacent elements
        for i in range(n):
            if listOne[i] > listOne[i + 1]:

                # Swap elements if they are in the wrong order
                swapped = True
                listOne[i], listOne[i + 1] = alistOner[i + 1], listOne[i]


# 33. 


    