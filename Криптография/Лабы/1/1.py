#функция зашифроки
def code(m, key):
    length = len(m)
    crypto = []
    for i in range(length):
        crypto.append(m[(i + key) % length])
        index = -1 - key - ((i+key) % length)
        if index < -length:
            index += length
        crypto.append(m[index])
    return ''.join(crypto)

#функция расшифроки
def decode(c, key):
    length = len(c) // 2
    answer = ['']*length
    for i in range(length):
        answer[(key + i) % length] = c[2*i]
    return ''.join(answer)

m = input("Введите строку: ")
key = int(input("Введите ключ: "))
c = code(m, key)
print(c)
print(decode(c, key))
