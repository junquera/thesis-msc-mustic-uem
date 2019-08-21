import random

# Basado en https://medium.com/asecuritysite-when-bob-met-alice/public-key-encryption-with-learning-with-errors-lwe-1aa6dd1df4e

Z_MAX = 1e50
MOD = 681029
q=MOD
DIMENSIONS = 10
E_MAX=1e2

s = random.randint(0, MOD)

A = []
B = []
for _ in range(DIMENSIONS):
    a = random.randint(0, MOD)
    A.append(a)
    B.append((a*s + random.randint(0, E_MAX)) % MOD)

# Encrypt
x = int(input("x > "))

u = 0
v = 0
for i in A:
    u = (u + i) % MOD

for i in B:
    v = (v + i) % MOD
     
v = (v + (int(q/2)*x)) % MOD

# Decrypt
dec = (v - (s*u)) % MOD
res = 1 if dec/(q/2) > 0.1 else 0

print(u, v, res)
