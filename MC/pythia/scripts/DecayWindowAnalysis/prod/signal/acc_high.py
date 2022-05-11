
# This script is plotting number of Events Produced that pass cuts vs Mass for low taus (10-100-1000 cm)
import matplotlib.pyplot as plt
import numpy as np

## for 10000 cm 
x1 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
y1 = [188,160,214,238,198,203,210,205,173,156]
y1 = [element / 10000 for element in y1]
plt.plot(x1, y1,marker='x', linestyle='dashdot', color='g', label='10000 cm')

## for 100000 cm 
x2 = [100,200, 300, 400, 500, 600, 700, 800, 900, 1000]
y2 = [8,16,20,24,16,28,32,26,24,12]
y2 = [element / 10000 for element in y2]
plt.plot(x2, y2,marker='x', linestyle='dashdot', color='m', label='100000 cm')

## for 1000000 cm 
x3 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
y3 = [1,4,2,1,4,2,1,4,2,2]
y3 = [element / 10000 for element in y3]

plt.plot(x3, y3,marker='x', linestyle='dashdot', color='c', label='1000000 cm')


plt.yscale('log')
plt.title('LHCb Acceptance (high) vs Mass')
plt.xlabel('Mass (GeV)')
plt.ylabel('Acceptance')
plt.legend()
plt.savefig('acc_high_LHCb.pdf')  
plt.show()
