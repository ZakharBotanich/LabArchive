#алфавит
a = " АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
#вычисление е
def get_e(d, phi):
    x = 1 + phi
    k = 1
    while x % d != 0:
        x = (x + phi) % d
        k += 1
    return (k*phi + 1) // d
#шифровка
def shifr(m, e, n):
    c = ""
    for i in m:
        c += a[a.index(i) ** e % n]
    return c
#расшифровка
def rasshifr(c, d, n):
    m = ""
    for i in c:
        m += a[a.index(i) ** d % n]
    return m
#ФИО - Иванов Иван Иванович
m = "ИИИ"
p = 11
q = 3
n = p * q
phi = (p - 1) * (q - 1)
d = 7
e = get_e(d, phi)
print("Открытые ключи:", "e =", e, "n =", n)
print("Закрытые ключи:", "d =", d, "n =", n)
c = shifr(m, e, n)
m1 = rasshifr(c, d, n)
print("Исходное сообщение:", m)
print("Зашифрованное ФИО:", c)
print("Расшифровка:", m1)

