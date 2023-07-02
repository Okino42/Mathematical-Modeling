# ！/usr/bin/nev python
# -*-coding:utf8-*-
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams["font.sans-serif"]=["SimHei"] #设置字体
plt.rcParams["axes.unicode_minus"]=False #该语句解决图像中的“-”负号的乱码问题
import numpy as np
from scipy.optimize import curve_fit

def solve_differential_equations(theta_in, theta_wall, theta_out, t, dt, P_heat):
    # 设置参数和初始条件
    C_in = 1.1e6
    C_wall = 1.86e8
    R1 = 1.2e-3
    R2 = 9.2e-3

    # 定义龙格-库塔法的四个步骤
    def step1(theta_in, theta_wall):
        return (P_heat - (theta_in - theta_out) / R1) / C_in

    def step2(theta_in, theta_wall, k1):
        theta_in_new = theta_in + 0.5 * dt * k1
        theta_wall_new = theta_wall + 0.5 * dt * step1(theta_in, theta_wall)
        return (theta_in_new, theta_wall_new)

    def step3(theta_in, theta_wall, k2):
        theta_in_new = theta_in + 0.5 * dt * k2
        theta_wall_new = theta_wall + 0.5 * dt * step1(theta_in, theta_wall)
        return (theta_in_new, theta_wall_new)

    def step4(theta_in, theta_wall, k3):
        theta_in_new = theta_in + dt * k3
        theta_wall_new = theta_wall + dt * step1(theta_in, theta_wall)
        return (theta_in_new, theta_wall_new)

    # 计算龙格-库塔法的四个斜率
    k1 = step1(theta_in, theta_wall)
    theta_in2, theta_wall2 = step2(theta_in, theta_wall, k1)
    k2 = step1(theta_in2, theta_wall2)
    theta_in3, theta_wall3 = step3(theta_in, theta_wall, k2)
    k3 = step1(theta_in3, theta_wall3)
    theta_in4, theta_wall4 = step4(theta_in, theta_wall, k3)
    k4 = step1(theta_in4, theta_wall4)

    # 使用龙格-库塔法更新下一个时间步的theta_in和theta_wall的值
    theta_in_next = theta_in + (1 / 6) * dt * (k1 + 2 * k2 + 2 * k3 + k4)
    theta_wall_next = theta_wall + dt * ((theta_in - theta_wall) / R1 - (theta_wall - theta_out) / R2) / C_wall

    return theta_in_next, theta_wall_next



def heat_off(theta_in_formal, theta_wall_formal,minute_formal):
    P_heat = 0
    theta_in = theta_in_formal
    theta_wall = theta_wall_formal
    t = minute_formal
    t0 = minute_formal
    dt = 0.01
    while t <= t0 + 1:
        theta_in, theta_wall = solve_differential_equations(theta_in, theta_wall, theta_out, t, dt, P_heat)
        # print(f"当前时间，第{t}分钟，当前室内温度：{theta_in}摄氏度")
        t += dt
    # print(f"当前时间:第{round(t)}分钟;室内温度：{round(theta_in, 4)}摄氏度;墙壁温度：{round(theta_wall,4)}")
    return theta_in, theta_wall

def heat_on(theta_in_formal, theta_wall_formal,minute_formal):
    P_heat = 280000
    theta_in = theta_in_formal
    theta_wall = theta_wall_formal
    t = minute_formal
    t0 = minute_formal
    dt = 0.01
    while t <= t0 + 1:
        theta_in, theta_wall = solve_differential_equations(theta_in, theta_wall, theta_out, t, dt, P_heat)

        t += dt
    # print(f"当前时间:第{round(t)}分钟;室内温度：{round(theta_in, 4)}摄氏度;墙壁温度：{round(theta_wall, 4)}")
    return theta_in, theta_wall

# 迭代求解微分方程组
theta_in = 22
theta_in_0 = theta_in
theta_out = -20
R1 = 1.2e-3
R2 = 9.2e-3
theta_wall = (theta_in*R2+theta_out*R1)/(R1+R2)
t_heat_on = 0
t_heat_off = 0
time = []
temperature = []
on_and_off = []
minute = 0
list_to_heat_on = []
list_to_heat_off = []
print(f"当前时间:第0分钟;室内温度：{round(theta_in, 4)}摄氏度;墙壁温度：{round(theta_wall,4)}")


while minute <= 24*60-1:
    if theta_in > 18:
        minute = minute + 1
        theta_in, theta_wall = heat_off(theta_in,theta_wall,minute)
        t_heat_off = t_heat_off + 1
        time.append(minute)
        temperature.append(theta_in)
        on_and_off.append(0)
        # -15摄氏度
        # t_to_heat_on = (-0.007286470604968064)*theta_in**2+(-4.093959249282294)*theta_in+92.9659509001159
        # t_to_heat_off = (-0.4980158630732919)*theta_in**2+57.324113522384266*theta_in-871.2012481107544
        # list_to_heat_on.append(t_to_heat_on)
        # list_to_heat_off.append(t_to_heat_off)
        # 0摄氏度
        # t_to_heat_on = (-0.00654624617329838) * theta_in ** 2 + (-3.87403737908692) * theta_in + 87.82535394164228
        # t_to_heat_off = (-1.6364025673132654) * theta_in ** 2 + 130.9399655361916 * theta_in - 1826.8962267414656
        # list_to_heat_on.append(t_to_heat_on)
        # list_to_heat_off.append(t_to_heat_off)

        # -5摄氏度
        t_to_heat_on = (-0.0068289083162163585) * theta_in ** 2 + (-3.971250979897413) * theta_in + 90.66590489948646
        t_to_heat_off = (-1.0405407554253325) * theta_in ** 2 + 93.9723974637585 * theta_in - 1355.0207260167772
        list_to_heat_on.append(t_to_heat_on)
        list_to_heat_off.append(t_to_heat_off)
        print(f"当前时间:第{round(minute)}分钟;室内温度：{round(theta_in, 4)}摄氏度;墙壁温度：{round(theta_wall, 4)}")
        # print(f"功率可持续上调时间为{t_to_heat_on}分钟")

    else:

        while theta_in < 22:
            theta_in, theta_wall = heat_on(theta_in,theta_wall,minute)
            minute = minute + 1
            t_heat_on = t_heat_on + 1
            time.append(minute)
            temperature.append(theta_in)
            on_and_off.append(1)
            #-15
            # t_to_heat_on = (-0.007286470604968064) * theta_in ** 2 + (-4.093959249282294) * theta_in + 92.9659509001159
            # t_to_heat_off = (-0.4980158630732919) * theta_in ** 2 + 57.324113522384266 * theta_in - 871.2012481107544
            # list_to_heat_on.append(t_to_heat_on)
            # list_to_heat_off.append(t_to_heat_off)

            # # 0摄氏度
            # t_to_heat_on = (-0.00654624617329838) * theta_in ** 2 + (-3.87403737908692) * theta_in + 87.82535394164228
            # t_to_heat_off = (-1.6364025673132654) * theta_in ** 2 + 130.9399655361916 * theta_in - 1826.8962267414656
            # list_to_heat_on.append(t_to_heat_on)
            # list_to_heat_off.append(t_to_heat_off)

            # -5摄氏度
            t_to_heat_on = (-0.0068289083162163585) * theta_in ** 2 + (
                -3.971250979897413) * theta_in + 90.66590489948646
            t_to_heat_off = (-1.0405407554253325) * theta_in ** 2 + 93.9723974637585 * theta_in - 1355.0207260167772
            list_to_heat_on.append(t_to_heat_on)
            list_to_heat_off.append(t_to_heat_off)
            print(f"当前时间:第{round(minute)}分钟;室内温度：{round(theta_in, 4)}摄氏度;墙壁温度：{round(theta_wall, 4)};累计加热时间：{t_heat_on}分钟")
            # print(f"功率可持续下调时间为{t_to_heat_off}分钟")


# 创建一个字典，将列表转换为字典的键值对
# data = {'功率上调的可持续时间': list_to_heat_on, '功率下调的可持续时间': list_to_heat_off}
# 创建一个DataFrame对象
# df = pd.DataFrame(data)
# 将DataFrame保存到Excel文件中
# df.to_excel('output-5.xlsx', index=False)


# 绘制图片
plt.plot(time, temperature)
# 添加网格
plt.grid(True)
# 添加标题和坐标轴标签
plt.title(f"初始室内温度：{theta_in_0}，室外温度：{theta_out}，室内温度随时间变化图")
plt.xlabel("时间")
plt.ylabel("室内温度")
# 显示图片
plt.show()

# 绘制图片
plt.plot(time, on_and_off)
# 添加网格
plt.grid(True)
# 添加标题和坐标轴标签
plt.title(f"初始室内温度：{theta_in_0}，室外温度：{theta_out}，电热器随时间变化图")
plt.xlabel("时间")
plt.ylabel("开关状态")
# 显示图片
plt.show()




#上调拟合
new_time = []
for x in time[110:127]:
    new_time.append(127-x)
new_temperature = []
for x in temperature[110:127]:
    new_temperature.append(x)

plt.plot(new_temperature, new_time)
# 添加网格
plt.grid(True)
# 添加标题和坐标轴标签
plt.title(f"初始室内温度：{theta_in_0}，室外温度：{theta_out}，功率上调可持续时间拟合函数")
plt.xlabel("温度")
plt.ylabel("功率上调可持续时间")
# 显示图片
plt.show()

# 定义拟合函数（多项式）
def func(x, a, b, c):
    return a * x**2 + b * x + c
# 执行拟合
params, _ = curve_fit(func, new_temperature, new_time)
# 获取拟合结果
a, b, c = params
# 打印拟合参数
print(f"初始室内温度：{theta_in_0}，室外温度：{theta_out}，功率上调可持续函数拟合参数:")
print("a =", a)
print("b =", b)
print("c =", c)


new_time1 = []
for x in time[128:348]:
    new_time1.append(348 - x)
new_temperature1 = []
for x in temperature[128:348]:
    new_temperature1.append(x)

plt.plot(new_temperature1, new_time1)
# 添加网格
plt.grid(True)
# 添加标题和坐标轴标签
plt.title(f"初始室内温度：{theta_in_0}，室外温度：{theta_out}，功率下调可持续时间拟合函数")
plt.xlabel("温度")
plt.ylabel("功率下调可持续时间")
# 显示图片
plt.show()


# 定义拟合函数（多项式）
def func(x, a, b, c):
    return a * x ** 2 + b * x + c


# 执行拟合
params, _ = curve_fit(func, new_temperature1, new_time1)
# 获取拟合结果
a, b, c = params
# 打印拟合参数
print("功率下调可持续函数拟合参数:")
print("a =", a)
print("b =", b)
print("c =", c)








# 绘制功率可持续上调时间图片
plt.plot(time, list_to_heat_on)
# 添加网格
plt.grid(True)
# 添加标题和坐标轴标签
plt.title(f"初始室内温度：{theta_in_0}，室外温度：{theta_out},功率可持续上调时间函数")
plt.xlabel("时间")
plt.ylabel("功率可持续上调时间")
# 显示图片
plt.show()

# 绘制功率可持续下调时间图片
plt.plot(time, list_to_heat_off)
# 添加网格
plt.grid(True)
# 添加标题和坐标轴标签
plt.title(f"初始室内温度：{theta_in_0}，室外温度：{theta_out},功率可持续下调时间函数")
plt.xlabel("时间")
plt.ylabel("功率可持续下调时间")
# 显示图片
plt.show()