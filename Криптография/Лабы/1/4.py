from random import shuffle
s = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
def generate_key():
    key = {}
    lst = []
    for i in s:
        for j in s:
            key[i+j] = ""
            for k in s:
                lst.append(i+j+k)
    shuffle(lst)
    index = 0
    for i in key:
        key[i] = lst[index]
        index += 1
    return key
def code(m, key):
    m += "ъ" * (len(m) % 2)
    answer = ""
    for i in range(0, len(m), 2):
        answer += key[m[i] + m[i+1]]
    return answer
def decode(c, key):
    answer = ""
    for i in range(0, len(c), 3):
        w = c[i] + c[i+1] + c[i+2]
        for j in key:
            if key[j] == w:
                answer += j
    if answer[-1] == "ъ":
        return answer[:-1]
    return answer
    
key = generate_key()
m = input()
c = code(m, key)
print(c)
print(decode(c, key))
