from random import randint
def xor_code(m, key):
    c = ""
    for i in range(len(m)):
        c += str(int(m[i]) ^ int(key[i]))
    return c
def generate_key(n):
    key = ""
    for i in range(n):
        key += str(randint(0, 1))
    return key
m = input("Введите битовую строку: ")
key = generate_key(len(m))
c = xor_code(m, key)
print("Ключ:", key)
print("Зашифрованное сообщение:", c)
print("Расшифрованное сообщение:", xor_code(c, key))
