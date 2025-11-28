from random import randint
alpha = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
def generate_key(n):
    key = ""
    for i in range(n):
        key += alpha[randint(0,32)]
    return key
def code(m, key):
    c = ""
    for i in range(len(m)):
        i1 = alpha.index(m[i])
        i2 = alpha.index(key[i])
        i3 = (i1 + i2) % 33
        c += alpha[i3]
    return c
def decode(c, key):
    m = ""
    for i in range(len(c)):
        i2 = alpha.index(key[i])
        i3 = alpha.index(c[i])
        m += alpha[(i3 - i2) % 33]
    return m
m = input("Введите строку: ")
key = generate_key(len(m))
c = code(m, key)
print("Ключ:", key)
print("Зашифрованное сообщение:", c)
print("Расшифрованное сообщение:", decode(c, key))
