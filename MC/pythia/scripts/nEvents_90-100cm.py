import matplotlib.pyplot as plt

## for 10 cm 
x1 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
y1 = [379, 275, 167, 135, 95, 74, 56, 36, 28, 21]
plt.plot(x1, y1,marker='x', linestyle='--', color='r', label='10 cm')

## for 100 cm
x2 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
y2 = [675, 836, 718, 793, 841, 870, 823, 841, 879, 871]
plt.plot(x2, y2,marker='o', linestyle='--', color='b', label='100 cm')

## for 1000 cm
x3 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
y3 = [137, 178, 214, 236, 242, 252, 308, 305, 342, 227]
plt.plot(x3, y3,marker='+', linestyle='--', color='g', label='1000 cm')

## for 10000 cm
x4 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
y4 = [10, 23, 32, 44, 35, 22, 39, 29, 40, 24]
plt.plot(x4, y4,marker='o', linestyle='--', color='m', label='10000 cm')


plt.title('Number of Events in decay window (90-100 cm) vs Mass')
plt.xlabel('Mass (GeV)')
plt.ylabel('Number of Events')
plt.legend()
plt.savefig('nEvents_90-100cm.pdf')  
plt.show()
