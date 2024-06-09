#1) Write the code to list the numbers which can be fully divided by 2, 3 and 7
# from 10 to 50.

numbers = []

for i in range(10, 51):
    if i%2 == 0 and i%3 == 0 and i%7 == 0:
        numbers.append(i)

print(numbers)
