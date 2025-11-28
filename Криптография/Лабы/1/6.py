def ceasar(s, rot):
    answer = ""
    for i in s:
        if i.isalpha():
            if i.islower():
                answer += chr((ord(i) - 97 + rot)%26 + 97)
            else:
                answer += chr((ord(i) - 65 + rot)%26 + 65)
        else:
            answer += i
    return answer
s = input("Введите строку: ")
codes = []
for i in range(1, 27):
    a = ceasar(s, i)
    print("ROT" + str(i) + " " + a)
    codes.append(a)
k = int(input("Введите правильный ключ: "))
print("Расшифрока: " + codes[k - 1])
