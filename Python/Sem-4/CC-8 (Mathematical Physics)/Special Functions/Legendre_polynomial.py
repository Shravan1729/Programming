#Important Modules to import

import numpy as np
from scipy.special import legendre
import matplotlib.pyplot as plt

x=np.linspace(-1,1,1000)
mark=['o','*','P','s']

n=5

#Plotting of the Legendre Polynomial
for i in range(1,n):
    p=legendre(i)
    plt.plot(x,p(x),marker=mark[i-1],markevery=50,label=f'$P_{i!r}$')

plt.title('Legendre Polynomial')
plt.xlabel('x')
plt.ylabel(r'$P_n(x)$')
plt.legend(loc = 'best')
plt.grid()
plt.savefig('legendre.png')
plt.show()