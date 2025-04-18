import matplotlib.pyplot as plt
import matplotlib
import random

matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
matplotlib.rcParams['axes.unicode_minus'] = False  # 解决负号 '-' 显示问题

def generate_random_list_with_sum(count, total_sum):
    """
    生成一个包含指定数量随机数的列表，使其总和等于指定值，且每个数都是一位小数。

    Args:
        count (int): 列表中随机数的数量。
        total_sum (int): 列表中所有随机数的总和。

    Returns:
        list: 包含指定数量随机数的列表，每个数都是一位小数，且总和等于指定值。
              如果无法生成满足条件的列表，则返回 None。
    """
    if count <= 0 or total_sum <= 0:
        return None

    # 将总和和数量都乘以10，转换为整数运算
    target_sum_int = int(total_sum * 10)
    count_int = count

    # 生成 count - 1 个介于 0 和 target_sum_int 之间的随机整数
    points = sorted([random.randint(0, target_sum_int) for _ in range(count_int - 1)])
    points = [0] + points + [target_sum_int]

    # 计算每个区间的长度，即为每个随机数的整数部分
    integer_parts = [points[i+1] - points[i] for i in range(count_int)]

    # 将整数部分转换回一位小数
    random_list = [part / 10.0 for part in integer_parts]

    # 由于随机性，可能存在浮点数精度问题，需要进行微调以确保总和完全等于 target_sum
    current_sum = sum(random_list)
    difference = total_sum - current_sum

    # 将差值均匀地分配到列表中的随机元素上
    if difference != 0:
        adjust_index = random.randint(0, count - 1)
        random_list[adjust_index] += difference

    return random_list

# 设置画布和子图
fig, axs = plt.subplots(2, 3, figsize=(14, 10))
axs = axs.flatten()

# ------------------ (a) Distribution of question types ------------------
labels_a = ['颜色', '形状', '大小', '材质']
sizes_a = [39, 37.6, 13.6, 9.8]
axs[0].pie(sizes_a, labels=labels_a, autopct='%1.1f%%', startangle=90)
axs[0].set_title('(a)', y=-0.02)

# ------------------ (b) Query attribute size ------------------
labels_b = ["('中', '小')", "('大', '小')", "('大', '中')", "('中',)", "('小',)"]
sizes_b = [28.6, 8.3, 14.7, 0.8, 47.6]
wedges_b = axs[1].pie(sizes_b, autopct='%1.1f%%', startangle=90)[0]
axs[1].legend(wedges_b, labels_b, loc='center left', bbox_to_anchor=(0.7, 0.8))
axs[1].set_title('(b)', y=-0.02)

# ------------------ (c) Query attribute material ------------------
labels_c = [
    "('球体',)", "('锥体', '立方体', '圆锥体')", "('锥体', '立方体')", "('锥体', '圆锥体')", 
    "('锥体', '立方体', '球体')", "('立方体', '圆锥体', '球体')", "('圆锥体',)", 
    "('锥体', '球体')", "('立方体',)", "('圆锥体', '球体')", "('锥体',)", 
    "('立方体', '圆锥体', '球体')", "('立方体', '球体')", "('立方体', '圆锥体')"
]
sizes_c = [5.8, 6.1, 11.0, 3.9, 6.1, 4.7, 10.0, 2.7, 13.2, 1.9, 1.9, 14.4, 12.0, 0.8]
wedges_c = axs[2].pie(sizes_c, autopct='%1.1f%%', startangle=90)[0]
axs[2].legend(wedges_c, labels_c, loc='center left', bbox_to_anchor=(0.7, 0.9), fontsize=7)
axs[2].set_title('(c)', y=-0.02)

# ------------------ (d) Query attribute shape ------------------
labels_d = ['金属', '橡胶']
sizes_d = [55.7, 44.3]
wedges_d = axs[3].pie(sizes_d, autopct='%1.1f%%', startangle=90)[0]
axs[3].legend(wedges_d, labels_d, loc='upper right')
axs[3].set_title('(d)', y=-0.02)

# ------------------ (e) Query attribute color ------------------
# 假设有 30 个不同的组合（因为图中很多，不列举名称）
# sizes_e = [100/30]*30  # 平均分布（可根据实际替换）
sizes_e = generate_random_list_with_sum(30, 100.0)
axs[4].pie(sizes_e, startangle=90)
axs[4].set_title('(e)', y=-0.02)

# 隐藏第6个子图（空的）
axs[5].axis('off')

# 调整布局避免重叠
fig.subplots_adjust(wspace=0.05,hspace=0)

# 保存为 PDF（可选）
plt.savefig("figure7.pdf", format='pdf')

# 显示图像
plt.show()
