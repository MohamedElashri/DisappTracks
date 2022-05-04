import matplotlib.pyplot as plt

## for 100 cm
x1 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
y1 = [15,14,14,24,12,12,20,7,14,14]
y1 = [element / 10000 for element in y1]
plt.plot(x1, y1,marker='x', linestyle='dashdot', color='r', label='10000 cm')


x2 = [100,200,300,400,500,600,700,800,900,1000]
y2 = [1.6176e-05,2.5473e-05,5.5924e-05,0.00012573,0.00017215,0.00024393,0.00018914,0.00021643,0.00038493,0.00038831]
plt.plot(x2, y2,marker='+', linestyle='solid', color='b', label='10000 cm (CMS)')

plt.title('Number of Events between T1 and T2 (780-850 cm) (tau = 10000cm)  vs Mass')
plt.xlabel('Mass (GeV)')
plt.ylabel('Number of Events')
plt.legend()
plt.savefig('comp_tau_10000cm.pdf')  
plt.show()
