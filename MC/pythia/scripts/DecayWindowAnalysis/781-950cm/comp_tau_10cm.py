import matplotlib.pyplot as plt

## for 10 cm 
x1 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
y1 = [16,0,0,0,0,0,0,0,0,0]
y1 = [element / 10000 for element in y1]
plt.plot(x1, y1,marker='x', linestyle='dashdot', color='r', label='10 cm')


x2 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
y2 = [0.00085014,0.00048598,0.00062577,0.00082845,0.00062054,0.00064325,0.0007397,0.00056225,0.0004338,0.00037027]
plt.plot(x2, y2,marker='+', linestyle='solid', color='b', label='10 cm (CMS)')


plt.title('Number of Events between T1 and T3 (781-850 cm) (tau = 10cm)  vs Mass')
plt.xlabel('Mass (GeV)')
plt.ylabel('Number of Events')
plt.legend()
plt.savefig('comp_tau_10cm.pdf')  
plt.show()
