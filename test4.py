import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import math
ans = []
for i in range(0, 26):
    res = math.comb(25, i) * ((0.6) ** i ) * ((0.4) ** (25 - i))
    ans.append(res)
x = list(range(0,26));
plt.plot(x, ans, lw=1, marker = 'o', ls='-', alpha=1)
plt.plot()
plt.show()