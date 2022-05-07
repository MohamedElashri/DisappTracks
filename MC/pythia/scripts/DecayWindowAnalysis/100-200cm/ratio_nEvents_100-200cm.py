import matplotlib.pyplot as plt

## for 10 cm 
x1 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
y1 = [825,408,244,170,94,51,30,22,14,6]
y1 = [element / 10000 for element in y1]
plt.plot(x1, y1,marker='x', linestyle='--', color='r', label='10 cm')

## for 100 cm
x2 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
y2 = [978,997,973,763,703,626,604,561,559,487]
y2 = [element / 10000 for element in y2]
plt.plot(x2, y2,marker='o', linestyle='--', color='b', label='100 cm')

## for 1000 cm
x3 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
y3 = [163,170,168,152,160,198,216,156,153,159]
y3 = [element / 10000 for element in y3]
plt.plot(x3, y3,marker='+', linestyle='--', color='g', label='1000 cm')

## for 10000 cm
x4 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
y4 = [25,18,22,34,18,26,14,18,16,14]
y4 = [element / 10000 for element in y4]
plt.plot(x4, y4,marker='o', linestyle='--', color='m', label='10000 cm')


plt.title('The ratio of Events in decay window (90-100 cm) to total event (10000 evts) vs Mass')
plt.xlabel('Mass (GeV)')
plt.ylabel('The ratio')
plt.legend()
plt.savefig('ratio_Events_90-100cm.pdf')  
plt.show()
