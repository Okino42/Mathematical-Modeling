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


total_power = []
for i in range(6):
    theta_in = 18 + i*0.8
    theta_out = -25
    R1 = 1.2e-3
    R2 = 9.2e-3
    t_heat_on = 0
    t_heat_off = 0
    time = []
    minute = 0
    theta_wall = (theta_in*R2+theta_out*R1)/(R1+R2)
    # total_power.append([])
    # print(f"total_power为{total_power[i-1]}")
    print(f"这是第{i}户住户")
    print(f"当前时间:第0分钟;室内温度：{round(theta_in, 4)}摄氏度;墙壁温度：{round(theta_wall, 4)}")
    if i % 2 == 0:
        while minute <= 24 * 60 - 1:
            if theta_in > 18:
                minute = minute + 1
                theta_in, theta_wall = heat_off(theta_in, theta_wall, minute)
                t_heat_off = t_heat_off + 1
                total_power.append(0)
                # print(f"第{i}户住户,第{round(minute)}分钟;室内温度：{round(theta_in, 4)}摄氏度;墙壁温度：{round(theta_wall, 4)}")


            else:

                while theta_in < 22:
                    theta_in, theta_wall = heat_on(theta_in, theta_wall, minute)
                    minute = minute + 1
                    t_heat_on = t_heat_on + 1
                    total_power.append(8)
                    # print(f"第{i}户住户,第{round(minute)}分钟;室内温度：{round(theta_in, 4)}摄氏度;墙壁温度：{round(theta_wall, 4)};累计加热时间：{t_heat_on}分钟")
                    if minute == 1440:
                        break

    else:
        while minute <= 24 * 60 - 1:
            if theta_in < 22:
                theta_in, theta_wall = heat_on(theta_in, theta_wall, minute)
                minute = minute + 1
                t_heat_on = t_heat_on + 1
                total_power.append(0)
                # print(f"第{i}户住户,第{round(minute)}分钟;室内温度：{round(theta_in, 4)}摄氏度;墙壁温度：{round(theta_wall, 4)};累计加热时间：{t_heat_on}分钟")


            else:
                while theta_in > 18:
                    minute = minute + 1
                    theta_in, theta_wall = heat_off(theta_in, theta_wall, minute)
                    t_heat_off = t_heat_off + 1
                    time.append(minute)
                    total_power.append(8)
                    # print(f"第{i}户住户,第{round(minute)}分钟;室内温度：{round(theta_in, 4)}摄氏度;墙壁温度：{round(theta_wall, 4)}")
                    if minute == 1440:
                        break

total_power = [total_power[i:i+1440] for i in range(0, len(total_power), 1440)]
# print(f"total_power为{total_power}")
time = [i for i in range(1, 1441)]
new_total_power = [sum(x) for x in zip(*total_power)]
# print(f"new_total_power为{new_total_power}")
print(f"new_total_power的长度为{len(new_total_power)}")

# 绘制600户住户用电功率曲线
plt.plot(time, new_total_power)
plt.grid(True)
plt.title(f"室外温度为{theta_out}℃时,6户用户用电功率曲线/min")
plt.xlabel("时间")
plt.ylabel("总功率/kw")
plt.show()


to_raise = []
to_redecu = new_total_power
for k in range(1440):
    to_raise.append(48 - new_total_power[k])

print(f"6户住户可提供的持续最大向下调节功率值:{max(to_redecu)}")
print(f"6户住户可提供的持续最大向上调节功率值:{max(to_raise)}")
# 绘制600户住户可参与上调总功率曲线
plt.plot(time, to_raise)
plt.grid(True)
plt.title(f"室外温度为{theta_out}℃时,6户住户可参与上调总功率曲线/min")
plt.xlabel("时间")
plt.ylabel("总功率/kw")
plt.show()

# 绘制600户住户可参与上调总功率曲线
plt.plot(time, to_redecu)
plt.grid(True)
plt.title(f"室外温度为{theta_out}℃时,6户住户可参与下调总功率曲线/min")
plt.xlabel("时间")
plt.ylabel("总功率/kw")
plt.show()



