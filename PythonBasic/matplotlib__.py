import numpy as np
import matplotlib.pyplot as plt

# 以下部分代码重用较多，为便于理解未省略
####################################
# x = np.linspace(-1, 1, 100)
# y = 2 * x + 1
# plt.plot(x, y)
# plt.show()
####################################

# x = np.linspace(-1, 1, 100)
# y1 = 2 * x + 1
# y2 = x ** 2
# plt.figure()
# plt.plot(x, y1)
# plt.figure(figsize=(8, 5))  # 大小可调
# plt.plot(x, y2)
# plt.show()
#
# plt.plot(x, y1, color="red", linewidth=1.0, linestyle="--")
# plt.plot(x, y2, color="blue", linewidth=3.0, linestyle="-")
# plt.show()
################################################

# x = np.linspace(-3, 3, 100)
# y1 = 2 * x + 1
# y2 = x ** 2
#
# plt.xlim((-1, 2))  # 自定义 x, y 范围
# plt.ylim((-2, 3))
# plt.xlabel("wow")  # 坐标轴命名
# plt.ylabel("ha")
# ticksX = np.linspace(-1, 2, 10)  # 改变采样点
# plt.xticks(ticksX)
# plt.yticks([-1, 0, 1, 2, 3], ["very bad", "bad", "normal", "better", "best"])  # 采样点文字描述
#
# plt.plot(x, y1, color="red", linewidth=1.0, linestyle="--")
# plt.plot(x, y2, color="blue", linewidth=3.0, linestyle="-")
# plt.show()
###########################################################

# x = np.linspace(-3, 3, 100)
# y1 = 2 * x + 1
# y2 = x ** 2
#
# plt.xlim((-1, 2))  # 自定义 x, y 范围
# plt.ylim((-2, 3))
# plt.xlabel("wow")  # 坐标轴命名
# plt.ylabel("ha")
# ticksX = np.linspace(-1, 2, 10)  # 改变采样点
# plt.xticks(ticksX)
# plt.yticks([-1, 0, 1, 2, 3], ["very bad", "bad", "normal", "better", "best"])  # 采样点文字描述
#
# ax1 = plt.gca()  # get current axis
# ax1.spines["right"].set_color("none")  # 设置边框
# ax1.spines["top"].set_color("none")  # set_color color / none
# # 改变坐标轴位置
# ax1.xaxis.set_ticks_position("bottom")
# ax1.yaxis.set_ticks_position("left")
# # 基于数据的坐标轴位置
# ax1.spines["bottom"].set_position(("data", 0))
# ax1.spines["left"].set_position(("data", 0))
#
# plt.plot(x, y1, color="red", linewidth=1.0, linestyle="--")
# plt.plot(x, y2, color="blue", linewidth=3.0, linestyle="-")
# plt.show()
####################################################################

# x = np.linspace(-3, 3, 100)
# y1 = 2 * x + 1
# y2 = x ** 2
#
# plt.xlim((-1, 2))  # 自定义 x, y 范围
# plt.ylim((-2, 3))
# plt.xlabel("wow")  # 坐标轴命名
# plt.ylabel("ha")
#
# l1, = plt.plot(x, y1, color="red", linewidth=1.0, linestyle="--")
# l2, = plt.plot(x, y2, color="blue", linewidth=3.0, linestyle="-")
# plt.legend(handles=[l1, l2], labels=["x", "y"], loc="lower right")  # best / left / lower right
# ticksX = np.linspace(-1, 2, 10)  # 改变采样点
# plt.xticks(ticksX)
# plt.yticks([-1, 0, 1, 2, 3], ["very bad", "bad", "normal", "better", "best"])  # 采样点文字描述
# plt.show()
#####################################################################################

# x = np.linspace(-3, 3, 100)
# y1 = 2 * x + 1
# l1 = plt.plot(x, y1, color="red", linewidth="1.0", linestyle="-")
# ax1 = plt.gca()  # get current axis
# # 改变坐标轴位置
# ax1.spines["top"].set_color("none")
# ax1.spines["right"].set_color("none")
# # 基于数据的坐标轴位置
# ax1.spines["bottom"].set_position(("data", 0))
# ax1.spines["left"].set_position(("data", 0))
# x0 = 0.5
# y0 = 2 * x0 + 1
# plt.scatter(x0, y0, s=50, color="b")  # 画一个点
# plt.plot([x0, x0], [y0, 0], "k--", lw=2)  # (x0, y0) 与 (x0, 0) 连线, black 虚线, linewidth = 2
# plt.annotate(r'$2x+1=%s$' % y0, xy=(x0, y0), xytext=(+30, -30), textcoords="offset points", fontsize=16,
#              arrowprops=dict(arrowstyle="->", connectionstyle="arc3, rad=0.2"))
# # r"表达式格式化" % 参数， xy=(实际的xy), xytext=(偏移量), textcoords=点偏移, fontsize=字号
# # arrow图形=dict(arrowstyle=形状, connectionstyle=连接方式)
# plt.text(-2.5, 2, r"$this\ is\ the\ text$", fontdict={"size": 16, "color": "r"})
# # 起始位置, 表达式格式化, fontdict={"size":字号, "color": "颜色"}
# plt.show()
###############################################################################################
# plt.scatter(np.arange(5), np.arange(5))  # 散点图 x, y 传入
# plt.show()
# x = np.random.normal(0, 1, 500)  # 范围数量控制的随机数
# y = np.random.normal(0, 1, 500)
# plt.scatter(x, y, s=50, c="b", alpha=0.5)  # s=点的大小 b=颜色 alpha=透明度
#
# plt.xlim((-2, 2))  # 强制x, y范围
# plt.ylim((-2, 2))
# plt.xticks(())  # 不传入可隐藏边框
# plt.yticks(())
# plt.show()
########################################################################################################
# x = np.arange(10)
# y = 2 ** x + 10
# plt.bar(x, y)  # 直方图 x, y 传入 , -y可以倒过来
# plt.show()
# plt.bar(x, y, facecolor="#9999ff", edgecolor="white")  # facecolor=柱体颜色 edgecolor=柱边框颜色
# for x, y in zip(x, y):  # 添加顶点标注 zip同时传入 x, y
#     plt.text(x, y, '%.2f' % y, ha="center", va="bottom")  # 利用格式化
# plt.show()
#########################################################################################################
# def func(x1, y1):
#     return (1 - x1 / 2 + x1 ** 5 + y1 ** 3) * np.exp(-x1 ** 2 - y1 ** 2)  # 一个神秘的方程
#
#
# x = np.linspace(-3, 3, 100)
# y = np.linspace(-3, 3, 100)
# X, Y = np.meshgrid(x, y)  # x, y 转化为网格
# plt.contourf(X, Y, func(X, Y), 8, alpha=0.75, cmap=plt.cm.hot)  # 8+1条等高线, 热力图
#
# C = plt.contour(X, Y, func(X, Y), 8, colors="black", linewidth=.5)  # 描线, 加注释
# plt.clabel(C, inline=True, fontsize=10)
#
# plt.xticks(())
# plt.yticks(())
# plt.show()
######################################################################################################
# from mpl_toolkits.mplot3d import Axes3D  # 注意大写
#
# fig = plt.figure()
# ax = Axes3D(fig)
#
# x = np.arange(-4, 4, 0.25)
# y = np.arange(-4, 4, 0.25)
# X, Y = np.meshgrid(x, y)
# R = np.sqrt(X ** 2 + Y ** 2)
# Z = np.sin(R)
#
# ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.get_cmap("rainbow"))
# # rstride=X方向色块大小, cstride=Y方向色块大小
# ax.contourf(X, Y, Z, zdir="z", offset=-2, cmap="rainbow")
# # 向下映射等高线图 zdir=映射方向 offset=偏移量
# ax.set_zlim(-2, 2)  # 限制 z 范围
# plt.show()
######################################################################################
# plt.figure()
# # like this
# # x   x
# # x   x
# plt.subplot(2, 2, 1)  # 2X2 1号位
# plt.plot([0, 1], [0, 1])
# plt.subplot(2, 2, 2)  # 2X2 2号位
# plt.plot([0, 1], [0, 1])
# plt.subplot(2, 2, 3)  # 2X2 3号位
# plt.plot([0, 1], [0, 1])
# plt.subplot(224)  # 2X2 4号位 逗号可省略
# plt.plot([0, 1], [0, 1])
# plt.show()
#
# # like this
# #     x
# # x   x   x
# plt.subplot(2, 1, 1)
# plt.plot([0, 1], [0, 1])
# plt.subplot(2, 3, 4)  # 注意 : 4号位
# plt.plot([0, 1], [0, 1])
# plt.subplot(2, 3, 5)
# plt.plot([0, 1], [0, 1])
# plt.subplot(2, 3, 6)
# plt.plot([0, 1], [0, 1])
# plt.show()
########################################################################################
from matplotlib import animation

fig, ax = plt.subplots()
x = np.arange(0, 2 * np.pi, 0.01)
line, = ax.plot(x, np.sin(x))


def animate(i):
    line.set_ydata(np.sin(x + i / 10))
    return line


def init():
    line.set_ydata(np.sin(x))
    return line


ani = animation.FuncAnimation(fig=fig, func=animate, init_func=init, interval=20)
plt.show()
