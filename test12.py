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
for _ in range(0, 1000):
    total_data += [make_data(100)]

mean = sum(total_data) / 1000
alpha = math.exp(1 / 200)
x = sum([math.log(make_data(100)) for _ in range(0, 1000)]) / 1000

print("First: ", [mean / (alpha + 1.96 * math.sqrt(alpha * (alpha - 1) / 1000)), mean / (alpha - 1.96 * math.sqrt(alpha * (alpha - 1) / 1000))])
print("Second: ", [math.exp(x - 1.96 * (10 ** (-2.5))), math.exp(x + 1.96 * (10 ** (-2.5)))])