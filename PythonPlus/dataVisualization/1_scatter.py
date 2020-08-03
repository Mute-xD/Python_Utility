import matplotlib.pyplot as plt

dataX = list(range(0, 1000, 2))
dataY = [i ** 2 for i in dataX]

plt.scatter(dataX, dataY, s=40, c=dataY, cmap='Blues', edgecolors='None')
plt.title('Square    Numbers', fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Square', fontsize=14)
plt.tick_params(axis='both', labelsize=14)
plt.axis([0, 1100, 0, 1100000])  # 指定两轴范围
plt.savefig('square.svg')
