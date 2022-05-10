import matplotlib.pyplot as plt

## for 100 cm
x1 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
y1 = [162,91,56,52,34,34,18,18,10,2]
y1 = [element / 10000 for element in y1]
plt.plot(x1, y1,marker='x', linestyle='dashdot', color='r', label='100 cm')


x2 = [100,200,300,400,500,600,700,800,900,1000]
y2 = [0.00061004,0.0024316,0.0038854,0.0051921,0.0050584,0.00598,0.0071477,0.0074629,0.007491,0.0079149]
plt.plot(x2, y2,marker='+', linestyle='solid', color='b', label='100 cm (CMS)')

plt.title('Ratio of Events between T2 and T3 (850-950 cm) (tau = 100cm)  vs Mass')
plt.xlabel('Mass (GeV)')
plt.ylabel('Ratio of Events')
plt.legend()
plt.savefig('comp_tau_100cm.pdf')  
plt.show()
