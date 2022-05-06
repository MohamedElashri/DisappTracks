from matplotlib import pyplot as plt

## for 1000 cm
x1 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
y1 = [117,110,111,95,128,106,92,88,50,67]
y1 = [element / 10000 for element in y1]
plt.plot(x1, y1,marker='x', linestyle='dashdot', color='r', label='1000 cm')



plt.title('Ratio of Events Produced (850-950 cm) (tau = 1000cm)  vs Mass')
plt.xlabel('Mass (GeV)')
plt.ylabel('Ratio of Events')
plt.legend()
plt.savefig('comp_tau_1000cm.pdf')  
plt.show()
