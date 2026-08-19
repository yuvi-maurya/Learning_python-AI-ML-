# Type conversion in Python refers to the process of converting a variable from one data type to another. 
# Python provides several built-in functions for type conversion, such as int(), float(), str(), and bool().


# notes: 
# Implicit conversion → Python does it automatically, only between compatible numerictypes (int → float, bool → int).
# Explicit casting → You use functions like int(), float(), str(), list(), etc.
# and it works between more type combinations, but can raise errors (ValueError) or lose data if not done carefully.
# Python is strict about mixing incompatible types (like str + int) — it will not silently convert them, 
# unlike some looser languages, so you almost always need explicit casting when 
# working with user input (input() always returns a string).


#example of type conversion in Python:
a = 10
b = 3.14 
c = a + b  # Implicit conversion: int to float
print(c)  # Output: 13.14



# Implicit casting: int to float
x = 10
print(x)
print(type(x))

# convert x to float
y = float(x)
print(y)
print(type(y))

# convert x to string
z = str(x)
print(z)
print(type(z))

# convert string to integer
a = "20"
b = int(a)
print(b)
print(type(b))



# Type casting in Python is the process of converting a variable from one data type to another. 

#example of type casting in Python:
x = 10.5
print(x)
print(type(x))

# convert x to integer
y = int(x)
print(y)
print(type(y))  




