from inverse_element import inverse_element


def add(P, Q):  # R = P+Q
    p = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F
    a = 0

    if (P[0] == Q[0] and P[1] == -Q[1]) or (P[0] == Q[0] and P[1] == Q[1] and P[1] == 0):
        return [0, 0]

    if P[0] == Q[0] and P[1] == Q[1]:
        if (3 * P[0] ** 2 + a) % (2 * P[1]) == 0:
            λ = (3 * P[0] ** 2 + a) // (2 * P[1]) % p
        else:
            λ = (3 * P[0] ** 2 + a) * inverse_element(2 * P[1], p) % p
    else:
        if P[0] == Q[0]:
            return [0, 0]

        if (P[1] - Q[1]) % (P[0] - Q[0]) == 0:
            λ = (P[1] - Q[1]) // (P[0] - Q[0]) % p
        else:
            λ = (P[1] - Q[1]) * inverse_element(P[0] - Q[0], p) % p

    R = [0, 0]
    R[0] = (λ ** 2 - P[0] - Q[0]) % p
    R[1] = (λ * (P[0] - R[0]) - P[1]) % p

    return R
