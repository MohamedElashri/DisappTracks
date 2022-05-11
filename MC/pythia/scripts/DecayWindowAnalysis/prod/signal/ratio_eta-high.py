# This script is to plot the eta cut ratio for high tau (10000cm-100000cm-1000000cm)

import matplotlib.pyplot as plt


x1 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
y1 = [6709,5296,4491,3795,2526,2995,2682,2359,2202,1982]
y1 = [element / 10000 for element in y1]
x2= [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
y2= [6709,5296,4491,3795,2526,2995,2682,2359,2202,1982]
y2 = [element / 10000 for element in y2]
x3 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
y3 = [6709,5296,4491,3795,2526,2995,2682,2359,2202,1982]
y3 = [element / 10000 for element in y3]
plt.plot(x1, y1,marker='o', linestyle='dashdot', color='r', label='Number of Events (10000 cm)')
plt.plot(x2, y2,marker='o', linestyle='dashdot', color='b', label='Number of Events (100000 cm)')
plt.plot(x3, y3,marker='o', linestyle='dashdot', color='g', label='Number of Events (1000000 cm)')

plt.title(' LHCb eta Acceptance (high Lifetimes) vs Mass')
plt.xlabel('Mass (GeV)')
plt.ylabel('Events Ratio')
plt.legend()
plt.savefig('Ratio_Events_eta-high_LHCb.pdf')  
plt.show()
