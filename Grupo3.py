import numpy as np
import matplotlib.pyplot as plt 

x = np.linspace(4,30,10)
y = x**2*np.sin(x)
plt.figure()
plt.plot(x,y)
plt.show()