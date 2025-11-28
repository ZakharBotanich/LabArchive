from scipy.io import wavfile
import random as rnd
import matplotlib.pyplot as plt
import numpy as np

#seed для модуля random для генерации одного и того PSP определенной длины
rnd.seed("Иванов")

def StegAudio():
    
    #считывание частоты дискретизации и списка амплитуд
    rate, data = wavfile.read('B.wav','r')
    
    #количество отчетов контейнера
    a = len(data)

    #количество каналов
    b = len(data[0])

    #считывание сообщения и преобразование в двоичный вид
    msg_file = open('A.txt', 'r', encoding='utf-8')
    msg = msg_file.readline()
    print(len(msg))
    bin_msg = ""
    for i in msg:
        bits = bin(ord(i))[2:]
        bits = (16 - len(bits)) * '0' + bits
        bin_msg += bits

    #длина сообщений
    m = len(msg)

    #количество бит на символ
    n = 16

    #закрытие файла A.txt
    msg_file.close()
    
    #количество отчетов контейнера на бит сообщения
    N = a//(m*n)
    if N == 0:
        print("Недостаточно большой контейнер")
        return
    #ПСП длиной N и построоение графика PSP
    psp = PSP(N)
    plt.plot(list(range(N)), psp)
    plt.show()
    
    #получние изменных амплитуд
    Stega = ST(bin_msg, psp, data.copy(), N)
    
    #запись в стегоконтейнер
    wavfile.write("C.wav", rate, Stega)
    DeST(m, n, psp, data, N)
    
#получение псевдослучайной последовательности длиной n
def PSP(n):
    a = []
    for i in range(n):
        a.append(rnd.choice([1,-1]))
    return a

#внедрение сообщения в список амплитуд контейнера
def ST(bin_msg, psp, data, N):
    for i in range(len(bin_msg) * N):
        #изменение определенной амплитуды взависимости от текущего бита и psp
        if bin_msg[i//N] == '0':
            k = -psp[i%N]
        else:
            k = psp[i%N]
        data[i][0] = data[i][0] + np.int16(k)
    return data

#извелечнеие сообщения из стегоконтейнера
def DeST(m, n, psp, data, N):
    rate, stega = wavfile.read('C.wav','r')
    msg = ""
    bit = ""
    for i in range(m*n):
        x = stega[N*i][0]
        y = data[N*i][0]
        bit_psp = x-y
        if psp[0] == 1:
            if bit_psp < 0:
                bit += "0"
            else:
                bit += "1"
        else:
            if bit_psp < 0:
                bit += "1"
            else:
                bit += "0"
        if len(bit) == n :
            msg += chr(to_10(bit))
            bit = ""
    print(msg)

#перевод числа из двочиной системы в десятичную
def to_10(a):
    answer = 0
    for i in range(len(a)):
        if a[i] == '1':
            answer += 2 ** (len(a) - i - 1)
    return answer

StegAudio() 
