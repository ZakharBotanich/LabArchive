s1 = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
s2 = "აბგდევზთიკლმნოპჟრსტუფქღყშჩცძწჭხჯჰ"
def code(m):
    answer = ""
    for i in range(len(m)):
        forward = 3
        if (i + 1) % 2 == 0:
            forward += 1
        if (i + 1) % 3 == 0:
            forward += 2
        if (i + 1) % 5 == 0:
            forward *= 2
        answer += s2[(s1.index(m[i])+forward)%33]
    return answer
def decode(c):
    answer = ""
    for i in range(len(c)):
        backward = 3
        if (i + 1) % 2 == 0:
            backward += 1
        if (i + 1) % 3 == 0:
            backward += 2
        if (i + 1) % 5 == 0:
            backward *= 2
        answer += s1[(s2.index(c[i])-backward)%33]
    return answer
m = input("Введите строку: ")
c = code(m)
print(c)
print(decode(c))
    
