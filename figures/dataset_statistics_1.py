import matplotlib.pyplot as plt
import matplotlib
# 设置中文字体
matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
matplotlib.rcParams['axes.unicode_minus'] = False  # 解决负号 '-' 显示问题

# 图6(a): 问题模板分布
labels_a = ['相同关系类问题', '单端目标类问题', '一跳问题', '两跳问题', '三跳问题', '零跳问题', '四跳问题', '五跳问题']
sizes_a = [35.2, 10.1, 15.5, 7.6, 12.2, 7.6, 6.4, 5.5]

# 图6(b): 属性与对象数量分布
labels_b = [
    '物体数量 = 5, 颜色', '物体数量 = 5, 尺寸', '物体数量 = 5, 形状', '物体数量 = 5, 材质',
    '物体数量 = 6, 颜色', '物体数量 = 6, 尺寸', '物体数量 = 6, 形状', '物体数量 = 6, 材质',
    '物体数量 = 7, 颜色', '物体数量 = 7, 尺寸', '物体数量 = 7, 形状', '物体数量 = 7, 材质',
    '物体数量 = 8, 颜色', '物体数量 = 8, 尺寸', '物体数量 = 8, 形状', '物体数量 = 8, 材质',
    '物体数量 = 9, 颜色', '物体数量 = 9, 尺寸', '物体数量 = 9, 形状', '物体数量 = 9, 材质',
]
sizes_b = [2.9, 3.4, 7.4, 7.7, 6.6, 8.9, 8.1, 7.7, 5.3, 8.3, 8.3, 7.7, 7.7, 6.6, 7.7, 8.9, 5.3, 2.9, 6.6, 7.7]

# 设置画布
fig, axs = plt.subplots(1, 2, figsize=(14, 7))

# 子图1
axs[0].pie(sizes_a, labels=labels_a, autopct='%1.1f%%', startangle=140)
axs[0].set_title('(a)', y=-0.02)

# 子图2
wedges = axs[1].pie(sizes_b, autopct='%1.1f%%', startangle=140)[0]
axs[1].set_title('(b)', y=-0.02)
axs[1].legend(wedges, labels_b, loc='upper right', bbox_to_anchor=(0.98, 1), fontsize=8, title="物体数量与属性")
plt.tight_layout()

# 保存为PDF用于LaTeX
plt.savefig("figure6.pdf", format='pdf')
plt.show()
