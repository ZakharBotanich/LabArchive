def xor_code(m, key):
    c = ""
    for i in m:
        c += chr(ord(i) ^ key)
    return c
m = input("Введите строку: ")
key = int(input("Введите ключ: "))
c = xor_code(m, key)
print("Зашифрованное сообщение:", c)
print("Расшифрованное сообщение:", xor_code(c, key))
