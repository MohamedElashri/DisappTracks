
# This script is plotting number of Events Produced that pass cuts vs Mass for low taus (10-100-1000 cm)
import matplotlib.pyplot as plt
import numpy as np

## for 10000 cm 
x1 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
y1 = [188,160,214,238,198,203,210,205,173,156]
y1 = [element / 10000 for element in y1]
xsec_prod = [2.428e-08,1.902e-09,3.969e-10,1.229e-10,4.592e-11,1.984e-11 ,9.366e-12,4.775e-12,2.175e-12,1.328e-12]
xsec_prod = [element * 1e-3 for element in xsec_prod]

 # https://lhcb.web.cern.ch/speakersbureau/html/PerformanceNumbers.html
L = 5.7e15 # LHCb run 2 integrated lumniosity
N1 = L * np.multiply(y1,xsec_prod) 
plt.plot(x1, N1,marker='x', linestyle='dashdot', color='r', label='10000 cm')


## for 100000 cm 
x2 = [100,200, 300, 400, 500, 600, 700, 800, 900, 1000]
y2 = [8,16,20,24,16,28,32,26,24,12]
y2 = [element / 10000 for element in y2]
N2 = L * np.multiply(y2,xsec_prod) 
plt.plot(x2, N2,marker='x', linestyle='dashdot', color='b', label='100000 cm')

## for 1000000 cm 
x3 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
y3 = [1,4,2,1,4,2,1,4,2,2]
y3 = [element / 10000 for element in y3]

N3 = L * np.multiply(y3,xsec_prod) 
plt.plot(x3, N3,marker='x', linestyle='dashdot', color='g', label='1000000 cm')


plt.yscale('log')
plt.title('Number of Events produced inside LHCb Tracker (high) vs Mass')
plt.xlabel('Mass (GeV)')
plt.ylabel('Number of Events')
plt.legend()
plt.savefig('nEvent-high_LHCb.pdf')  
plt.show()
