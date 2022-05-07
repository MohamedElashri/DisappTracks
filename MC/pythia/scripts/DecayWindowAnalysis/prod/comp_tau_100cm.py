import matplotlib.pyplot as plt

## for 100 cm
x1 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
y1 = [5478,4771,4167,3653,3432,2947,2628,2339,2196,1974]
y1 = [element / 10000 for element in y1]
plt.plot(x1, y1,marker='x', linestyle='dashdot', color='r', label='100 cm')


plt.title('Ratio of Events Produced (tau = 100cm)  vs Mass')
plt.xlabel('Mass (GeV)')
plt.ylabel('Ratio of Events')
plt.legend()
plt.savefig('comp_tau_100cm.pdf')  
plt.show()
