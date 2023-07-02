# ！/usr/bin/nev python
# -*-coding:utf8-*-
import networkx as nx
import matplotlib.pyplot as plt

# 创建一个空的有向图
G = nx.DiGraph()

# 添加社交网络中的节点
nodes = ['Alice', 'Bob', 'Charlie', 'Dave', 'Eve']
G.add_nodes_from(nodes)

# 添加社交网络中的边
edges = [('Alice', 'Bob'), ('Bob', 'Charlie'), ('Charlie', 'Dave'), ('Dave', 'Eve'), ('Eve', 'Alice')]
G.add_edges_from(edges)

# 使用spring布局获取节点的二维坐标
pos = nx.spring_layout(G)

# 绘制节点和边
nx.draw_networkx_nodes(G, pos)
nx.draw_networkx_edges(G, pos)

# 显示节点标签
labels = {node: node for node in G.nodes}
nx.draw_networkx_labels(G, pos, labels, font_size=12, font_color='w')

# 隐藏坐标轴
plt.axis('off')

# 显示图形
plt.show()



