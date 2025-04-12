import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
# 定义数据点（示例数据，需要根据你的图调整）
points = {
    "ChatGPT-4o": (1, 0.71, 'pink', 'o'),
    "LLaMa3 8B": (0.58, 0.39, 'blue', '^'),
    "LLaMa3 70B": (0.77, 0.68, 'blue', 'v'),
    "DeepSeek-Coder 1.3B": (0.41, 0.37, 'purple', '*'),
    "微调后模型": (0.89, 0.88, 'magenta', 'd'),
}

# 创建图表
fig, ax = plt.subplots(figsize=(5,5))

# 绘制散点
for label, (x, y, color, marker) in points.items():
    ax.scatter(x, y, color=color, marker=marker, s=150, label=label, edgecolors='black', alpha=0.8)

# 设置坐标轴
ax.set_xlabel("语法正确率", fontsize=12)
ax.set_ylabel("语义正确率", fontsize=12)
ax.set_xlim(-0.1, 1.1)
ax.set_ylim(-0.1, 1.1)

# 添加图例
ax.legend(loc="upper left", title="模型")

# 显示图表
plt.grid(True, linestyle="--", alpha=0.6)
plt.show()
