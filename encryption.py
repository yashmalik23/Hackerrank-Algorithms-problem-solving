import math

s = input().strip().replace(' ', '')
cols = int(math.ceil(len(s) ** 0.5))

for i in range(cols):
    p=[s[x] for x in range(i, len(s), cols)]
    print(''.join(p),end=' ')