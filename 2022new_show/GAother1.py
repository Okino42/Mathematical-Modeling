# ！/usr/bin/nev python
# -*-coding:utf8-*-
import numpy as np
import matplotlib.pyplot as plt

def initpop(popsize,binarylength):
	#生成popsize×binarylength的二维0、1序列
    pop = np.random.randint(0,2,(popsize,binarylength))
    return pop

def bintodec(ypop):
    pop=ypop.copy() #拷贝种群
    [row,col] = pop.shape #得到pop种群的行数、列数
    #将二进制数组中每一个位置的值转换位对应的十进制数
    for i in range(col):
        pop[:,i]=2**(col-1-i)*pop[:,i]
    #每一行求和
    pop = np.sum(pop,axis=1)
    num=[]
    #因为二进制串为10位，所以我们除以1023将其限制再0-1之间，然后再乘以10得到定义域内的随机数。
    num=pop*10/8
    return num

def cal_objval(pop):
    x = bintodec(pop)
    a0=0.3
    b0=0.3
    W=13.836
    a = a0 + (14 - W) / 600 - (1E-4) * (x ** 3 - 18.75 * x ** 2 + 75 * x)
    b = b0 + (14.5 - W) / 650 - 2 * (1E-4) * (x ** 3 - 15 * x ** 2 + 48 * x)
    objval = 0.5 * a + 0.5 * b
    # objval = 10*np.sin(5*x)+7*abs(x-5)+10
    return objval

def selection(pop,fitval,popsize):
    idx = np.random.choice(np.arange(popsize),size=popsize,replace=True,p=fitval/fitval.sum())
    return pop[idx]


def crossover(pop,pc):
    [px,py] = pop.shape
    newpop = np.ones((px,py))  #成同样规格的newpop数组来存储新种群
    for i in range(0,px,2):
        if np.random.rand()<pc:
            cpoint = int(np.random.rand()*py*10//10)
            newpop[i,0:cpoint]=pop[i,0:cpoint]
            newpop[i,cpoint:py]=pop[i+1,cpoint:py]
            newpop[i+1,0:cpoint]=pop[i+1,0:cpoint]
            newpop[i+1,cpoint:py]=pop[i,cpoint:py]
#               newpop[i+1,:]=[pop[i+1,0:cpoint],pop[i,cpoint:py]]
        else:
            newpop[i,:]=pop[i,:]
            newpop[i+1,:]=pop[i+1,:]
    return newpop


def mutation(pop,pm):
    [px,py] = pop.shape
    newpop = np.ones((px,py))
    for i in range(px):
        if(np.random.rand()<pm):
            mpoint = int(np.random.rand()*py*10//10)
            if mpoint<=0:
                mpoint=1
            newpop[i,:]=pop[i,:]
            if newpop[i,mpoint]==0:
                newpop[i,mpoint]=1
            else:
                newpop[i,mpoint]=0
        else:
            newpop[i,:]=pop[i,:]
    return newpop



def best(pop,fitvalue):
    [px,py]=pop.shape
    bestindividual = pop[0,:]
    bestfit = fitvalue[0]
    for i in range(1,px):
        if fitvalue[i]>bestfit:
            bestindividual = pop[i,:]
            bestfit = fitvalue[i]
    return bestindividual,bestfit


if __name__ == "__main__":
    popsize = 100  # 种群规模
    binarylength = 4  # 二进制编码长度（DNA）
    pc = 0.6  # 交叉概率
    pm = 0.001  # 变异概率
    pop = initpop(popsize, binarylength)  # 初始化种群

    # 进行计算,迭代一百次，每十次画一张图
    for i in range(100):
        # 计算当前种群适应度
        objval = cal_objval(pop)
        fitval = objval

        # 选择操作
        newpop = selection(pop, fitval, popsize)
        # 交叉操作
        newpop = crossover(newpop, pc);
        # 变异操作
        newpop = mutation(newpop, pm);
        # 更新种群
        pop = newpop;

        # 寻找最优解并绘图
        [bestindividual, bestfit] = best(pop, fitval)

        x1 = bintodec(newpop)
        y1 = cal_objval(newpop)
        x = np.arange(0, 8, 0.1)
        a0 = 0.3
        b0 = 0.3
        W = 13.836
        a = a0 + (14 - W) / 600 - (1E-4) * (x ** 3 - 18.75 * x ** 2 + 75 * x)
        b = b0 + (14.5 - W) / 650 - 2 * (1E-4) * (x ** 3 - 15 * x ** 2 + 48 * x)
        y = a+b

    [n] = bestindividual.shape
    x2 = 0
    for i in range(n):
        x2 += 2 ** (n - 1 - i) * bestindividual[i]
    print("The best X is ", x2 * 10 / 9)
    print("The best Y is ", bestfit)
