def gcd_iter(a, b):
    # Итеративный вариант.
    while b:
        a, b = b, a % b
    return a

def gcd_rec(a, b):
    # Рекурсивный вариант.
    if b:
        return gcd_rec(b, a % b)
    return a

print(gcd_iter(50164, 324), gcd_rec(50164, 324))