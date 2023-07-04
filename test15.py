import numpy as np
from scipy.stats import cauchy, norm
def do(n):
    print(f"When n = {n}:")
    data = np.array(cauchy.rvs(size = n))
    cnt = [0, 0, 0, 0, 0, 0]
    mu = data.mean()
    sig = data.std()
    e = np.array([norm.cdf(-20, loc = mu, scale = sig) - 0, norm.cdf(-10, loc = mu, scale = sig) - norm.cdf(-20, loc = mu, scale = sig), norm.cdf(0, loc = mu, scale = sig) - norm.cdf(-10, loc = mu, scale = sig), norm.cdf(10, loc = mu, scale = sig) - norm.cdf(0, loc = mu, scale = sig), norm.cdf(20, loc = mu, scale = sig) - norm.cdf(10, loc = mu, scale = sig), 1 - norm.cdf(20, loc = mu, scale = sig), ]) * n
    for i in data:
        if i < -20:
            cnt[0] += 1
        elif i < -10:
            cnt[1] += 1
        elif i < 0:
            cnt[2] += 1
        elif i < 10:
            cnt[3] += 1
        elif i < 20:
            cnt[4] += 1
        else:
            cnt[5] += 1  
                 
    chi = 0
    for i in range(0, 6):
        chi += (e[i] - cnt[i]) ** 2 / e[i] 
        
    print("real value:")
    print(cnt)
    print("expected value:")
    print(e)
    print(f"chi = {chi}")
    
do(30)
do(100)
do(1000)