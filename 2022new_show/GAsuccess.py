import numpy as np

# pop, 即种群, 是一个二维数组(type为ndarray)
# DNA长度, pop的行, pop的一列就是一条DNA
DNA_size = 30
# 种群数量, pop的列
pop_size = 100
# 交叉率, 一般位于 0.4~0.99之间, 太小会导致效率低下, 太大可能会破坏种群的优良性
crossover_rate = 0.9
# 变异率, 一般位于 1/DNA长度 与 1/种群数量 之间, 这里采用权重的方式, 且以DNA长度为主要影响因素, 取值平均位于0.01%~10%
mutation_tate = 1/DNA_size*0.7+1/pop_size*0.3
# 种群代数, 也就是需要循环的次数
n_generations = 50
# 函数的定义域
x_bound = [2,3.52]
# W=[13.836,13.103,13.698,14.067,16.383,19.074,21.230,20.224,18.405,17.147,15.723,14.551]
W=[14.0294197,13.30441989,	13.39141789	,14.7241447	,16.55114841,	19.3025191	,21.01966206	,19.28772575,	18.42802453,	17.22567502	,15.66639661,	14.59944635]

# 目标函数
def f(x):
    a0 = 0.3
    b0 = 0.3
    for i in range(12):
        a = a0 + (14 - W[i]) / 600 - (1E-4) * (x ** 3 - 18.75 * x ** 2 + 75 * x)
        b = b0 + (14.5 - W[i]) / 650 - 2 * (1E-4) * (x ** 3 - 15 * x ** 2 + 48 * x)
        z = 0.5 * a + 0.5 * b
        a0 = a
        # print('a=',a)
        b0 = b
        # print('b=',b)
    print('a=', a)
    print('b=', b)
    print('a+b',a+b)
    return z

# 翻译, 将二进制的DNA翻译成指定区间的实数, 但当DNA_size较大时, 2 ** np.arange(DNA_size)[::-1]中较大的数会变为0, 导致不能正确翻译, 原因不明
# def translateDNA(pop):
#     x = (2 ** np.arange(DNA_size)[::-1]).dot(pop)/float(2 ** DNA_size - 1) * (x_bound[1] - x_bound[0]) + x_bound[0]
#     return x
# [[1,1,0,1]
#  [1,0,1,0]
#  [1,1,0,0]]
# 另一种翻译方案
def translateDNA(pop):
    x=[]
    for i in range(pop_size):
        a = ""
        for j in range(DNA_size):
            a = a + str(pop[:,i][j])
        x.append(int(a,2) / float(2 ** DNA_size - 1) * (x_bound[1] - x_bound[0]) + x_bound[0])
    # 将list转为ndarray, 这样方便广播
    x = np.array(x)
    return x

# 适应度函数
def get_fitness(pop):
    x = translateDNA(pop)
    y = f(x)
    return (y - np.min(y)) + 1e-3

# 轮盘赌选择
def select(pop, fitness):
    idx = np.random.choice(np.arange(pop_size), size=pop_size, replace=True, p=(fitness) / (fitness.sum()))
    return pop[:,idx]

# 交叉和变异
def crossover_and_mutation(pop, crossover_rate = 0.8):
    new_pop = pop
    for i in range(pop_size):
        child = pop[:,i]
        if np.random.rand() < crossover_rate:
            father = pop[:,np.random.randint(pop_size)]
            cross_points = np.random.randint(0, DNA_size)
            child[cross_points:] = father[cross_points:]
        mutation(child,mutation_tate)
        new_pop[:,i] = child
    return new_pop

def mutation(child, mutation_tate):
    if np.random.rand() < mutation_tate:
        mutate_point = np.random.randint(0, DNA_size)
        child[mutate_point] = child[mutate_point] ^ 1


pop = np.random.randint(2, size=(DNA_size, pop_size))

# 计算适应度->选择->交叉变异, 另一种方案是交叉变异->计算适应度->选择, 两者结果不会有太大差别
for k in range(n_generations):
    fitness = get_fitness(pop)
    pop = select(pop, fitness)
    pop = crossover_and_mutation(pop, crossover_rate)

x = translateDNA(pop)
y = f(x)
x0 = x[np.argmax(y)] # np.argmax(y), 是数组y中最大数对应的索引, 如果最大数有多个, 则取第一个
y0 = f(x0)


print('x0=',x0,'y0=',y0)
