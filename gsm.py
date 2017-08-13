# -*- coding: utf8 -*-
from time import sleep
import serial

gsm = serial.Serial('/dev/ttyS1', 115200, timeout=60)
gsm.write('+++')
sleep(1)
def readuntil():
    lines = []
    while True:
        data = gsm.readline().strip()
        if len(data) == 0:
            continue
        lines.append(data)
        if data == 'OK' or data == 'ERROR':
            sleep(.2)
            return lines

# AT+GSN
# 861445031805950
def getIMEI():
    gsm.write('AT+GSN\r\n')
    xs = readuntil()
    if xs[-1] == 'OK':
        return xs[1]
    else:
        print xs
        return None


def doCNETSCAN():
    gsm.write('AT+CNETSCAN\r\n')
    xs = readuntil()
    if xs[-1] == 'OK':
        return xs[1:-1]
    else:
        print xs
        return None

# +CENG: 0,"0096,28,00,466,05,43,1960,08,05,0462,255,-85,69,69,x,x,x,x,x,x,x"
# +CENG: 1,"0089,17,42,195e,466,05,0462,33,33"
# +CENG: 2,"0085,16,01,1973,466,05,0462,29,29"
def getCENG():
    gsm.write('AT+CENG?\r\n')
    xs = readuntil()
    if xs[-1] == 'OK':
        return xs[2:-1]
    else:
        print xs
        return None


gsm.write('AT+CENG=4,1\r\n')
readuntil()
