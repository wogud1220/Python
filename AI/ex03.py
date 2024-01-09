import matplotlib.pyplot as mp
import numpy as np

x=[]
y=[]

for i in range (1,101):
    x.append()
    y.append(i*i*i)


arr_x= np.array(x)
arr_y = np.array(y)

mp.plot(arr_x, arr_y)
mp.show()