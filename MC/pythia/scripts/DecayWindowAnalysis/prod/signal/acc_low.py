
# This script is plotting number of Events Produced that pass cuts vs Mass for low taus (10-100-1000 cm)
import matplotlib.pyplot as plt
import numpy as np

## for 10 cm 
x1 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
y1 = [6700,5280,4471,3771,3510,2967,2650,2333,2178,1970]
y1 = [element / 10000 for element in y1]

plt.plot(x1, y1,marker='x', linestyle='dashdot', color='r', label='10 cm')


## for 100 cm 
x2 = [100,200, 300, 400, 500, 600, 700, 800, 900, 1000]
y2 = [5478,4771,4167,3653,3432,2947,2628,2339,2196,1974]
y2 = [element / 10000 for element in y2]
plt.plot(x2, y2,marker='x', linestyle='dashdot', color='b', label='100 cm')

## for 1000 cm 
x3 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
y3 = [1495,1501,1485,1472,1525,1313,1262,1212,1077,1096]
y3 = [element / 10000 for element in y3]

plt.plot(x3, y3,marker='x', linestyle='dashdot', color='g', label='1000 cm')


plt.yscale('log')
plt.title('LHCb Acceptance (low) vs Mass')
plt.xlabel('Mass (GeV)')
plt.ylabel('Acceptance')
plt.legend()
plt.savefig('acc_low_LHCb.pdf')  
plt.show()
