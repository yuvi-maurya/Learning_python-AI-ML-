# # Function in python.

# # Block of statementbthat perform a specific task. 


# Function Definition 

      # The part  containing the exact set of instructions which are executed during the function call.


def greet():
    print("Namaste!")

# Function ko call karna
greet()
greet()
greet()



# 2. Parameters — Function ko Input dena

def greet(name):
    print("Namaste,", name)

greet("Yuvraj")
greet("Priya")

# Output:

# Namaste, Yuvraj
# Namaste, Priya

# Kya ho raha hai:

# name ek parameter hai — function ka "placeholder" jo call karte waqt actual value lega.
# Jab greet("Yuvraj") call kiya, "Yuvraj" argument ban ke name mein chala gaya.
# Isi wajah se function generic (reusable) ban gaya — same function, alag-alag input, alag output.

# Multiple parameters bhi le sakte ho:

# python
def add(a, b):
    print(a + b)

add(5, 3)   # Output: 8




def func_name(param1, param2):    # function Definition 
    # Some Work
    return

# func_name(age1, age2)       # function call    

def calcSum(a, b):
    sum = a + b
    print(sum)
    return sum


calcSum(5, 10)



def calc_sum(a, b):
    return a + b

sum = calc_sum(5, 8)
print(sum)



def calc_avg(a, b ,c):
    sum = a + b + c
    avg = sum / 3
    print(avg)
    

calc_avg(98 , 97 , 95)



# A function is a group of statement performing a specific tack .
# When a program gets bigger in size and its complexity grows it gets 
# difficult for a program to keep track on which piece if code is doing what !

# A function can be reused by the programmer in a given program any number of


# Function type in python 

   # There are two type of function in python:

# (1.) built-in functions ( Already present in python )

        #    print()
        #     len()
        #     type()
        #     range()  etc....

# User defined functions ( Defined by the user)




# DEFAULT PARAMETERS

    # Assigning a default value to parameter, which is used on argument is passed .


def cal_prod(a = 4, b = 5):
    print(a*b)
    return a*b

cal_prod()


def cal_prod(a, b = 5):
    print(a*b)
    return a*b

cal_prod(6)


          # error return karega 

  
# def cal_prod(a = 4, b):
#     print(a*b)
#     return a*b

# cal_prod(9)

# Not-default argument follows default argment pylance (parameter b : any)



# 3. Return Values — Function se Output wapas lena


def add(a, b):
    result = a + b
    return result

sum_value = add(5, 3)   # function ka result variable mein store ho gaya
print(sum_value)        # Output: 8
print(sum_value * 2)    # Output: 16 — ab is value ko aage use kar sakte ho!


# Farak samjho print vs return mein:

# print() wala function	                                   return wala function
# Sirf screen pe dikhata hai	                                 Value ko function ke bahar bhejta hai
# Us value ko aage use nahi kar sakte	                         Us value ko variable mein store karke aage use kar sakte ho
# Function khatam hone pe value "gayab" ho jaati hai	         Value "zinda" rehti hai, jab tak chaho use karo


def add_print(a, b):
    print(a + b)     # sirf print karta hai

def add_return(a, b):
    return a + b      # value wapas deta hai

x = add_print(5, 3)    # Output: 8 (print hua), lekin x = None
y = add_return(5, 3)   # Kuch print nahi hua, lekin y = 8

print(x)   # None
print(y)   # 8
