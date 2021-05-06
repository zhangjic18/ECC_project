def euclid(a, b):
    if b == 0:
        return 1, 0
    else:
        k = a // b
        remainder = a % b
        x1, y1 = euclid(b, remainder)
        x, y = y1, x1 - k * y1
    return x, y


def inverse_element(e, φ_n):
    e %= φ_n
    d, x = euclid(e, φ_n)
    d %= φ_n
    return d

