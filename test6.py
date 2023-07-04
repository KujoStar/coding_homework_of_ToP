import numpy as np
import matplotlib.pyplot as plt
import random as rd
import math

result = np.random.standard_normal(10000)

another = [math.pow(math.e, x) for x in result]

plt.hist(another,bins=10,edgecolor="r",histtype="bar",alpha=1)

plt.show()

plt.savefig("5-1.png") 

num = list(range(1, 10001))

y = [math.pow(math.e, -(np.log(x))**2 / 2) / (math.sqrt(2 * math.pi) * x) for x in num]

plt.hist(y,bins=5,edgecolor="r",histtype="bar",alpha=1)

plt.show()

plt.savefig("5-2.png")
