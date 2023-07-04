import numpy as np
import matplotlib.pyplot as plt
import random as rd

array = np.random.normal(100.0, 10.0, 1000)
another = []
for _ in range(1, 1001):
    j = rd.randint(0, 999)
    another.append(array[j])
    
plt.hist(array,bins=10,edgecolor="r",histtype="bar",alpha=0.5)
print(np.mean(array))
print(np.var(array))
plt.savefig("4-1.png")

plt.hist(another,bins=10,edgecolor="r",histtype="bar",alpha=1)
print(np.mean(another))
print(np.var(another))
plt.savefig("4-2.png")