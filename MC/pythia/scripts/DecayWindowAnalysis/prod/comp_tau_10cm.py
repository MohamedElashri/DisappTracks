import matplotlib.pyplot as plt

## for 10 cm 
x1 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
y1 = [6,0,0,0,0,0,0,0,0,0]
y1 = [element / 10000 for element in y1]
yerr1 =10
plt.plot(x1, y1,marker='x', linestyle='dashdot', color='r', label='10 cm')


plt.title('Ratio of Events Produced  (tau = 10cm) vs Mass')
plt.xlabel('Mass (GeV)')
plt.ylabel('Ratio of Events')
plt.legend()
plt.savefig('comp_tau_10cm.pdf')  
plt.show()
