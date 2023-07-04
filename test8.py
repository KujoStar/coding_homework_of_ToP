from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np
import random as rd
import math

def func():
    x = range(1, 10001)
    y = [1 if rd.randint(0,1) else -1 for _ in range(1, 10001)]
    z = [sum(y[0:i]) for i in range(0, 10000)]
    plt.plot(x, z)
    
for i in range(0, 10):
    func()
    
plt.show()