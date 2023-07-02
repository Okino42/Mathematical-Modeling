# ！/usr/bin/nev python
# -*-coding:utf8-*-
# ！/usr/bin/nev python
# -*-coding:utf8-*-
def runge_kutta(theta_in, theta_wall, h):
    # 定义常数和参数
    P_heat = 8000
    C_in = 1.1e6
    C_wall = 1.86e8
    R1 = 1.2e-3
    R2 = 9.2e-3
    theta_out = 0

    # 计算当前theta_wall对应的theta_in值
    theta_wall_curr = (theta_in * R2 + theta_out * R1) / (R1 + R2)

    # 计算k1
    k1_theta_in = (P_heat - (theta_in - theta_wall_curr) / R1) / C_in
    k1_theta_wall = ((theta_in - theta_wall_curr) / R1 - (theta_wall_curr - theta_out) / R2) / C_wall

    # 计算k2
    theta_in_temp = theta_in + 0.5 * h * k1_theta_in
    theta_wall_temp = theta_wall + 0.5 * h * k1_theta_wall
    theta_wall_temp_curr = (theta_in_temp * R2 + theta_out * R1) / (R1 + R2)
    k2_theta_in = (P_heat - (theta_in_temp - theta_wall_temp_curr) / R1) / C_in
    k2_theta_wall = ((theta_in_temp - theta_wall_temp_curr) / R1 - (theta_wall_temp_curr - theta_out) / R2) / C_wall

    # 计算k3
    theta_in_temp = theta_in + 0.5 * h * k2_theta_in
    theta_wall_temp = theta_wall + 0.5 * h * k2_theta_wall
    theta_wall_temp_curr = (theta_in_temp * R2 + theta_out * R1) / (R1 + R2)
    k3_theta_in = (P_heat - (theta_in_temp - theta_wall_temp_curr) / R1) / C_in
    k3_theta_wall = ((theta_in_temp - theta_wall_temp_curr) / R1 - (theta_wall_temp_curr - theta_out) / R2) / C_wall

    # 计算k4
    theta_in_temp = theta_in + h * k3_theta_in
    theta_wall_temp = theta_wall + h * k3_theta_wall
    theta_wall_temp_curr = (theta_in_temp * R2 + theta_out * R1) / (R1 + R2)
    k4_theta_in = (P_heat - (theta_in_temp - theta_wall_temp_curr) / R1) / C_in
    k4_theta_wall = ((theta_in_temp - theta_wall_temp_curr) / R1 - (theta_wall_temp_curr - theta_out) / R2) / C_wall

    # 计算下一个时间步的theta_in和theta_wall
    theta_in_next = theta_in + (h / 6) * (k1_theta_in + 2 * k2_theta_in + 2 * k3_theta_in + k4_theta_in)
    theta_wall_next = theta_wall + (h / 6) * (k1_theta_wall + 2 * k2_theta_wall + 2 * k3_theta_wall + k4_theta_wall)

    # 计算下一个时间步的theta_in对应的theta_wall值
    theta_wall_next_curr = (theta_in_next * R2 + theta_out * R1) / (R1 + R2)

    # 更新theta_in和theta_wall的值
    theta_in_next = theta_in_next
    theta_wall_next = theta_wall_next_curr

    return theta_in_next, theta_wall_next

