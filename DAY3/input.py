# input() function is used to take input from the user.
name = input("Enter your name: ")
print(f"Hello, {name}!")

# input() function always returns a string, so if you want to take numerical input, you need to convert it to
#  the appropriate data type using type conversion functions like int() or float().

# Question-1: Take two numbers as input from the user and print their sum.
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
sum = num1 + num2
print(f"The sum of {num1} and {num2} is: {sum}")


# Question-2: Wap to input side of a square and print its area and perimeter.
side = float(input("Enter the side of the square: "))
area = side ** 2
perimeter = 4 * side
print(f"The area of the square is: {area}")
print(f"The perimeter of the square is: {perimeter}")

# Question-3: Wap to input radius of a circle and print its area and circumference.
import math
radius = float(input("Enter the radius of the circle: "))
area = math.pi * radius ** 2
circumference = 2 * math.pi * radius
print(f"The area of the circle is: {area}")
print(f"The circumference of the circle is: {circumference}")

# Question-4: Wap to input temperature in Celsius and convert it to Fahrenheit.
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"The temperature in Fahrenheit is: {fahrenheit}")

# Question-5: Wap to input 2 floting point number and print their average.
num1 = float(input("Enter the first floating point number: "))
num2 = float(input("Enter the second floating point number: "))
average = (num1 + num2) / 2
print(f"The average of {num1} and {num2} is: {average}")

# Question-6: Wap to input 3 numbers and print their product.
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
product = num1 * num2 * num3
print(f"The product of {num1}, {num2}, and {num3} is: {product}")