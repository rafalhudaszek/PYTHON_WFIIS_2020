#!/usr/bin/env python3.7
import math
import sys
import random

#1
def ifPalindrome(a):
    a_string = str(a)
    if a_string == a_string[::-1]:
        return True
    else:
        return False

#2
def ifFirst(a):
    if a == 2:
        return True
    if a % 2 == 0 or a <= 1:
        return False
    
    iter = int(a**0.5)
    for sep in range (3, iter, 2):
        if  a % sep == 0:
            return False 
    return True

#3

def createPalindromeDictionar(dictionaryLenght, rangeA, rangeB):
    s = {}
    i = 0
    while(i < dictionaryLenght):
        k = random.randint(100,10000)
        if k in s:
            None
        else:
            s[k] = ifPalindrome(k)
            i += 1
    return s

#4
lista = []
for i in range(100):
    lista.append(random.randint(0,19))

s1 = {}
s2 = {}
for i in range(20):
    if i % 2:
        s1.setdefault(i, [x for x, y in list(enumerate(lista)) if y == i ])
    else:
        s2.setdefault(i, [x for x, y in list(enumerate(lista)) if y == i ])

s3 = {}
listaList = []
for i in range(10):
    listaList.append([x for x in list(s1.values())[i]if not x % 3])


#5

lista = []
for i in range(100):
    lista.append(random.randint(0,10))

s2 = {}
for it in lista:
    s2.setdefault(it, []).append(lista.index(it, s2[it][-1] + 1 if s2[it] else 0))
