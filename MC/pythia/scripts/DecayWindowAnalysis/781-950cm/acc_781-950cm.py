import matplotlib.pyplot as plt

## for 10 cm 
x1 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
y1 = [16,0,0,0,0,0,0,0,0,0]
y1 = [element / 10000 for element in y1]
plt.plot(x1, y1,marker='x', linestyle='dashdot', color='r', label='10 cm')

## for 100 cm
x2 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
y2 = [486,283,102,150,88,86,59,46,32,20]
y2 = [element / 10000 for element in y2]
plt.plot(x2, y2,marker='x', linestyle='dashdot', color='b', label='100 cm')

## for 1000 cm
x3 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
y3 = [305,287,267,291,302,222,238,193,172,157]
y3 = [element / 10000 for element in y3]
plt.plot(x3, y3,marker='x', linestyle='dashdot', color='g', label='1000 cm')

## for 10000 cm
x4 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
y4 = [52,39,32,57,46,47,60,45,51,39]
y4 = [element / 10000 for element in y4]
plt.plot(x4, y4,marker='x', linestyle='dashdot', color='m', label='10000 cm')


# CMS accpetance
# https://www.hepdata.net/record/ins1790827
x5 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
y5 = [0.00085014,0.00048598,0.00062577,0.00082845,0.00062054,0.00064325,0.0007397,0.00056225,0.0004338,0.00037027]
plt.plot(x5, y5,marker='+', linestyle='solid', color='y', label='10 cm (CMS)')

x6 = [100,200,300,400,500,600,700,800,900,1000]
y6 = [0.00061004,0.0024316,0.0038854,0.0051921,0.0050584,0.00598,0.0071477,0.0074629,0.007491,0.0079149]
plt.plot(x6, y6,marker='+', linestyle='solid', color='c', label='100 cm (CMS)')

x7 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
y7 = [0.00015382,0.00028979,0.00091359,0.0011283,0.001012,0.001058,0.002202,0.0021455,0.002421,0.002421]
plt.plot(x7, y7,marker='+', linestyle='solid', color='lime', label='1000 cm (CMS)')

x8 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
y8 = [1.6176e-05,2.5473e-05,5.5924e-05,0.00012573,0.00017215,0.00024393,0.00018914,0.00021643,0.00038493,0.00038831]
plt.plot(x8, y8,marker='+', linestyle='solid', color='0', label='10000 cm (CMS)')

plt.title('LHCb Accpetance between T1 and T3 (780-950 cm) vs Mass')
plt.xlabel('Mass (GeV)')
plt.ylabel('Accpetance')
plt.legend()
plt.savefig('Acc_781-950cm.pdf')  
plt.show()
