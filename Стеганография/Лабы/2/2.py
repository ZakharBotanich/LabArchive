#перевод одного символа в двоичный вид
def to_bites(s):
    bt = ""
    for i in s:
        if ord(i) >= ord("А"):
            bt += bin(ord(i) - ord("А") + 192)[2:]
        else:
            a = bin(ord(i))[2:]
            bt += (8 - len(a)) * '0' + a
    return bt

#перевод символа из двоичного вида
def to_char(s):
    if len(s) < 8 or s == '0' * 8:
        return ''
    a = to_10(s)
    if a >= 192:
        return chr(a + ord("А") - 192)
    return chr(a)

#перевод числа из двоичной в десятичную
def to_10(a):
    answer = 0
    for i in range(len(a)):
        if a[i] == '1':
            answer += 2 ** (len(a) - i - 1)
    return answer

#функция встраивания сообщения в стегоконтейнер
def st():
    #файл сообщение и считывание сообщения
    file_msg = open("A.txt", "r", encoding='utf-8')
    msg = ''.join(file_msg.readlines())

    #файл контейнер и считывание текста контейнера
    file_con = open("B.txt", "r", encoding='utf-8')
    con = ''.join(file_con.readlines())

    #файл стегоконтейнер
    file_stg = open("C.txt", "w", encoding='utf-8')

    #количество пробелов в контейнере и количество битов сообщения
    spaces = con.count(" ")
    bits = 8*len(msg)
    print("Количество пробелов в контейнере:", spaces)
    print("Количество бит в сообщении:", bits)

    #проверка достаточности пробелов для скрытия всех битов
    if spaces < bits:
        print("Количество пробелов недостаточно")
        return
    
    #конечная стего-строка
    result = ""

    #перевод первого символа в двоичное число и индекс текущего скрываемого бита в символе
    bit = to_bites(msg[0])
    bit_index = 0
    
    #индекс записываемого символа
    now_index = 0
    for i in con:
        #запись не пробела в result стего контейнера или запись обычного пробела если все сообщения уже было записано
        if i != " " or now_index == len(msg):
            result += i
            continue
        
        #запись одного бита
        if bit[bit_index] == "0":  
            result += " " + " "
        else:
            result += " "
        bit_index += 1

        #переход на следующий символ, если старый уже записан полностью
        if bit_index == 8:
            bit_index = 0
            now_index += 1
            if now_index != len(msg):
                #получение следующего символа в виде битовой строки
                bit = to_bites(msg[now_index])
    
    #запись результата
    file_stg.write(result)
    
    #закрытие файлов
    file_msg.close()
    file_con.close()
    file_stg.close()
    print("Результат записан в стегоконтейнер")

#функция извлечения сообщения из стегоконтейнера
def dest(len_msg):
    #открытие стегоконтейнера и считывание содержаемого в нем
    file_stg = open("C.txt", "r", encoding='utf-8')
    stg = ''.join(file_stg.readlines())
    #переменная исходного сообщения
    msg = ""

    #переманная записи символа в виде битовой строки
    char = ""

    i = 0
    
    #цикл до конца стегоконтейнера и до получения всего сообщения
    while i < len(stg) and len(msg) < len_msg:
        #цикл преобразования пробелов в символы
        if stg[i] != " ":
            i += 1
            continue
        if stg[i] == " ":
            if i != len(stg) - 1 and stg[i + 1] == " ":
                i += 1
                char += "0"
            else:
                char += "1"
    
        #запись расшифрованного символа
        if len(char) == 8:
            msg += to_char(char)
            char = ""
        i += 1
    return msg

st()
print("Исходное сообщение:", dest(10))
