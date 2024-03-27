# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 21:36:20 2024

@author: VishalRajak
"""

#check a given number is prime or not 
def is_prime(num):
    if num <= 1:
        return False
    
    
    for i in range(2,(num//2)+1):
        if num%i == 0:
            return False
    return True


#count prime numbers till a given number

def count_prime(num):
    prime = [True for i in range(num+1)] 
    p = 2 
    while p*p <= num:
        if prime[p] == True:
            for i in range(p*p,num+1,p):
                prime[i] = False
        p = p+1
    cnt = 0 
    for i in range(2,num+1):
        if prime[i]:
            print(i, ' ')
            cnt += 1 
    print('total prime till ', num, 'is : ',cnt)


#remove duplicates from a list
def remove_duplicates(input_list):
    # Your code here
   uniq = []
   [uniq.append(i) for i in input_list if i not in uniq]
   return uniq

def find_common_elements(list1, list2):
    # Your code here
    
    l1,l2 = len(list1),len(list2)
    if l1 == 0 or l2 == 0:
        return []
    ls1 = set(list1)
    ls2 = set(list2)
    lst = ls1.intersection(ls2)
    return list(lst)

def find_missing_number(nums):
    # Your code here
    ln = len(nums)
    if ln == 0:
        return 0
    sm = sum(nums)
    cal = ln*(ln+1)//2 
    return (cal-sm)

def count_occurrences(numbers, target):
    cnt = numbers.count(target)
    return cnt

def count_primes(num):
    if num <= 1:
        return 0
    prime = [True for i in range(num+1)] 
    p = 2 
    while p*p <= num:
        if prime[p] == True:
            for i in range(p*p,num+1,p):
                prime[i] = False
        p = p+1
    cnt = 0 
    for i in range(2,num):
        if prime[i]:
            cnt += 1 
    return cnt 

def count_word_occurrences(text, word):
    # Your code here
    
    return word.lower().count(text.lower())

print(count_word_occurrences('python','Python is a versatile programming language.'))


t = int(input('enter test number of cases'))
while t > 0:
    n = int(input('enter a number'))
    check_prime = is_prime(n)
    if(check_prime) :
        print(n, 'is a prime number\n')
    else:
        print(n, 'is not a prime number\n')
    count_prime(n)
    t = t-1 
    