import numpy as np
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE

# 生成随机高维数据
np.random.seed(0)
X = np.random.randn(100, 10)  # 100个样本，每个样本有10个特征

# 对数据进行t-SNE降维
tsne = TSNE(n_components=2)  # 将数据降维到二维
X_tsne = tsne.fit_transform(X)

# 创建交互图形界面
fig, ax = plt.subplots()

# 绘制初始的t-SNE可视化结果
scatter = ax.scatter(X_tsne[:, 0], X_tsne[:, 1])


# 添加交互功能
def on_click(event):
    # 获取鼠标点击的坐标
    x, y = event.xdata, event.ydata

    # 计算距离最近的点的索引
    distances = np.sqrt(np.sum((X_tsne - np.array([x, y])) ** 2, axis=1))
    closest_index = np.argmin(distances)

    # 在图上突出显示距离最近的点
    colors = ['black'] * len(X)
    colors[closest_index] = 'red'
    scatter.set_edgecolors(colors)
    scatter.set_facecolors(colors)

    # 刷新图形界面
    fig.canvas.draw()


# 将鼠标点击事件绑定到图形界面
cid = fig.canvas.mpl_connect('button_press_event', on_click)

# 显示图形界面
plt.show()
