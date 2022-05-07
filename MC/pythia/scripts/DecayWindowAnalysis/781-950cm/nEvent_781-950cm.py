import matplotlib.pyplot as plt

## for 10 cm 
x1 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
y1 = [16,0,0,0,0,0,0,0,0,00,0,0,0,0,0,0,0]
plt.plot(x1, y1,marker='x', linestyle='--', color='r', label='10 cm')

## for 100 cm
x2 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
y2 = [486,283,102,150,88,86,59,46,32,20]
plt.plot(x2, y2,marker='o', linestyle='--', color='b', label='100 cm')

## for 1000 cm
x3 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
y3 = [305,287,267,291,302,222,238,193,172,157]
plt.plot(x3, y3,marker='+', linestyle='--', color='g', label='1000 cm')

## for 10000 cm
x4 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
y4 = [52,39,32,57,46,47,60,45,51,39]
plt.plot(x4, y4,marker='o', linestyle='--', color='m', label='10000 cm')


plt.title('Number of Events between T1 and T2 (780-850 cm) vs Mass')
plt.xlabel('Mass (GeV)')
plt.ylabel('Number of Events')
plt.legend()
plt.savefig('nEvents_781-850cm.pdf')  
plt.show()
