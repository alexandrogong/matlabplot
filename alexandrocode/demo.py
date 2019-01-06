import matplotlib.pyplot as plt
import pylab as pl
import pandas as pd
import numpy as np
# head = ["表头1", "表头2", "表头3"]
# l = [[1, 2, 3], [4, 5, 6], [8, 7, 9]]
# df = pd.DataFrame(l)
# df.to_csv("testfoo.csv")

# 提供中文字符支持
pl.rcParams['font.sans-serif'] = ['SimHei']

x = np.linspace(1, 10, 10)
y = np.random.randint(1, 10, 10)

plt.figure(figsize=[6, 6])

plt.plot(x, y, color='orange')
plt.bar(x, y, color='g')
plt.scatter(x, y, color='r')

plt.show()

# 线型图
plt.subplot(2, 2, 1)
plt.title('linear')
plt.xlabel('x label')
plt.ylabel('y label')
plt.plot(x, y, color='b')

# 柱状图
plt.subplot(2, 2, 2)
plt.title('bar')
plt.xlabel('x label')
plt.ylabel('y label')
plt.bar(x, y, color='g')

# 水平柱状图
plt.subplot(2, 2, 3)
plt.title('barh')
plt.xlabel('x label')
plt.ylabel('y label')
plt.barh(x, y, color='r')

# 散点图
plt.subplot(2, 2, 4)
plt.title('scatter')
plt.xlabel('x label')
plt.ylabel('y label')
plt.scatter(x, y, color='y')

plt.show()
plt.close()



