from math import *
import random

#22
c = 0
for i in range(100,200):
    if(i % 17 == 0):
        c += i
print(c)

#19
for i in range(35,88):
    if i % 7 == 1 or i % 7 == 2 or i % 7 == 5:
        print(i)


#20
sum = 0
for i in range(1,51):
    if i % 5 == 0 or i % 7 == 0:
        sum += i
print("summa = ", sum)

#15
for r in range(10):
    for c in range(-1,9):
        if r==c:
            print(r+1, end=" ")
        else:
            print(c+1, end=" ")
    print()

#1
j=0
for i in range(0,15,1): #for i in range(15)
    A=float(input(f"{i+1} Sisesta A : "))
    if int(A)==A:
        j+=1
print(j)

#10
text=""
for i in range(1,11):
    arv1=randint(-100,100)
    arv2=randint(-100,100)
    if arv1>arv2:
        print(f"{arv1} on suurem kui {arv2}")
        text+=" "+str(arv1)
    elif arv2>arv1:
        print(f"{arv2} on suurem kui {arv1}")
        text+=" "+str(arv2)
    else:
        print(f"{arv1},{arv2} on võrdsed")
print(text)

#12
N=int(input("Kogus: "))
m=int(input("Min: "))
m*=60
summa=0
for i in range(1,N):
    summa+=m
    m+=10
print(summa/60)

#16
for r in range(9):
    for c in range(9):
        if r==c:
            print(r+1, end=" ")
        else:
            print(0, end=" ")
    print()

