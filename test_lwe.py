import random

Z_MAX = 1e50
q=Z_MAX
MOD = 681029
DIMENSIONS = 10

s = []
aes = []
es = []

for i in range(DIMENSIONS):
    s.append(random.randint(0, Z_MAX))

for i in range(100):
    a = []
    e = []
    for j in range(DIMENSIONS):
        a.append(random.randint(0, Z_MAX))
        e.append(random.randint(0, Z_MAX))
    aes.append(a)
    es.append(e)

bs = []
for i in range(len(aes)):
    b = []
    for j in range(DIMENSIONS):
        b.append((aes[i][j]*s[j]+e[j])) # % MOD
    bs.append(b)

# TODO Probar para array de x
x = 0

# Cifrar
v = []
for i in range(DIMENSIONS):
    v.append(random.randint(0, 1))

reses_a = []
reses_b = []
for i in range(len(aes)):
    res_a = []
    res_b = []
    for j in range(DIMENSIONS):
        res_a.append((aes[i][j]*v[j])) # % MOD
        res_b.append((bs[i][j]*v[j] + x*int(q/2))) # % MOD

    reses_a.append(res_a)
    reses_b.append(res_b)

# Descifrar
dec = []
for i in range(len(reses_a)):
    c2 = reses_b[i]
    c1 = reses_a[i]
    for j in range(DIMENSIONS):
        c1_aux = (c1[j]*s[j])
        dec.append((c2[j] - c1_aux)) # % MOD

for i in dec:
    print(abs(abs(i))%MOD)
