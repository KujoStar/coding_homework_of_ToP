import math
import numpy as np
ans = []
for i in range(0, 26):
    res = math.comb(25, i) * ((0.6) ** i ) * ((0.4) ** (25 - i))
    ans.append(res)

total = 0
for i in range(11, 20):
    total += ans[i]
    
print(total)