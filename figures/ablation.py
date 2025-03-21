# 用于生成消融实验的图像

import matplotlib.pyplot as plt
import matplotlib

# 设置中文字体
matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
matplotlib.rcParams['axes.unicode_minus'] = False  # 解决负号 '-' 显示问题

# 数据
rounds = [0, 1, 2]

# Execution Rate 数据
deepseek_exec = [51.3, 76.7, 84.2]
llama3_exec = [60.2, 82.2, 89.7]
gpt4mini_exec = [64.6, 84.2, 91.1]

# Accuracy 数据
deepseek_acc = [57.8, 75.5, 79.3]
llama3_acc = [61.1, 78.9, 85.7]
gpt4mini_acc = [69.7, 84.1, 93.4]

# 颜色 & 线型
colors = {'DeepSeek R1': 'blue', 'Llama3': 'green', 'GPT-4.0 turbo': 'orange'}
linestyles = {'可执行率': 'dashed', '正确率': 'solid'}

# 创建图像
plt.figure(figsize=(8, 4))
plt.xticks([0, 1, 2])

# 绘制 Execution Rate
plt.plot(rounds, deepseek_exec, linestyle=linestyles['可执行率'], color=colors['DeepSeek R1'], marker='o', label='DeepSeek R1可执行率')
plt.plot(rounds, llama3_exec, linestyle=linestyles['可执行率'], color=colors['Llama3'], marker='o', label='Llama3可执行率')
plt.plot(rounds, gpt4mini_exec, linestyle=linestyles['可执行率'], color=colors['GPT-4.0 turbo'], marker='o', label='GPT-4.0 turbo可执行率')

# 绘制 Accuracy
plt.plot(rounds, deepseek_acc, linestyle=linestyles['正确率'], color=colors['DeepSeek R1'], marker='s', label='DeepSeek R1正确率')
plt.plot(rounds, llama3_acc, linestyle=linestyles['正确率'], color=colors['Llama3'], marker='s', label='Llama3正确率')
plt.plot(rounds, gpt4mini_acc, linestyle=linestyles['正确率'], color=colors['GPT-4.0 turbo'], marker='s', label='GPT-4.0 turbo正确率')

# 轴标签 & 标题
plt.xlabel("迭代轮数")
plt.ylabel("百分比 (%)")
plt.title("LLM与ASP求解器之间的迭代反馈机制的效果对比")

# 图例
plt.legend()

# 显示网格
plt.grid(True, linestyle="--", alpha=0.6)

# 显示图像
plt.show()
