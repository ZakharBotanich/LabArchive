from random import choice
lst = [5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73,
79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]
def get_e(phi):
    e = choice(lst)
    while n % e == 0:
        e = choice(lst)
    return e
def get_d(e, phi):
    x = 1 + phi
    k = 1
    while x % e != 0:
        x = (x + phi) % e
        k += 1
    return (k*phi + 1) // e
def code(m, e, n):
    c = ""
    for i in m:
        c += chr(ord(i) ** e % n)
    return c
def decode(c, d, n):
    m = ""
    for i in c:
        m += chr(ord(i) ** d % n)
    return m
#этап формирования системы RSA
p = choice(lst)
q = choice(lst)
while q == p:
    q = choice(lst)
n = p * q
phi = (p - 1) * (q - 1)
e = get_e(phi)
d = get_d(e, phi)
print("Открытые ключи:", "e =", e, "n =", n)
print("Закрытые ключи:", "d =", d, "p =", p, "q =", q, "phi =", phi)
m = input("Введите ссобщение M: ")
c = code(m, e, n)
print("Зашифрованное сообщение", c)
print("Расшифрованное сообщение", decode(c, d, n))
