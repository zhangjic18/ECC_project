	椭圆加解密算法。

​	运行demo.m即可得到示例运行结果

​	算法参数如下（同比特币系统）：

```python
# 比特币系统选用的secp256k1的参数
p = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F
a = 0
b = 7
G = [0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798,
     0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8]
n = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141
h = 1
```

# 1 文件目录如下所示：

```python
.idea
add.py
demo.py
inverse_element.py
multiply.py
readme.md
sub.py
__pycache__
```

# 2 各文件及其内部函数说明如下：

demo.m：

​	主程序。

add.py：

​	def add(P, Q)：椭圆曲线上的有理点的加法，return P+Q

inverse_element.py：

​	def inverse_element(e, $φ\_n$)：计算e在mod $φ\_n$意义下的逆元素

multiply.py：

​	def multiply(k, G)：椭圆曲线上的有理点的乘法，return k*G

sub.py：

​	def sub(P, Q)：解密时需要用到的减法。