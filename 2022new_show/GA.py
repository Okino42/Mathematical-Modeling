# ！/usr/bin/nev python
# -*-coding:utf8-*-
import math
import random
import copy
import matplotlib.pyplot as plt

num=10
W=[13.836,13.103,13.698,14.067,16.383,19.074,21.230,20.224,18.405,17.147,15.723,14.551]

child=[]
#初始化种群
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


#函数
def f(m):
    a0=0.3
    b0=0.3
    for i in range(12):
        a = a0 + (14 - W[i]) / 600 - (1E-4) * (m[i] ** 3 - 18.75 * m[i] ** 2 + 75 * m[i])
        b = b0 + (14.5 - W[i]) / 650 - 2*(1E-4) * (m[i] ** 3 - 15 * m[i] ** 2 + 48 * m[i])
        z=0.2*a+0.8*b
        a0 = a
        # print(a)
        b0 = b
        # print(b)
    print(a)
    print(b)
    return z

#适应度函数
def get_fitness():

    return 0


def cross():
    for i in range(num):
        m=child[i]
        # print(child[i])
        r=f(child[i])
        print(r)



if __name__=='__main__':
    child=start()
    print(child)


