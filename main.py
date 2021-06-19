import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np
bc = mcolors.BASE_COLORS

f = ['0001.lvm', '0002.lvm', '0004.lvm', '0005.lvm']
d = []
x = []
y = []
x1 = []
y1 = []
x2 = []
y2 = []
x3 = []
y3 = []
sl = slice(None, 100)

for i in f:
    with open(i, 'r') as f:
        read_file = f.readlines()
        d.append(read_file)

for i in range(len(d)):
    for j in d[i]:
        a = j.split('\t')
        if i == 0:
            x.append(a[0])
            x = x[sl]
            b = a[1]
            y.append(b[0:-1])
            y = y[sl]
        if i == 1:
            x1.append(a[0])
            x1 = x1[sl]
            b = a[1]
            y1.append(b[0:-1])
            y1 = y1[sl]
        if i == 2:
            x2.append(a[0])
            x2 = x2[sl]
            b = a[1]
            y2.append(b[0:-1])
            y2 = y2[sl]
        if i == 3:
            x3.append(a[0])
            x3 = x3[sl]
            b = a[1]
            y3.append(b[0:-1])
            y3 = y3[sl]

plt.plot(x, y, "g--")
plt.plot(x1, y1, "r--")
plt.plot(x2, y2, "b--")
plt.plot(x3, y3, "w--")

plt.show()


