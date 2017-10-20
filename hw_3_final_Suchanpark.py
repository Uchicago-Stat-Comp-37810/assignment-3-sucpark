# Name: Suchan Park
# hw3.py
# Due : 10/20/2017

from math import sin  #import sin,cos,pi,ceil,log from module math
from math import cos
from math import pi
from math import ceil
from math import log
import random  #import module random


##### Template for Homework 3, exercises 1 -  ######


# ********** Exercise 1 ********** 

# Define is_divisible function here
def is_divisible(num1, num2):   #Take two integers
    if (num2==0):
        print("Divisor cannot be zero")  # Divisor cannot be zero.
    elif (num1 % num2 == 0):  #If num1 is divisible by num2, the remainder will be zero
        return True
    else:
        return False

# Test cases for is_divisible
## Provided for you... uncomment when you're done defining your function

print ("10 is divisible by 5 : ", is_divisible(10, 5))  # This should return True
print ("18 is divisible by 7 : ",is_divisible(18, 7))  # This should return False
print ("42 is divisible by 0 : ",is_divisible(42, 0))  # What should this return? : Error happens. Exception handling is required.

# ********** Exercise 2 ********** 

# Define not_equal function here
def is_notoperator(num1,num2):   #Take two numbers
    if (num1 == num2):   #If two numbers are equal to each other, than the operator will be fail. So return False.
        return False
    else:
        return True


# Test cases for not_equal
print("3 is not equal to 4 :", is_notoperator(3,4)) #New function
print("3 is not equal to 4 :", 3 != 4) #Original operator

# ********** Exercise 3 ********** 

## 1 - multadd function
def multadd(a,b,c):
    sol=a+b*c
    return sol


## 2 - Equations

angle_test = multadd(sin(pi/4),cos(pi/4),1/2) #parameters are sin(pi/4), cos(pi/4) and 1/2
print("sin(pi/4) + cos(pi/4)/2 is:")
print(angle_test)

ceiling_test=multadd(ceil(276/19),log(12,7),2) #parameters are ceil(276/19). log_7(12) and 2
print("ceiling(276/19) + 2 log_7(12) is:")
print(ceiling_test)

# Test Cases
# angle_test =
# print "sin(pi/4) + cos(pi/4)/2 is:"
# print angle_test

# ceiling_test =
# print "ceiling(276/19) + 2 log_7(12) is:"
# print ceiling_test


# ********** Exercise 4 **********

## 1 - rand_divis_3 function
def rand_divis_3():  #Takes no parameter
    a=random.randint(0,100)  #Generates a random number, 0 is minimum and 100 is maximum
    if(a%3 == 0):   #True Condition : the remainder of a by 3 is equal to zero.
        print("The number is ", a) #Print the random number
        return True
    else:
        print("The number is ", a)
        return False

# Test Cases
print("The number is divisible by 3 : ", rand_divis_3())

