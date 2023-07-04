import numpy as np
from numpy import *
import matplotlib.pyplot as plt
import random as rd
#'''
#绘制单个散点图
plt.xlim(0, 1001)
plt.ylim(0, 1)
times = []
percents = []
cnt = 0
for i in range(1, 1001):
    times.append(i)
    j = rd.randint(1, 10)
    if(1 <= j <= 3):
        cnt += 1
    res = round(cnt / i, 2)
    percents.append(res)

maxsize = 2000000
m = 0.2
N =len(times)
s = maxsize / plt.gcf().dpi * N + 2 * m
margin = m / plt.gcf().get_size_inches()[0]
plt.gcf().subplots_adjust(left=margin, right=1. - margin)
plt.gcf().set_size_inches(s, plt.gcf().get_size_inches()[1])
plt.scatter(times, percents, s = 0.5)
plt.show()
#'''

up_times = []
for i in range(1, 101):
    cnt = 0
    for j in range(1, 801):
        temp = rd.randint(1, 10)
        if(1 <= temp <= 7):
            cnt += 1
    up_times.append(cnt)

b = mean(up_times)
print(b)
plt.hist(up_times,bins=10,edgecolor="r",histtype="bar",alpha=0.5)
plt.show()
