#conditional statements in Python
x = 10
y = 5

if x > y:
    print("x is greater than y")
elif x < y:
    print("x is less than y")
else:
    print("x is equal to y")


# if - elif - else statements are used to execute different blocks of code based on certain conditions.

#if( Condition1):
    # block of code to be executed if Condition1 is true
#elif( Condition2):
    # block of code to be executed if Condition2 is true
#else:
    # block of code to be executed if both Condition1 and Condition2 are false

    #program-1.

age = 18

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")


    #program-2.

Light = "Green"

if(Light == "Green"):
    print("Go")
elif(Light == "Yellow"):
    print("Slow Down")  
elif(Light == "Red"):
    print("Stop")


        #program-3.

age = int (input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")


    #program-4.

    #GRADE STUDENT BASED ON MARKS

    #Question-1?

    #marks >=90 , grade = "A"  90 > marks >= 80 , grade = "B"  80 > marks >= 70 ,
    #grade = "C"  70 > marks >= 60 , grade = "D"  marks < 60 , grade = "F"

marks = float(input("Enter your marks: "))
if marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C"
elif marks >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Your grade is: {grade}")

#ques-2.   WAp to chech if a number entered by the user is odd or even.


number = int(input("Enter a number: "))
if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")



#Ques-3.  Wao to find the largest of three numbers entered by the user.



a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
c = float(input("Enter the third number: "))

if a >= b and a >= c:
    largest = a
elif  b >= c:
    largest = b
else:
    largest = c

print(f"The largest number is: {largest}")

#Ques-4.  Wap to check if a number is a multiple of 7 or not.



number = int(input("Enter a number: "))
if number % 7 == 0:
    print("The number is a multiple of 7.")
else:
    print("The number is not a multiple of 7.")
