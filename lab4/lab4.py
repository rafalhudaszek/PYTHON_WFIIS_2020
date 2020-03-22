#!/usr/bin/env python3.7
import math
import sys
import random

#1
def fun1(a):
    s = {}
    size = random.randrange(0,20)
    i = 0
    b = 0.5
    while i < 20:
        key = random.random()
        if key in s:
            None
        else:
            s[key] = eval("round(a*key , 3) + b")
            i += 1
    return s

#2
def fun2(*val):
    lista = []
    for i in val[0]:
        for j in val[1:]:
            if i not in j:
                break
        else:
            lista.append(i)
    return lista
#print(fun2([5,12,42,11],(42,11,56,23)))

#3
def fun3(seq1,seq2,Flag=True):
    
    if Flag:        
        A=[(seq1[i],seq2[i]) for i in range(min( len(seq2),len(seq1) )) ]
    else:
        A=[(seq1[i],seq2[i]) if i<min( len(seq2),len(seq1) ) else None for i in range(max( len(seq2),len(seq1) )) ]
    return A

#4
def fun4(*a):
    return min(*a) 

def fun5(fun, *a):
    b = fun(*a) 
    print(b)

#fun5(fun4, [5,6,2,7])


#5
def fun6(amount, values = (10,5,2)):
    i = amount
    stop = 0
    step = 0
    while i > 0 and stop < 100:
        if i >= values[step]:
            L = int(i / values[step])
            i = i - values[step] * L
        step += 1
        stop += 1

#fun6(147,(10,2,1))

#6
def fun7(searched, rangeA, rangeB, tactic = 'r'):
    steps = 0
    rand = 0
    if tactic == 'r':
        while rand != searched:
            rand = random.randrange(rangeA, rangeB)
            rangeA, rangeB = (rangeA, rand)  if rand > searched else (rand, rangeB)
            steps +=1
    else:    
        None
    print("Ilosc krokow %d, wartosc = %d",steps, rand)

fun7(57, 20, 100)
