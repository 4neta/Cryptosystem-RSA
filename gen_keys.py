import random

def is_prime(p):
    for i in range (2, int(p/2)):
        if p%i == 0:
            return False
    return True

def gcd(a, b):
    while a != b:
        if b==0:
            break
        temp = b
        b = a % b
        a = temp
    return a

def find_e(numb):
    while True:
        e = random.randrange(3, numb, 2) # n should be odd
        if gcd(e, numb) != 1: # checking if e and n are relatively prime
            return e

def find_mmi(a, b): # mmi - modular multiplicative inverse (of a mod b)
    # we are sure that inverse exists
    u = 1
    w = a
    x = 0
    z = b
    while w != 0:
        if w < z:
            (u, x) = (x, u)
            (w, z) = (z, w)
        q = int(w/z)
        u -= q*x
        w -= q*z
    if x < 0:
        x += b
    return x

print('-- RSA Algorithm \\ GENERATING KEYS --')
print("Choose two big prime numbers: ")

p = int(input(" p = "))
q = int(input(" q = "))

if is_prime(p) == True and is_prime(q) == True:
    euler = (p - 1) * (q - 1)
    n = p * q
    e = find_e(n)
    d = find_mmi(e, euler)
    while e == d or d == 1:
        e = find_e(n)
        d = find_mmi(e, euler)

    print("Your public key: (%d,%d)" % (e, n))
    print("Your private key: (%d,%d)" % (d, n))

else:
    print("Sorry, p or q are not a prime numbers.")

input()