import matplotlib.pyplot as plt

x1 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
y1 = [2.428e-08,1.902e-09,3.969e-10,1.229e-10,4.592e-11,1.984e-11 ,9.366e-12,4.775e-12,2.175e-12,1.328e-12]
y1 = [element / 10000 for element in y1]
plt.plot(x1, y1,marker='o', linestyle='dashdot', color='r', label='Production')




plt.title('Production cross section vs Mass')
plt.xlabel('Mass (GeV)')
plt.ylabel('Production cross section (mb)')
plt.legend()
plt.savefig('prod_xsec.pdf')  
plt.show()
