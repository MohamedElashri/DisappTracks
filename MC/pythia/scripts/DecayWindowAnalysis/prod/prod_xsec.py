import matplotlib.pyplot as plt
import numpy as np
## for 10 cm 
x1 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
y1 = [6700,5280,4471,3771,3510,2967,2650,2333,2178,1970]
xsec_prod = [2.428e-08,1.902e-09,3.969e-10,1.229e-10,4.592e-11,1.984e-11 ,9.366e-12,4.775e-12,2.175e-12,1.328e-12]
#xsec_prod = [element * 1e-7 for element in xsec_prod]
plt.plot(x1, xsec_prod,marker='o', linestyle='dashdot', color='b', label='Cross Section')


plt.title('Production Cross Section vs Mass')
plt.xlabel('Mass (GeV)')
plt.ylabel('Cross Section (mb)')
plt.legend()
plt.savefig('prod_xsec.pdf')  
plt.show()
