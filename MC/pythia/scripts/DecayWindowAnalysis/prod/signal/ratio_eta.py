## This plot shows the ratio of events that will pass the forward acceptance of LHCb detector 
import matplotlib.pyplot as plt


x1 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
y1 = [6709,5296,4491,3795,2526,2995,2682,2359,2202,1982]
y1 = [element / 10000 for element in y1]
x2 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
y2 = [6709,5296,4491,3795,2526,2995,2682,2359,2202,1982]
y2 = [element / 10000 for element in y2]
x3 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
y3 = [6709,5296,4491,3795,2526,2995,2682,2359,2202,1982]
y3 = [element / 10000 for element in y3]
x4 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
y4 = [6709,5296,4491,3795,2526,2995,2682,2359,2202,1982]
y4= [element / 10000 for element in y4]

plt.plot(x1, y1,marker='o', linestyle='dashdot', color='r', label='Number of Events (10 cm)')
plt.plot(x2, y2,marker='o', linestyle='dashdot', color='b', label='Number of Events (100 cm)')
plt.plot(x3, y3,marker='o', linestyle='dashdot', color='g', label='Number of Events (1000 cm)')
plt.plot(x4, y4,marker='o', linestyle='dashdot', color='y', label='Number of Events (10000 cm)')

plt.title('Ratio of Events Produced pass through LHCb Acceptance vs Mass')
plt.xlabel('Mass (GeV)')
plt.ylabel('Events Ratio')
plt.legend()
plt.savefig('Ratio_Events_eta_LHCb.pdf')  
plt.show()
