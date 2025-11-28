s1 = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
s2 = "აბგდევზთიკლმნოპჟრსტუფქღყშჩცძწჭხჯჰ"
def code(m):
    answer = ""
    for i in m:
        answer += s2[s1.index(i)]
    return answer
def decode(c):
    answer = ""
    for i in c:
         answer += s1[s2.index(i)]
    return answer
m = input("Введите строку: ")
c = code(m)
print(c)
print(decode(c))
    
