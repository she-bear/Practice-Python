# Factorial of a number using recursion

def recur_factorial(n):
   print(n)
   if n == 1:
       print("if", n)
       return n
   else:
       y = n-1
       z = recur_factorial(y)
       x = n*z
       print("else",n)
       return x

num = 7

# check if the number is negative
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   print("The factorial of", num, "is", recur_factorial(num))