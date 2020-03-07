#!/usr/bin/env python3.7
import math
import sys

#split przyjmuje argument przez ktory dzielimy
#join 
#chmod +x by wykorzystac pierwsza linijke, wywolanie ./nazwa_pliku
#interpreter uruchamiamy python3, funkcje stringa dir('')
#lista skladana

#1
if len(sys.argv) < 2:
    print("Niewlasciwe uruchomienie programu")
else:
    wywolanie = ''.join(sys.argv[1:])

#2
small = [x for x in wywolanie if x.islower()]
big = [x for x in wywolanie if x.isupper()]
cyfry= [float(x) for x in wywolanie if x.isnumeric()]
reszta = [x for x in wywolanie if not x.isalnum()] 
 
print(small)
print(big)
print(cyfry)
print(reszta)

#3
repate = []
for x in small:    
    if x not in repate:
        repate.append(x)

lista = [(x, small.count(x)) for x in repate]   
print(lista)

#4
lista.sort(key = lambda x : x[1])
print(lista)

#5
samogloski = ('a','e','i','o','u','y', 'A', 'E', 'I', 'O', 'U','Y')

a = sum(wywolanie.count(x) for x in samogloski)
b = len(wywolanie) - a
krotka = [(x, a*x+b) for x in cyfry]
print(krotka) 

#6
xsrednie = sum(cyfry) / len(cyfry)
ysrednie = sum([b for a, b in krotka]) / len(krotka)

D = sum([((x-xsrednie) ** 2) for x in cyfry])
a = (1/D)*sum([(y * (x - xsrednie)) for x, y in krotka]) 
b = ysrednie - a*xsrednie 
print(a, b)
