from random import randint
def has_33(nums):
    for i in range(len(nums)-1):
        if nums[i]==3 and nums[i+1]==3:
            return True
    return False
a=input()
lst = [randint(1, 3) for i in range(5)]
print(lst)
print(has_33(lst))
num= [int(x) for x in a.split()]
print(has_33(num))