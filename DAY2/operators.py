# Operators:
# An operator is a symbol that performs a specific operation on one or more operands (values or variables)
# in a programming language. Operators are used to manipulate data and perform various tasks, such as 
# arithmetic calculations, comparisons, logical operations, and more.

# In Python, operators can be categorized into several types:
# 1. Arithmetic Operators
# 2. Relational/Comparison Operators
# 3. Assignment Operators
# 4. Logical Operators
# 5. Bitwise Operators

# 1. Arithmetic Operators:
# These operators are used to perform basic mathematical operations.
#    ( + ) Addition: Adds two operands.
#    ( - ) Subtraction: Subtracts the second operand from the first.
#    ( * ) Multiplication: Multiplies two operands.
#    ( / ) Division: Divides the first operand by the second.
#    ( % ) Modulus: Returns the remainder of the division.
#    ( ** ) Exponentiation: Raises the first operand to the power of the second.
#    ( // ) Floor Division: Returns the quotient of the division, rounded down to the nearest integer.



#example of arithmetic operators in Python:
a = 10
b = 5
c = a + b  # Addition
d = a - b  # Subtraction
e = a * b  # Multiplication
f = a / b  # Division
g = a % b  # Modulus
h = a ** b # Exponentiation
i = a // b # Floor Division


# 2. Relational/Comparison Operators:
# These operators are used to compare two values and return a boolean result (True or False).
#    ( == ) Equal to: Returns True if both operands are equal.
#    ( != ) Not equal to: Returns True if both operands are not equal.
#    ( < ) Less than: Returns True if the first operand is less than the second.
#    ( > ) Greater than: Returns True if the first operand is greater than the second.
#    ( <= ) Less than or equal to: Returns True if the first operand is less than or equal to the second.
#    ( >= ) Greater than or equal to: Returns True if the first operand is greater than or equal to the second.

#example of relational/comparison operators in Python:
# x = 10
# y = 5
# z = x == y  # Equal to
# w = x != y  # Not equal to
# v = x < y   # Less than
# u = x > y   # Greater than
# t = x <= y  # Less than or equal to
# s = x >= y  # Greater than or equal to

# 3. Assignment Operators:
# These operators are used to assign values to variables.
#    ( = ) Assignment: Assigns the value of the right operand to the left operand.
#    ( += ) Addition Assignment: Adds the right operand to the left operand and assigns the result to the left operand.
#    ( -= ) Subtraction Assignment: Subtracts the right operand from the left operand and assigns the result to the left operand.
#    ( *= ) Multiplication Assignment: Multiplies the right operand with the left operand and assigns the result to the left operand.
#    ( /= ) Division Assignment: Divides the left operand by the right operand and assigns the result to the left operand.
#    ( %= ) Modulus Assignment: Returns the remainder of the division and assigns it to the left operand.
#    ( **= ) Exponentiation Assignment: Raises the left operand to the power of the right operand and assigns the result to the left operand.
#    ( //= ) Floor Division Assignment: Returns the quotient of the division, rounded down to the nearest integer, and assigns it to the left operand.


#example of assignment operators in Python:
a = 10
a += 5  # Equivalent to a = a + 5
a -= 3  # Equivalent to a = a - 3
a *= 2  # Equivalent to a = a * 2
a /= 4  # Equivalent to a = a / 4
a %= 3  # Equivalent to a = a % 3
a **= 2 # Equivalent to a = a ** 2
a //= 2 # Equivalent to a = a // 2

# 4. Logical Operators:
# These operators are used to combine conditional statements and return a boolean result.
#    ( and ) Logical AND: Returns True if both operands are True.
#    ( or ) Logical OR: Returns True if at least one of the operands is True.
#    ( not ) Logical NOT: Returns True if the operand is False, and vice versa.

#example of logical operators in Python:
x = True
y = False
z = x and y  # Logical AND
w = x or y   # Logical OR
v = not x    # Logical NOT

# 5. Bitwise Operators:
# These operators are used to perform operations on binary representations of integers.
#    ( & ) Bitwise AND: Returns 1 if both bits are 1, otherwise returns 0.
#    ( | ) Bitwise OR: Returns 1 if at least one of the bits is 1, otherwise returns 0.
#    ( ^ ) Bitwise XOR: Returns 1 if the bits are different, otherwise returns 0.
#    ( ~ ) Bitwise NOT: Returns the complement of the number.
#    ( << ) Left Shift: Shifts the bits of the number to the left by the specified number of positions.
#    ( >> ) Right Shift: Shifts the bits of the number to the right by the specified number of positions.

#example of bitwise operators in Python:
a = 5  # Binary: 0101
b = 3  # Binary: 0011
c = a & b  # Bitwise AND: 0001 (1)
d = a | b  # Bitwise OR: 0111 (7)
e = a ^ b  # Bitwise XOR: 0110 (6)
f = ~a     # Bitwise NOT: 1010 (10)
g = a << 1 # Left Shift: 1010 (10)
h = a >> 1 # Right Shift: 0010 (2)
