

#importing math module to access sqrt()
import math

#to test if a given number is a perfect square

def testIfPerfectSquare(a):
    b=int(math.sqrt(a))
    return (b*b)==a

def fibonacci(x):
    #f(n)=f(n-1)+f(n-2)
    f=5
    return testIfPerfectSquare(f*x*x+4) or testIfPerfectSquare(f*x*x-4)

i=int(input("Enter a number: ")) #get input from user
if (fibonacci(i)==True):
    print(str(i) +"  belong to a fiboacci")
else:
    print(str(i) + "  does not belong to fibonacci")