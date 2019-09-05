import random

Z_MAX = 1e50
MOD = 681029
q=MOD
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
        a.append(random.randint(0, Z_MAX) % MOD)
        e.append(random.randint(0, 10))
    aes.append(a)
    es.append(e)

bs = []
for i in range(len(aes)):
    b = []
    for j in range(DIMENSIONS):
        b.append((aes[i][j]*s[j]+e[j]) % MOD)
    bs.append(b)

x = int(input("x > "))

# Cifrar
v = []
for i in range(DIMENSIONS):
    '''
    Si v es aleatorio, queda delatada la b porque si x=0
    y v=0 a=0 y b=x*q/2. v tiene que ser 1
    '''
    v.append(1)

reses_a = []
reses_b = []
for i in range(len(aes)):
    res_a = []
    res_b = []
    for j in range(DIMENSIONS):
        res_a.append((aes[i][j]*v[j]))
        res_b.append((bs[i][j]*v[j] + x*int(q/2)))

    reses_a.append(res_a)
    reses_b.append(res_b)

# Descifrar
dec = []
for i in range(len(reses_a)):
    for j in range(DIMENSIONS):
        c1 = reses_a[i][j]
        c2 = reses_b[i][j]
        c1_aux = c1 * s[j]
        dec.append((c2 - c1_aux) % MOD)

print("c1: ", reses_a[0])
print("c2: ", reses_b[0])
print("Result: ", dec[:3])
