import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-10, 10.01, 0.01)
y=str(input())
plt.xkcd()
plt.plot(x,eval(y))

plt.show()