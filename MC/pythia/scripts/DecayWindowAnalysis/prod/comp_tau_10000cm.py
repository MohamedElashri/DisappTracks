import matplotlib.pyplot as plt

## for 100 cm
x1 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
y1 = [188,160,214,238,198,203,210,205,173,156]
y1 = [element / 10000 for element in y1]
plt.plot(x1, y1,marker='x', linestyle='dashdot', color='r', label='10000 cm')



plt.title('Ratio of Events Produced (850-950 cm) (tau = 10000cm)  vs Mass')
plt.xlabel('Mass (GeV)')
plt.ylabel('Ratio of Events')
plt.legend()
plt.savefig('comp_tau_10000cm.pdf')  
plt.show()
