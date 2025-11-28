a = " АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
#нахождение d
def get_d(e, phi):
    x = 1 + phi
    k = 1
    while x % e != 0:
        x = (x + phi) % e
        k += 1
    return (k*phi + 1) // e
#функция шифровки
def shifr(m, e, n):
    return m ** e % n
#функция расшифровки
def rasshifr(c, d, n):
    return c ** d % n
#хэш функция
def hash_func(s, n):
    h = 1
    for i in range(len(s)):
        m = a.index(s[i])
        h = (h + m) ** 2 % n
    return h
#функция проверки подписи
def proverka(h, podpis, e, n):
    if h == shifr(podpis, e, n):
        return True
    return False
p = 17
q = 11
n = p * q
phi = (p - 1) * (q - 1)
e = 7
d = get_d(e, phi)
print("Открытые ключи:", "e =", e, "n =", n)
print("Закрытые ключи:", "d =", d, "n =", n)
m = "ИВАНОВ"
h = hash_func(m, n)
podpis = rasshifr(h, d, n)
print("Подпись сообщения:", podpis)
x = int(input("Введите предпологаемую подпись для проверки: "))
if proverka(h, x, e, n):
    print("Подпись правильная")
else:
    print("Подпись неправильная")
