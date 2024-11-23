def div(a, b):
    q = a // b
    r = a % b
    return q, r


def finput(*args):
    input(" ".join(map(str, args)))


def pgcd(a, b):
    r = -1
    l = []
    while r != 0:
        q, r = div(a, b)
        finput(a, "=", b, "x", q, "+", r)
        l.append([a, b, q, r])
        a, b = b, r
    finput("=", a)
    l.pop(-1)
    return l


def aubv(a, b, l):
    a, b, v, d = l[0]
    u = 1
    finput(a, "x", u, "-", b, "x", v, "=", a * u - b * v)
    l.pop(0)
    for i in l:
        if i[3] == a:
            a = i[0]
            v += u * i[2]
        elif i[3] == b:
            b = i[0]
            u += v * i[2]
        finput(a, "x", u, "-", b, "x", v, "=", a * u - b * v)
    if a > b:
        finput(str(u) + "a - " + str(v) + "b")
    else:
        finput("-" + str(v) + "a + " + str(u) + "b")


def main():
    a = int(input("Premier nombre : "))
    b = int(input("Deuxième nombre : "))
    a, b = max(a, b), min(a, b)
    l = pgcd(a, b)[::-1]
    if input("Avec la forme au + bv ? ").lower() in ("y", "yes", "1"):
        aubv(a, b, l)
    print()


while True:
    main()
