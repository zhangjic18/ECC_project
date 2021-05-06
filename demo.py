import random

from add import add
from sub import sub
from multiply import multiply

# 比特币系统选用的secp256k1的参数
p = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F
a = 0
b = 7
G = [0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798,
     0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8]
n = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141
h = 1

k = random.randint(1, n - 1)  # k（k<n）为私有密钥
K = multiply(k, G)  # K为公开密钥，K=kG

M = multiply(random.randint(1, n - 1), G)  # M为明文对应的点（实际编码算法不是这个）

r = random.randint(1, n - 1)

C = [multiply(r, G), add(M, multiply(r, K))]  # C为密文

M_decoded = sub(C[1], multiply(k, C[0]))  # 解密
print("明文对应的点：", M)
print("解密得到的明文对应的点：", M_decoded)
