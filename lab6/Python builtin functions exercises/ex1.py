from functools import reduce
from operator import mul
import time
import math
#1
def multiply_list(num):
    return(reduce(mul,num))
numbers = [1, 2, 3, 4, 5]
print(multiply_list(numbers))

#2
def calculate_letters(s):
    upper=sum(1 for char in s if char.isupper())
    lower=sum(1 for char in s if char.islower())
    return upper, lower
upper,lower=calculate_letters("HellO")
print(f"Upper: {upper}, lower:{lower}")
#3  
def is_palindrome(str):
    reverse="".join(reversed(str))
    if reverse==str:
        return "Is Palindrome"
    else:
        return "Is not Palindrome"
print(is_palindrome("hakervrekah"))
#4
def delayed_sqrt(n, delay_ms):
    time.sleep(delay_ms / 1000)
    return math.sqrt(n)
n=25100
delay_ms=2123
result=delayed_sqrt(n,delay_ms)
print(f"Square root of {n} after {delay_ms} miliseconds is {result}")
#5

def all_true(elements):
    return all(elements)
print(all_true((True, True, True)))
print(all_true((True, False, True)))