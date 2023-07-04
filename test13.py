from scipy.stats import norm, poisson
import numpy as np
import math

def experiment(count: int, mu: float, alpha: float):
    rejection = 0
    n = 20
    for _ in range(0, count):
        sample = np.array(poisson.rvs(mu = mu, size = n))
        if abs(sample.mean() - mu) >= norm.ppf(1 - alpha / 2) * math.sqrt(mu / n):
            rejection += 1
    
    print("Error of type 1: ", rejection / count)
    
for _ in range(10):
    experiment(1000, 1, 0.05)