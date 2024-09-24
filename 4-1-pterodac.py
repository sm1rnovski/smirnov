import RPi.GPIO as gp
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

try:
    while True:
        n = input("число от 0 до 255: ")
        gp.output(dac, 0)
        if n == 'q':
            break
        else:
            if n.isnumeric() == True:
                n = int(n)
                if (n >= 0) and (n < 256) and (n%1 == 0):
                    num = ddouble(n)
                    gp.output(dac, num)
                    print(str((3.3/256)*n) + ' V')
                else:
                    print('no no no mr. fish')
            else:
                print('no no no mr. fish')
finally:
    gp.output(dac, 0)
    gp.cleanup()