import matplotlib.pyplot as plt
import numpy as np
from random import normalvariate as norm
from random import choice
import math

def make_data(n):
    raw_data = []
    observation = []
    for _ in range(0, n):
        raw_data += [norm(5, 1)]
        
    for _ in range(0, n):
        observation += [choice(raw_data)]
        
    return math.exp(sum(observation) / n)

total_data = []
norm_log = lambda x, mu, sigma: 1 / (x * math.sqrt(2 * math.pi) * sigma) * math.exp(-1 / (2 * (sigma ** 2)) * (math.log(x)-mu) ** 2)
for _ in range(0, 1000):
    total_data += [make_data(100)]
tensorhower = np.linspace(min(total_data), max(total_data), 1000)

plt.figure(dpi = 300)
plt.hist(total_data, bins = 30, density = True)
plt.plot(tensorhower, [norm_log(x, 5, 1/10) for x in tensorhower])
plt.show()

print(np.array(total_data).var(), (math.exp(1/100)-1) * math.exp(2 * 5 + 1/100))