import matplotlib.pyplot as plt
import numpy as np

## for 10 cm 
x1 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
y1 = [4,0,0,0,0,0,0,0,0,0]
y1 = [element / 10000 for element in y1]
xsec_prod = [2.428e-08,1.902e-09,3.969e-10,1.229e-10,4.592e-11,1.984e-11 ,9.366e-12,4.775e-12,2.175e-12,1.328e-12]
xsec_prod = [element * 1e-7 for element in xsec_prod]

 # https://lhcb.web.cern.ch/speakersbureau/html/PerformanceNumbers.html
L = 5.7e15 # LHCb run 2 integrated lumniosity
N1 = L * np.multiply(y1,xsec_prod) 
plt.plot(x1, N1,marker='x', linestyle='dashdot', color='r', label='10 cm')


## for 100 cm 
x2 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
y2 = [147,97,60,52,26,28,19,14,10,4]
y2 = [element / 10000 for element in y2]
N2 = L * np.multiply(y2,xsec_prod) 
plt.plot(x2, N2,marker='x', linestyle='dashdot', color='b', label='100 cm')

## for 1000 cm 
x3 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
y3 = [106,94,70,107,79,50,80,40,56,54]
y3 = [element / 10000 for element in y3]

N3 = L * np.multiply(y3,xsec_prod) 
plt.plot(x3, N3,marker='x', linestyle='dashdot', color='g', label='1000 cm')


x4 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
y4 = [15,14,14,24,12,12,20,7,14,14]
y4 = [element / 10000 for element in y4]

N4 = L * np.multiply(y4,xsec_prod) 
plt.plot(x4, N4,marker='x', linestyle='dashdot', color='y', label='10000 cm')


plt.title('Number of Events between T1-T3 vs Mass')
plt.xlabel('Mass (GeV)')
plt.ylabel('Number of Events')
plt.legend()
plt.savefig('nEvent_T1-T2.pdf')  
plt.show()
