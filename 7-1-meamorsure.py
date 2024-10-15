import matplotlib.pyplot as plt
import RPi.GPIO as gp
import time
gp.setmode(gp.BCM)
gp.setwarnings(False)

dac = [6, 12, 5, 0, 1, 7, 11, 8]
leds = [9, 10, 22, 27, 17, 4, 3, 2]
gp.setup(dac, gp.OUT)
gp.setup(leds, gp.OUT)
comp = 24
troyka = 13
gp.setup(comp, gp.OUT)
gp.setup(troyka, gp.OUT, initial=1)

def ddouble(n):
    num_str = bin(n)[2:]
    num = list(map(int, num_str))
    num = num[::-1]
    for i in range(7, len(num)-1, -1):
        num.append(0)
    return num

def acd():
    ww = 0
    for i in range(8):
        step = 2**(7 - i)
        gp.output(dac, ddouble(ww + step))
        time.sleep(0.001)
        volt = gp.input(comp)
        if volt == 0:
            ww += step
    return ww
voltage = []
try:
    start = time.time()
    while time.time() <= start + 7.6:
        voltage.append(acd())
        gp.output(leds, ddouble(acd()))
        print(acd())
    finish = time.time()
    delta_t = (finish - start)/len(voltage)
    s_t = 1/(delta_t)
    step = 1*3.3/256
    stime = [(str(s_t) + " частота дискретизации"), (str(step) + " шаг квантования")]

    voltage_str = [str(item) for item in voltage]
    with open("data.txt", "w") as outfile:
        outfile.write("\n".join(voltage_str))

    with open("settings.txt", "w") as outfile:
        outfile.write("\n".join(stime))

finally:
    null = [0, 0, 0, 0, 0, 0, 0, 0]
    gp.output(leds, null)
    gp.output(dac, null)
    gp.output(comp, 0)
    gp.output(troyka, 0)
    gp.cleanup()

plt.plot(voltage)
plt.show()