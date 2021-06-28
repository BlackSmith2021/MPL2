import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
bc = mcolors.BASE_COLORS

def read_one_file(f):
    with open(f, 'r') as f_mf:
        read_file = f_mf.readlines()
        return read_file

def read_sever_files(f_s):
    result = []
    d = []
    for i in f_s:
        d.append(read_one_file(i))
    for i in range(len(d)):
        x = []
        y = []
        for j in d[i]:
            a = j.split('\t')
            x.append(a[0])
            y.append(a[1][0:-1])
        result.append((x, y))
    return result

s = read_sever_files(['0001.lvm', '0002.lvm', '0004.lvm', '0005.lvm'])

print(len(s[0]))

plt.plot(s[0][0][::100], s[0][1][::100], "g--")
plt.plot(s[1][0][::100], s[1][1][::100], "r--")
plt.plot(s[2][0][::100], s[2][1][::100], "b--")
plt.plot(s[3][0][::100], s[3][1][::100], "o--")

plt.show()


