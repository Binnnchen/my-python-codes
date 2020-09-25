import matplotlib.pyplot as plt

input_value = list(range(1,101))
squares = [x**3 for x in range(1,101)]
plt.plot(input_value,squares, linewidth=5)

# 设置图表标题，并给坐标轴加上标签
plt.title("y=x^3", fontsize=24)
plt.xlabel("x", fontsize=14)
plt.ylabel("y", fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='both', labelsize=14)


plt.show()
