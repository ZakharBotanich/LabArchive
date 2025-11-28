#функция преобразования
def f(r, x):
    s = ""
    a = 0
    #сложение по модулю 2^32
    for i in range(31, -1, -1):
        p = a + int(r[i]) + int(x[i])
        s += str(p%2)
        a = p // 2
    s = s[::-1]
    #подстановка в блок
    block = [[1, 13, 4, 6, 7, 5, 14, 4],[15,11, 11, 12, 13, 8, 11, 10],[13, 4, 10, 7, 10, 1, 4, 9],[0, 1, 0, 1, 1, 13, 12, 2],[5, 3, 7, 5, 0, 10, 6, 13],[7, 15, 2, 15, 8, 3, 13, 8],[10, 5, 1, 13, 9, 4, 15, 0],[4, 9, 13, 8, 15, 2, 10, 4],[9, 0, 3, 4, 14, 14, 2, 6],[2, 10, 6, 10, 4, 15, 3, 11],[3, 14, 8, 9, 6, 12, 8, 1],[14, 7, 5, 14, 12, 7, 1, 12],[6, 6, 9, 0, 11, 6, 0, 7],[11, 8, 12, 3, 2, 0, 7, 15],[8, 2, 15, 11, 5, 9, 5, 5],[12, 12, 14, 2, 3, 11, 9, 3]]
    otvet = ""
    for i in range(8):
        stolbik = 8 * int(s[4*i]) + 4 * int(s[4*i + 1]) + 2 * int(s[4*i+2])+int(s[4*i+3])
        chislo = bin(block[stolbik][i])[2:]
        otvet += "0" * (4 - len(chislo)) + chislo
    pechat(otvet, "")
    #сдвиг на 11 влево
    otvet = otvet[11:] + otvet[:11]
    return otvet
#функция преобразования сторки в битовую строку
def v_biti(s):
    bits = ""
    for i in s:
        bits += bin(ord(i) - ord("А") + 192)[2:]
    return bits
#функция xorа двух строк
def xor(a, b):
    c = ""
    for i in range(len(a)):
        c += str((int(a[i]) + int(b[i])) % 2)
    return c
#функция печати битовой строки в блоки по 4 бита
def pechat(bit, stroka):
    print(stroka, end = "")
    for i in range(len(bit)):
        print(bit[i], end = "")
        if (i + 1) % 4 == 0:
            print(" ", end = "")
    print()
bt = v_biti("ИвановИ")
l = bt[:32]
r = bt[32:]
x = v_biti("Иван")
preobr = f(r, x)
pechat(preobr,"f(r, x) = ")
r1 = xor(preobr, l)
l1 = r
pechat(l,"L0 = ")
pechat(r,"R0 = ")
pechat(l1,"L1 = ")
pechat(r1,"R1 = ")
