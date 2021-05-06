from add import add


def multiply(k, G):
    n = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141
    k %= n
    if k == 0:
        return [0, 0]
    elif k == 1:
        return G
    elif k == 2:
        return add(G, G)
    else:
        if k % 2 == 0:
            result_half = multiply(k // 2, G)
            return add(result_half, result_half)
        else:
            result_half = multiply(k // 2, G)
            return add(add(result_half, result_half), G)
