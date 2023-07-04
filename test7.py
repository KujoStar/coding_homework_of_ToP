from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np
import random as rd
import math
''' 绘制标准正态分布对应的Q-Q图
result = np.random.standard_normal(100)
result.sort()
another = [norm.ppf((x-0.5)/100) for x in range(1,101)]
plt.plot(result, another)
plt.show()
'''
### 绘制Cauchy分布对应的Q-Q图
result = np.random.standard_cauchy(100)
result.sort()
another = [norm.ppf((x-0.5)/100) for x in range(1,101)]
plt.plot(result, another)
plt.show()