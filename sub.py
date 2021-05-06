from add import add


def sub(P, Q):
    Q[1] = -Q[1]
    return add(P, Q)
