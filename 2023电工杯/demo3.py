# ！/usr/bin/nev python
# -*-coding:utf8-*-
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


# 迭代求解微分方程组
theta_in = 20
theta_wall = 0
theta_out = 0
t = 0
t0 = t
dt = 0.01
P_heat = 8

while t <= t0 + 1:
    theta_in, theta_wall = solve_differential_equations(theta_in, theta_wall, theta_out, t, dt, P_heat)
    # print(f"当前时间，第{t}分钟，当前室内温度：{theta_in}摄氏度")
    t += dt
# 输出最终结果
print(f"当前时间:第{round(t)}分钟;当前室内温度：{round(theta_in,4)}摄氏度")



