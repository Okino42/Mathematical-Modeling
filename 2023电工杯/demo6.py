# ！/usr/bin/nev python
# -*-coding:utf8-*-
# 导入scipy.integrate模块
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams["font.sans-serif"]=["SimHei"] #设置字体
plt.rcParams["axes.unicode_minus"]=False #该语句解决图像中的“-”负号的乱码问题

# 读取Excel文件
df = pd.read_excel('6个住户的总用电功率.xlsx')

# 提取横坐标和纵坐标数据
x = df['时间']
y = df['总功率']

# 绘制折线图
plt.plot(x, y)

plt.grid(True)
# 设置图形标题和坐标轴标签
plt.title('6个住户的总用电功率曲线')
plt.xlabel('时间/min')
plt.ylabel('总用电功率/kw')

# 指定纵坐标的刻度
plt.yticks([0, 8, 16, 24])
# 显示图形
plt.show()



# 读取Excel文件
df = pd.read_excel('6个住户的总用电功率.xlsx')

# 提取横坐标和纵坐标数据
x = df['时间']
y = df['可上调总功率']

# 绘制折线图
plt.plot(x, y)

plt.grid(True)
# 设置图形标题和坐标轴标签
plt.title('6个住户的可上调总功率曲线')
plt.xlabel('时间/min')
plt.ylabel('总用电功率/kw')

# 指定纵坐标的刻度
plt.yticks([0, 8, 16, 24, 32, 40, 48])
# 显示图形
plt.show()


# 读取Excel文件
df = pd.read_excel('6个住户的总用电功率.xlsx')

# 提取横坐标和纵坐标数据
x = df['时间']
y = df['可下调总功率']

# 绘制折线图
plt.plot(x, y)

plt.grid(True)
# 设置图形标题和坐标轴标签
plt.title('6个住户的可下调总功率曲线')
plt.xlabel('时间/min')
plt.ylabel('总用电功率/kw')

# 指定纵坐标的刻度
plt.yticks([0, 8, 16, 24, 32, 40, 48])
# 显示图形
plt.show()
