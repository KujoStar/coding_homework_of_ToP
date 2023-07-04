from scipy.stats import norm, t
import numpy as np

for _ in range(0, 10):
    cnt = 0
    for _ in range(0, 1000):
        arr = np.array(norm.rvs(loc=5.0, scale=1, size=100))
        p = 1-t.cdf((arr.mean()-5.2) / arr.std(ddof=True)*10, 99)
        if p < 0.05:
            cnt += 1
            
    print(cnt / 1000)   
