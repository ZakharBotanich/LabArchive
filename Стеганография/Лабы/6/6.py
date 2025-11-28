from scipy.fftpack import dct
from PIL import Image, ImageDraw
from random import randint
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
    blue = []
    for x in range(width):
        row = []
        for y in range(height):
            row.append(pix[x,y][2])
        blue.append(row)
    #ДКП матрицы значений синего цвета пикселей
    blue = dct(blue)
    a = width // 8
    b = height // 8
    P = 2000
    
    #координаты коэффициентов ДКП
    u1 = 3
    v1 = 4
    u2 = 4
    v2 = 3
    for i in range(len(bin_msg)):
        x = 8*(i%a)
        y = 8*(i//a)

        if bin_msg[i] == "1":
            #если единица, то ДКП 1го пикселя должен быть меньше ДКП 2го пикселя
            while abs(blue[x+u1][y+v1]) - abs(blue[x+u2][y+v2]) >= P - 1200:
                blue[x+u1][y+v1] -= 10*get_znak(blue[x+u1][y+v1])
                blue[x+u2][y+v2] += 10*get_znak(blue[x+u2][y+v2])
        else:
            #если единица, то ДКП 1го пикселя должен быть больше ДКП 2го пикселя
            while abs(blue[x+u1][y+v1]) - abs(blue[x+u2][y+v2]) < P + 1200:
                blue[x+u1][y+v1] += 10*get_znak(blue[x+u1][y+v1])
                blue[x+u2][y+v2] -= 10*get_znak(blue[x+u2][y+v2])

    blue = dct(blue, type = 3)
    
    for x in range(width):
        for y in range(height):
            r = pix[x,y][0]
            g = pix[x,y][1]
            b = round(blue[x][y] / (2*len(blue[0])))
            draw.point((x,y), (r, g, b))
    image.save("B.bmp", "BMP")
def get_znak(x):
    if x <= 0:
        return -1
    return 1
def dest():
    print()
    #открытие bmp файла
    image = Image.open("B.bmp")
    draw = ImageDraw.Draw(image)

    #ширина, высота и значения пискелей
    width = image.size[0]
    height = image.size[1]
    pix = image.load()
    bit = ""
    msg = ""
    a = width // 8
    b = height // 8
    blue = []
    for x in range(width):
        row = []
        for y in range(height):
            row.append(pix[x,y][2])
        blue.append(row)
    blue = dct(blue)
    for i in range(b):
        for j in range(a):
            if i*a+j < 480:
                blue1 = blue[8*j+3][8*i+4]
                blue2 = blue[8*j+4][8*i+3]
                #сравнения синих градиентов 2 пикселей для нахождения одного бита
                if abs(blue1) - abs(blue2) < 1300:
                    bit += "1"
                else:
                    bit += "0"
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
dest()
