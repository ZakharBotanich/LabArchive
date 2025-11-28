from PIL import Image, ImageDraw
import random
random.seed("Иванов")
def st():
    #открытие bmp файла
    image = Image.open("A.bmp")
    draw = ImageDraw.Draw(image)

    #ширина, высота и значения пискелей
    width = image.size[0]
    height = image.size[1]
    pix = image.load()
    
    #сообщение в двоичном виде
    msg = "Иванов Иван Иванович"
    bin_msg = ""
    for i in msg:
        bits = bin(ord(i))[2:]
        bits = (16 - len(bits)) * '0' + bits
        bin_msg += bits
        
    inter = get_inter(len(bin_msg))
    
    #изменение пикселей для шифрованиях в них сообщения
    sm = inter[0]
    inter_index = 0
    for x in range(width):
        for y in range(height):
            red = pix[x,y][0]
            green = pix[x,y][1]
            blue = pix[x,y][2]
            
            #проверка прохождения интервала между битами сообщения 
            if x * height + y == sm:
                #замена наименее значемого бита на бит сообщения
                blue -= blue%2 - int(bin_msg[inter_index])
                inter_index += 1
                if inter_index != len(inter):
                    sm += inter[inter_index]
            draw.point((x,y), (red, green, blue))
    image.save("B.bmp", "BMP")
    dest(inter)
    
#генерация интервалов
def get_inter(n):
    a = []
    for i in range(n):
        a.append(random.randint(1, 100))
    return a
def dest(inter):
    image = Image.open("B.bmp")
    pix = image.load()
    width = image.size[0]
    height = image.size[1]
    bit = ""
    msg = ""
    sm = 0
    for i in inter:
        sm += i
        x = sm // height
        y = sm % height
        blue = pix[x,y][2]
        bit += str(blue%2)
        if len(bit) == 16:
            msg += chr(to_10(bit))
            bit = ""
    file = open("A.txt", "w")
    file.write(msg)
    file.close()
#перевод числа из двочиной системы в десятичную
def to_10(a):
    answer = 0
    for i in range(len(a)):
        if a[i] == '1':
            answer += 2 ** (len(a) - i - 1)
    return answer
st()

