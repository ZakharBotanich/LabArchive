s = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяабвгдеёжзийклмнопрстуфхцчшщъыьэюя"
def code(m):
    key = "докторливси"
    answer = ""
    for i in range(len(m)):
        j = i % len(key)
        i1 = s.index(m[i])
        i2 = s.index(key[j])
        dist = abs(i2 - i1)
        if i1 > i2:
            answer += s[(i2 - dist) % 33]
        else:
            answer += s[(i2 + dist) % 33]
    return answer
m = input("Введите строку: ")
c = code(m)
print(c)
print(code(c))
