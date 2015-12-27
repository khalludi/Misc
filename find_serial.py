import serial

s = serial.Serial("/dev/ttyAMA0", baudrate=38400, timeout=1)
hexd = list("0123456789ABCDEF")

def getSerial():

    inc = '0x00'
    for x in range(0, 10):
        s.write(''.join(map(chr, [0x56, inc, 0x11, 0x00])))
        inc = hex(int(inc, 16) + 1)
        if not s.read(100).equals(''):
            print inc

getSerial()