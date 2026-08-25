# While loop in python.

# Loop through a block of code as long as a condition is true.

# Loop are used when you want to repeat a block of code multiple times.


# While loop syntax:

# while condition:
    # block of code



i = 0
while i < 5:
    print(i)
    i += 1

# Question- 1: Print the numbers from 1 to 10 using while loop.

i = 1
while i <= 10:
    print(i)
    i += 1

# Question- 2: print the reverse numbers from 10 to 1 using while loop.
i = 10
while i >= 1:
    print(i)
    i -= 1

# Question- 3: Print the even numbers from 1 to 20 using while loop.
i = 1
while i <= 20:
    if i % 2 == 0:
        print(i)
    i += 1

# Question- 4: Print the odd numbers from 1 to 20 using while loop.
i = 1
while i <= 20:
    if i % 2 != 0:
        print(i)
    i += 1

# Question- 5: print the multiples of 5 from 1 to 50 using while loop.
i = 1
while i <= 50:
    if i % 5 == 0:
        print(i)
    i += 1


# Question- 6: Print the squares of numbers from 1 to 10 using while loop.
i = 1
while i <= 10:
    print(i ** 2)
    i += 1


# Question- 7: Print the multiples toble of a number using while loop.

number = int(input("Enter a number: "))
i = 1
while i <= 10:
    print(number * i)
    i += 1


# Question- 8: Print the element of the list using while loop.
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
i = 0
while i < len(list):
    print(list[i])
    i += 1


# Question- 9: Search for a specific element in the list using while loop.
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 11
i = 0
found = False
while i < len(list):
    if list[i] == target:
        print(f"Element found at index {i}")
        found = True
        break
    i += 1
if not found:
    print("Element not found")


# Question- 10:  print the elements of the following list using while loop.
list = ["apple", "banana", "cherry", "date", "elderberry"]

i = 0
while i < len(list):
    print(list[i])
    i += 1


# Question- 10:  print the elements of the following list using while loop.

list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

i = 0
while i < len(list):
    print(list[i])
    i += 1


    #OR



i = 1
while i <= 10:
    print(i ** 2)
    i += 1  