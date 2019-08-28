import random

'''
junquera@opa:~/Dropbox/Estudios/UEM/TFM/it3/tfm/lwe_tests$ python3 test_lwe.py
x > 1
c1:  [20879, 467127, 239889, 298626, 143587, 116876, 441870, 358117, 405978, 117286]
c2:  [862895, 409484, 878468, 595170, 591475, 813510, 498679, 582178, 793386, 539857]
Result:  [340517, 340521, 340515]
junquera@opa:~/Dropbox/Estudios/UEM/TFM/it3/tfm/lwe_tests$ python3 test_lwe.py
x > 0
c1:  [245223, 483493, 619825, 4950, 167883, 200668, 6545, 414358, 572824, 560333]
c2:  [327111, 452061, 70139, 343482, 668823, 602074, 230847, 195368, 287346, 169525]
Result:  [0, 9, 3]
'''

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
        b.append((aes[i][j]*s[j]+e[j]) % MOD) # % MOD
    bs.append(b)

# TODO Probar para array de x
x = int(input("x > "))

# Cifrar
v = []
for i in range(DIMENSIONS):
    '''
    Si v es aleatorio, queda delatada la b porque si x=0
    y v=0 a=0 y b=x*q/2. v tiene que ser 1
    '''
    # v.append(random.randint(0, 1))
    v.append(1)

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
    for j in range(DIMENSIONS):
        c1 = reses_a[i][j]
        c2 = reses_b[i][j]
        c1_aux = c1 * s[j]
        dec.append((c2 - c1_aux) % MOD)

print("c1: ", reses_a[0])
print("c2: ", reses_b[0])
print("Result: ", dec[:3])
