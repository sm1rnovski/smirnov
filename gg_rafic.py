import numpy as np
import matplotlib.pyplot as plt

#with open("settings.txt", "r") as set:
#    tmp = [float(i) for i in set.read().split("\n")]

data_ar = np.loadtxt("data.txt", dtype = int)
volt = []
for i in range(0, len(data_ar)):
    volt.append(data_ar[i]*3.3/256)

time = []
t_step = 0.03
for i in range(0, len(data_ar)):
    time.append(i*t_step)

fig, ax = plt.subplots(figsize=(16,10), dpi = 400)
ax.set_ylim(0, 3.3)
ax.set_xlim(0, 8)
ax.plot(time, volt, '-o',linewidth = 2, markersize = 5, markevery = 5)
#plt.scatter(time[::10], volt[::10], s = 52, c = "red")
plt.xlabel("Время, с")
plt.ylabel("Напряжение, В")
plt.title("Процесс заряда и разряда конденсатора в RC-цепи")
plt.grid(which = 'major', linewidth = 1.6)
plt.grid(which = 'minor', linewidth = 0.4)
plt.minorticks_on()
plt.legend(["V(t)"])
plt.text(0.7, 3.2, 'время зарядки: 7,46', fontsize = 8)
plt.text(0.7, 3.09, 'время разрядки: 3,71', fontsize = 8)

fig.savefig("test.png")
plt.show()