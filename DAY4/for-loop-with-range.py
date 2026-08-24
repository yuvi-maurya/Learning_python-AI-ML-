# Range function in Python

# The range() function generates a sequence of numbers.
# It is commonly used with for loops to specify the number of iterations.

# We can use the range() function in three different ways:

# Example 1: Using range() with a single argument

# range( start?, stop, step) - generates a sequence of numbers from start (inclusive) 
# to stop (exclusive) with a step value.

print("Using range() with a single argument:")

for i in range(5):
    print(i)

# Example 2: Using range() with two arguments (start and stop)

print("Using range() with two arguments:")

for i in range(2, 8):
    print(i)

# Example 3: Using range() with three arguments (start, stop, and step)

print("Using range() with three arguments:")

for i in range(1, 10, 2):
    print(i)

# We can also specify the start, stop, and step values in the range() function.



#let's see some examples of using the range() function in different ways:


#Question-1: Print the numbers from 1 to 10 using range() function.

print("Numbers from 1 to 10:")

for i in range(1, 11):
    print(i)

#Question-2: Print the even numbers from 1 to 20 using range() function.
print("Even numbers from 1 to 20:")

for i in range(2, 21, 2):
    print(i)


#Question-3: Print the odd numbers from 1 to 20 using range() function.
print("Odd numbers from 1 to 20:")

for i in range(1, 21, 2):
    print(i)


#Question-4: Print the numbers from 10 to 1 in reverse order using range() function.
print("Numbers from 10 to 1 in reverse order:")
for i in range(10, 0, -1):
    print(i)


#Question-5: Print the multiplication table of a given number using range() function.
number = int(input("Enter a number to print its multiplication table: "))
print(f"Multiplication table of {number}:")
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")


# Wap to print the sum of first n natural numbers using range() function.
n = int(input("Enter a number: "))
sum = 0
for i in range(1, n + 1):
    sum += i
print(f"The sum of first {n} natural numbers is: {sum}")

    #for while loop 


n = int(input("Enter a number: "))
sum = 0
i = 1
while i <= n:
    sum += i
    i += 1
print(f"The sum of first {n} natural numbers is: {sum}")



# Wap to find the factorial of a given number using range() function.
number = int(input("Enter a number to find its factorial: "))
factorial = 1
for i in range(1, number + 1):
    factorial *= i
print(f"The factorial of {number} is: {factorial}")
