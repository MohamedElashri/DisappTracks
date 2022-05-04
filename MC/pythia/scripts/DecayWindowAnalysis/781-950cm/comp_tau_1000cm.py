from matplotlib import pyplot as plt

## for 1000 cm
x1 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
y1 = [305,287,267,291,302,222,238,193,172,157]
y1 = [element / 10000 for element in y1]
plt.plot(x1, y1,marker='x', linestyle='dashdot', color='r', label='1000 cm')


x2 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
y2 = [0.00015382,0.00028979,0.00091359,0.0011283,0.001012,0.001058,0.002202,0.0021455,0.002421,0.002421]
plt.plot(x2, y2,marker='+', linestyle='solid', color='b', label='1000 cm (CMS)')

plt.title('Number of Events between T1 and T3 (781-950 cm) (tau = 1000cm)  vs Mass')
plt.xlabel('Mass (GeV)')
plt.ylabel('Number of Events')
plt.legend()
plt.savefig('comp_tau_1000cm.pdf')  
plt.show()
