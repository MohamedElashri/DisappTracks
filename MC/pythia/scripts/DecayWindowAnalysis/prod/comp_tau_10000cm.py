import matplotlib.pyplot as plt

## for 100 cm
x1 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
y1 = [24,13,11,20,16,15,22,24,23,23]
y1 = [element / 10000 for element in y1]
plt.plot(x1, y1,marker='x', linestyle='dashdot', color='r', label='10000 cm')



plt.title('Ratio of Events Produced (850-950 cm) (tau = 10000cm)  vs Mass')
plt.xlabel('Mass (GeV)')
plt.ylabel('Ratio of Events')
plt.legend()
plt.savefig('comp_tau_10000cm.pdf')  
plt.show()
