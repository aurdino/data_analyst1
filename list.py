# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 17:57:03 2024

@author: VishalRajak
"""


lst = [1,2,3,4,5,6,7]
print('reversed list: ', lst[::-1])
print('length:', len(lst))
lst.append(10)
print(lst)
lst.insert(0,-1)
print(lst)
lst1 = [10,20,30]
lst.extend(lst1)
print(lst)
print(lst.index(10), lst.count(10))
lst.remove(10)
print(lst, 'len:', len(lst))
lst.pop()
print(lst, 'sum : ', sum(lst)) #lst.clear() to empty the list, return empty list
print('sort: ', sorted(lst)) #sorted(lst)[::-1] --descending order
print('descending: ', sorted(lst)[::-1])


sq = [i*i for i in range(10)]
print('square:', sq)


def square(x):
    return x**2
sq1 = square(20);
print(sq1)

print(type(None))


def max_ele(ls):
    mx = -1
    for i in ls:
        if i > mx:
            mx = i
    return mx
test_max = max_ele([1,4,2,10,58])
print('max:', test_max)


def greet(name, age):
    return "Hello, {}! You are {} years old".format(name,age)
print(greet('Visha', 27))

def odd_even(num):
    
    return True if num%2 == 0 else False 


print(odd_even(10))


#tuple : are immutable ie they can't be modified
tup = (1,2,3,4,5,6)
print(tup[1])
tup += (7,8,9) #concatenate tuples
print(tup)



