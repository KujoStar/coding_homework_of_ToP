from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np
import random as rd
import math

def normal(n):
    return np.random.standard_normal(n)

def uniform(n):
    return np.random.uniform(0,1,n)

def cauchy(n):
    return np.random.standard_cauchy(n)

def generate(func, n, sample):
    res = [sum(func(n)) / n for _ in range(0, sample)]
    plt.figure(dpi = 400)
    plt.hist(res, bins = 25)
    plt.title(f"X~{func.__name__} distribution, n={n}")
    plt.savefig(f"{func.__name__} for n={n}.jpg")

num = 5000
for i in [1, 25, 100, 1000]:
    generate(normal, i, num)
    generate(uniform, i ,num)
    generate(cauchy, i, num)