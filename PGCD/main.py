def div(a, b):
    q = a // b
    r = a % b
    return q, r


def pgcd(a, b):
    r = -1
    l = []
    while r != 0:
        q, r = div(a, b)
        print(a, "=", b, "x", q, "+", r)
        l.append([a, b, q, r])
        a, b = b, r
    print("=", a)
    return l


def aubv(a, b):
    a, b = max(a, b), min(a, b)
    l = pgcd(a, b)[::-1]
    if input("Avec la forme au + bv ? (y/n) : ").lower() != "y":
        return
    l.pop(0)
    a, b, v, d = l[0]
    u = 1
    print(a, "x", u, "-", b, "x", v, "=", a * u - b * v)
    l.pop(0)
    for i in l:
        if i[3] == a:
            a = i[0]
            v += u * i[2]
        elif i[3] == b:
            b = i[0]
            u += v * i[2]
        print(a, "x", u, "-", b, "x", v, "=", a * u - b * v)


while True:
    a = int(input("Premier nombre : "))
    b = int(input("Deuxième nombre : "))
    aubv(a, b)
