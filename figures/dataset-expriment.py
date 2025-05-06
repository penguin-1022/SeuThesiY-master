import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from matplotlib.lines import Line2D

import matplotlib
# 设置中文字体
matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
matplotlib.rcParams['axes.unicode_minus'] = False  # 解决负号 '-' 显示问题

# 模型名称与准确率
model_names = ['CNN+LSTM', 'DeepSeek', 'Gemini 2.5 Flash', 'ChatGPT-4o']
accuracies = [45.4, 59.4, 65.7, 71.5]
human_accuracy = 94

# 与图中一致的颜色
colors = ['#c49bcf', '#a78ec6', '#80a3d4', '#a3d69b']
human_color = '#804000'  # 棕色线条颜色

# 创建图形
fig, ax = plt.subplots(figsize=(5, 3))

# 画柱状图
bars = ax.bar(range(len(model_names)), accuracies, color=colors)

# 添加数值标签
for bar, acc in zip(bars, accuracies):
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 1,
            f'{acc}', ha='center', va='bottom', fontsize=8)

# 画人类表现线
ax.axhline(human_accuracy, color=human_color, linewidth=1)
ax.text(len(model_names) - 0.5, human_accuracy + 1, f'{human_accuracy}', 
        color=human_color, fontsize=8)

# 设置标签
ax.set_ylabel('准确率')
ax.set_ylim(0, 100)
ax.set_xticks([])  # 不显示横轴标签

# 添加图例
legend_elements = [Patch(facecolor=color, label=name) for color, name in zip(colors, model_names)]
legend_elements.append(Line2D([0], [0], color=human_color, lw=2, label='人类'))
ax.legend(handles=legend_elements, title='图例', frameon=True, loc='center left', bbox_to_anchor=(1.0, 0.5))

plt.tight_layout()
plt.show()
