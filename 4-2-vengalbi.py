import RPi.GPIO as gp
import time
gp.setmode(gp.BCM)
gp.setwarnings(False)

gp.setup([6, 12, 5, 0, 1, 7, 11, 8], gp.OUT)
dac = [6, 12, 5, 0, 1, 7, 11, 8]

def ddouble(n):
    num_str = bin(n)[2:]
    num = list(map(int, num_str))
    num = num[::-1]
    for i in range(7, len(num)-1, -1):
        num.append(0)
    return num

t = float(input())

try:
    while True:
        for i in range(256):
            gp.output(dac, ddouble(i))
            time.sleep(t/512)
            gp.output(dac, 0)
        for i in range(255, -1, -1):
            gp.output(dac, ddouble(i))
            time.sleep(t/512)  
            gp.output(dac, 0)
               
finally:
    gp.output(dac, 0)
    gp.cleanup()