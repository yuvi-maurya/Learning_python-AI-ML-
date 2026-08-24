# For Loop in Python

# For loop is used to iterate over a sequence (like a list, tuple, dictionary, set, or string).

# Example 1: Iterating through a list
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

# Example 2: Iterating through a list

list = [1, 2, 3, 4, 5]
for number in list:
    print(number)


# For loop with else statement

for fruit in fruits:
    print(fruit)
else:
    print("All fruits have been printed.")


# Example 3: Iterating through a string

string = "Hello"
for char in string:
    print(char)


# Example 4: iterating through a tuple
tuple = (1, 2, 3, 4, 5)
for number in tuple:
    print(number)


# Question-1: print the element of the list using for loop.
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
for element in list:
    print(element)


# Question-2: Search for a specific element in the tuple using for loop.
tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)
target = 16
for element in tuple:
    if element == target:
        print(f"Element {target} found.")
        break
else:
    print(f"Element {target} not found.")

# Question-3: Print the element of the tuple using for loop.
tuple = (1, 2, 3, 4, 5)
for number in tuple:
    print(number)