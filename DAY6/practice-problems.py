# # Question: Do numbers input lo aur unka sum, difference, product, division print karo.

# num1 = int(input("Enter your number:"))
# num2 = int(input("Enter your number:"))

# sum = num1 + num2

# diff = num1 - num2

# product_result = num1 * num2

# if num2 != 0:
#     division_result = num1 / num2
# else:
#     print("Division by zero not possible")


# print(sum)
# print(diff)
# print(product_result)
# print(division_result)


# #Question: Ek number ka square aur cube nikalo.

# num1 = int(input("Enter your number:"))

# square = num1 ** 2

# cube = num1 ** 3

# print(square)
# print(cube)

# # Question: Temperature ko Celsius se Fahrenheit mein convert karo.

# Celsius = int(input("Enter temperature in Celsius:"))

# fahrenheit = (Celsius * 9/5) + 32

# print(fahrenheit)


# # Question: Simple interest calculate karo (P, R, T input lekar).

# P = float(input("Principal amount enter karo: "))
# R = float(input("Rate of interest (%) enter karo: "))
# T = float(input("Time (years) enter karo: "))

# SI = (P * R * T) / 100

# print(f"Simple interest: {SI}")

# # Question: Ek rectangle ka area aur perimeter nikalo (length, breadth input).


# length = float(input("Enter rectangle length:"))
# breadth = float(input("Enter rectangle breadth:"))

# area = length * breadth

# perimeter = 2 * ( length + breadth)

# print(f"Area of a rectangle: {area}")

# print(f"Perimeter of a Rectabgle: {perimeter}")



# # Question: Do numbers swap karo (bina third variable use kiye).

# a = 5 
# b = 7

# print(f"Print number A: {a}")
# print(f"Print number B: {b}")


# # tarika 1

# a = a + b 

# b = a - b
# a = a - b

# print(f"Print number A: {a}")
# print(f"Print number B: {b}")



# #   tarika 2


# a , b = b , a

# print(f"Print number A: {a}")
# print(f"Print number B: {b}")


# # Question: 

# # Ek number ki last digit nikalo.

# num = int(input("Enter your number:"))

# last_digit = num % 10

# print("Last digit hai:", last_digit)




# # Question: Circle ka area nikalo (radius input, π = 3.14159).



# redius = float(input("Enter Redius:"))

# area = (3.14159) * redius ** 2

# print(f"Area of Circle: {area}")


# # Question 9. Number even hai ya odd, check karo.

# num = int(input("Enter your number:"))

# if num % 2 == 0:
#     print(f"Number {num} is even")
# else:
#     print(f"Number {num} is odd")


# # Question 10. Teen numbers mein sabse bada number find karo.


# num1 = int(input("Enter your number1:"))
# num2 = int(input("Enter your number2:"))
# num3 = int(input("Enter your number3:"))

# if num1 > num2 or num1 > num3:
#     print(f"num1: {num1} is largest number")
# elif num2 > num3:
#     print(f"num2: {num2} is largest number")
# else:
#     print(f"num3: {num3} is largest number")




# # Question 11. Ek number positive, negative ya zero hai, check karo.

# num = int(input("Enter your number:"))

# if num > 0:
#     print(f"{num} is positive number")
# elif num < 0:
#     print(f"{num} is negative number")
# else:
#     print(f"Number is zero")


# # Question 12. Student ke marks input lo aur grade decide karo (A/B/C/F).
# # out of 100

# num = int(input("Enter your number:"))

# if num >= 90:
#     grade = "A"
# elif 90 > num >= 80:
#     grade = "B"
# elif 80 > num >=70:
#     grade = "C"
# else:
#     grade = "F"

# print(f" Grade: {grade}")



# # Question 13. Year leap year hai ya nahi, check karo.

# year = int(input("Year enter karo: "))

# # Leap year check karna
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print(year, "leap year hai")
# else:
#     print(year, "leap year nahi hai")


# # Question 14. Ek number vowel hai ya consonant (character input lekar).

# ch = input("Ek character enter karo: ")

# # Lowercase mein convert kar diya taaki 'A' aur 'a' dono handle ho jaayein
# ch = ch.lower()

# if ch in ['a', 'e', 'i', 'o', 'u']:
#     print(ch, "ek vowel hai")
# else:
#     print(ch, "ek consonant hai")



# # Question 15. Simple calculator banao (+, -, *, / — operator input lekar if-elif se).

# num1 = float(input("Pehla number enter karo: "))
# num2 = float(input("Dusra number enter karo: "))
# op = input("Operator enter karo (+, -, *, /): ")

# if op == '+':
#     result = num1 + num2
# elif op == '-':
#     result = num1 - num2
# elif op == '*':
#     result = num1 * num2
# elif op == '/':
#     if num2 != 0:
#         result = num1 / num2
#     else:
#         result = "Error: Division by zero"
# else:
#     result = "Invalid operator"

# print("Result:", result)

# # Question 16. Triangle valid hai ya nahi, check karo (3 sides input, triangle inequality).


# a = float(input("Side A enter karo: "))
# b = float(input("Side B enter karo: "))
# c = float(input("Side C enter karo: "))

# if (a + b > c) and (b + c > a) and (a + c > b):
#     print("Yeh triangle valid hai")
# else:
#     print("Yeh triangle valid nahi hai")


# # Loops — Basic (17-22)


# # Question 17. 1 se 10 tak table print karo (kisi bhi number ka).
# num = int(input("enter any number:"))
# for i in range(1, 11):
#     tabel = (f"{num} X {i} = {num * i}")
#     print(tabel)


# # Question 18. 1 se N tak sabhi numbers ka sum nikalo.

# num = int(input ("Enter your number"))
# sum = 0
# for i in range(1, num + 1):
#     sum += i
# print(sum)


# # Question 19. Ek number ka factorial nikalo.

# num = int(input ("Enter your number"))
# factorial = 1
# for i in range(1, num + 1):
#     factorial*= i
# print(factorial)


# # Question 20. N tak ke sabhi even numbers print karo.

# num = int(input ("Enter your number"))

# for i in range(1, num + 1):
#     if i % 2 == 0:
#         print(i)


#         #OR

# for i in range(2, num +1, 2):
#     print(i)


# # Question 21. Fibonacci series print karo (N terms tak).

# # N terms input lena
# n = int(input("Kitne terms chahiye: "))

# # Pehle 2 numbers
# first = 0
# second = 1

# print("Fibonacci Series:")

# if n <= 0:
#     print("Please enter a positive number")
# elif n == 1:
#     print(first)
# else:
#     print(first, second, end=" ")
#     for i in range(2, n):
#         next_num = first + second
#         print(next_num, end=" ")
#         first = second
#         second = next_num



# # Question 22. Number palindrome hai ya nahi, check karo (e.g. 121).


# num = int(input("Enter your number"))
# original = num
# new_num = 0
# while num > 0:
#     last_digit = num % 10
#     new_num = new_num * 10 + last_digit
#     num //= 10

# if original == new_num:
#     print(f"{new_num} is palindrome")
# else:
#     print(f"{new_num} is not palindrome")




# # Question 23. Classic FizzBuzz: 1-100 tak, 3 ke multiple pe "Fizz", 5 ke multiple pe "Buzz", dono pe "FizzBuzz".


# for i in range(1, 101):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz", end=" ")
#     elif i % 3 == 0:
#         print("Fizz", end=" ")
#     elif i % 5 == 0:
#         print("Buzz", end=" ")
#     else:
#         print(i, end=" ")


# # Question 24. FizzBuzz variant: 3 ke multiple pe "Fizz", 7 ke multiple pe "Buzz" (different numbers try karo).


# for i in range(1, 101):
#     if i % 3 == 0 and i % 7 == 0:
#         print("FizzBuzz", end=" ")
#     elif i % 3 == 0:
#         print("Fizz", end=" ")
#     elif i % 7 == 0:
#         print("Buzz", end=" ")
#     else:
#         print(i, end=" ")




# Question 25. 1-50 tak print karo, lekin prime numbers ke aage "Prime" likho.


for num in range(1, 51):
    is_prime = True

    if num < 2:
        is_prime = False

    else:
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break 
    if is_prime:
        print(num, "- Prime")
    else:
        print(num)        
