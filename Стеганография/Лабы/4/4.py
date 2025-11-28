from PIL import Image, ImageDraw
def st():
    #открытие bmp файла
    image = Image.open("A.bmp")
    draw = ImageDraw.Draw(image)

    #ширина, высота и значения пискелей
    width = image.size[0]
    height = image.size[1]
    pix = image.load()

    #преобразование текстового сообщения в двоичный вид
    msg = "Иванов Иван Иванович"
    bin_msg = ""
    for i in msg:
        bits = bin(ord(i))[2:]
        bits = (16 - len(bits)) * '0' + bits
        bin_msg += bits
    
    #изменение пикселей для скрытия в них сообщения
    for x in range(width):
        for y in range(height):
            red = pix[x,y][0]
            green = pix[x,y][1]
            blue = pix[x,y][2]
            if x*height + y < len(bin_msg):
                
                #замена наименее значемого бита на бит сообщения
                blue -= blue%2 - int(bin_msg[x*height + y])
            draw.point((x,y), (red, green, blue))
    image.save("B.bmp", "BMP")
def dest():
    image = Image.open("B.bmp")
    pix = image.load()

    width = image.size[0]
    height = image.size[1]
    bit = ""
    msg = ""
    for x in range(width):
        for y in range(height):
            if x*height + y >= 480:
                #конец извлечения сообщения
                break
            blue = pix[x,y][2]
            
            #получение бита сообщения
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
dest()
