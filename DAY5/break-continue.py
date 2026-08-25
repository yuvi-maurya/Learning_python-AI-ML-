# Break and continue statements in Python are used to control the flow of loops.
# The break statement is used to exit a loop prematurely, while the continue statement
#  is used to skip the current iteration and move on to the next one.
  

print("======================")

i = 1
while i <= 5:
    print(i)
    if(i == 3):
        break
    i+=1

#program to demonstrate the use of continue statement


print("======================")


i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)


# ques- 1:
print("======================")

i = 0
while i <= 10:
    i+=1
    if(i % 2 == 0):
        continue
    print(i)
    
