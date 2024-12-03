import jetFunctions as j
import spidev
import time
import RPi.GPIO as GPIO

spi = spidev.SpiDev()
try:
    j.initSpiAdc()
    j.initStepMotorGpio()
    volt = [0]*100
    j.stepBackward(400)
    for i in range(100):
        volt[i] = j.getAdc()
        j.stepForward(8)
        time.sleep(0.5)
    j.stepBackward(400)

    volt_str = [str(item) for item in volt]
    with open("/home/b03-405/затопленая струя смирнов/m&m's_70.txt",'w') as outfile:
        outfile.write("\n".join(volt_str))

finally: 
    j.deinitSpiAdc()
    j.deinitStepMotorGpio()
