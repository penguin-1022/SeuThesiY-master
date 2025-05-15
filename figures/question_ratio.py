import matplotlib.pyplot as plt
import matplotlib
import numpy as np

matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
matplotlib.rcParams['axes.unicode_minus'] = False  # 解决负号 '-' 显示问题
# 问题类型和对应占比
labels = ['位置类问题', '位置关系类问题', '与位置相关的计数类问题']
sizes = [33.9, 32.8, 33.3]
colors = ['#66c2a5', '#fc8d62', '#8da0cb']


# 创建图和坐标轴
fig, ax = plt.subplots(figsize=(7, 7))
wedges, texts = ax.pie(sizes,
                       colors=colors)  # 使用环状图更好放文字

# 添加每个扇区的文字（扇区中间）
for i, p in enumerate(wedges):
    ang = (p.theta2 + p.theta1) / 2.0
    x = np.cos(np.deg2rad(ang)) * 0.7
    y = np.sin(np.deg2rad(ang)) * 0.7
    ax.text(x, y,
            f'{labels[i]}\n{sizes[i]}%',
            ha='center', va='center', fontsize=10)

ax.set_aspect('equal')
plt.show()