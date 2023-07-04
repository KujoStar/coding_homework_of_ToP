from scipy.stats import bernoulli
import numpy as np

def generate(k, p, n):
     num = np.array([sum(bernoulli.rvs(p=p, size=k)) for _ in range(0, n)])
     a1 = num.mean()
     m2 = num.var()
     p_estimate = 1 - m2 / a1
     k_estimate = a1 / (p_estimate)
     return (p_estimate, k_estimate)
 
print("")
print("When k = 10, p = 0.5, n = 1000")
print("num      p           k")
for i in range(0, 10):
    print(" %d   %5f    %5f" %((i, ) + generate(10, 0.5, 1000)))