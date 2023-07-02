# ！/usr/bin/nev python
# -*-coding:utf8-*-
import math
import random
import copy
import matplotlib.pyplot as plt
num=10
child=[]
# W=[13.83632,13.10326,13.69784,14.06674,16.38327,19.07445,21.23016,20.22245,18.40512,17.14743,15.72301,14.55143]
W=[14.0294197,13.30441989,	13.39141789	,14.7241447	,16.55114841,	19.3025191	,21.01966206	,19.28772575,	18.42802453,	17.22567502	,15.66639661,	14.59944635
]
def start():
    for k in range(num):
        x = []
        for i in range(12):
            rd=random.uniform(0,8)
            rd1=round(rd,1)
            x.append(rd1)
        child.append(x)
        # print(child)
    return child

def f(x):
    a0 = 0.3
    b0 = 0.3
    c = 0
    for i in range(12):
        a = a0 + (14 - W[i]) / 600 - (1E-4) * (x[i] ** 3 - 18.75 * x[i] ** 2 + 75 * x[i])
        b = b0 + (14.5 - W[i]) / 650 - 2*(1E-4) * (x[i] ** 3 - 15 * x[i] ** 2 + 48 * x[i])
        z=0.5*a+0.5*b
        a0 = a
        b0 = b
        c=c+x[i]
    print('a=',a)
    print('b=',b)
    print('c=',c)
    print('a+b=',a+b)
    return z

if __name__=='__main__':
    # x_data=[3.3,3,4,3.4,3.4,3.5,3.5,3.6,3.6,3.6,3.6,3.6,3.6]
    x_data=[3.52,3.52,3.52,3.52,3.52,3.52,3.52,3.52,3.52,3.52,3.52,3.52]
    f(x_data)

