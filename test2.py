import numpy as np
import math
total = 0
for i in range(0, 11):
    total += (i ** 3) * math.comb(10, i) * ((0.9) ** i) * ((0.1) ** (10-i))
    
print(total)