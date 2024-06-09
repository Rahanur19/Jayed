# 2）Write a function to calculate the factorial of one positive number.

def factorial(number):
    factorial = 1
    for i in range(1,number+1):
        factorial = factorial * i

    return factorial

num = 4
print(f"The factorial of {num} is : {factorial(num)}")
