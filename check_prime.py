# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 15:38:35 2024

@author: VishalRajak
"""

def check_prime(num):
    if num < 2:
        return '{} is not a prime number'.format(num)
    if num == 2:
        return '{} is a prime number'.format(num)
    p = 3 
    for p in range(2,int(num/2)+1):
        if num%p == 0:
            return '{} is not a prime number'.format(num)
        else:
            '{} is a prime number number'.format(num)
            
    return '{} is a prime number number'.format(num)

t = int(input('enter number of test cases'))
while t > 0 :
    n = int(input('enter a number '))
    res = check_prime(n)
    print(res)
    t = t-1
    
    