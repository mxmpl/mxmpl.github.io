import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,20,100)
w = 0.54 - 0.46*np.cos(2*np.pi*x/20)

plt.plot(x, w, label='Hamming')
plt.xlabel('Samples')
plt.ylabel('Amplitude')
plt.legend()
plt.show()

