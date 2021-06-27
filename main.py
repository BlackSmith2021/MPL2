import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
bc = mcolors.BASE_COLORS

d = []
x = []
y = []
x1 = []
y1 = []
x2 = []
y2 = []
x3 = []
y3 = []

def read_one_file(f):
    with open(f, 'r') as f_mf:
        read_file = f_mf.readlines()
        return read_file

def read_sever_files(f_s):
    for i in f_s:
        d.append(read_one_file(i))
    for i in range(len(d)):
        for j in d[i]:
            a = j.split('\t')
            if i == 0:
                x.append(a[0])
                y.append(a[1][0:-1])
            if i == 1:
                x1.append(a[0])
                y1.append(a[1][0:-1])
            if i == 2:
                x2.append(a[0])
                y2.append(a[1][0:-1])
            if i == 3:
                x3.append(a[0])
                y3.append(a[1][0:-1])

read_sever_files(['0001.lvm', '0002.lvm', '0004.lvm', '0005.lvm'])



plt.plot(x[::100], y[::100], "g--")
plt.plot(x1[::100], y1[::100], "r--")
plt.plot(x2[::100], y2[::100], "b--")
plt.plot(x3[::100], y3[::100], "o--")

plt.show()


