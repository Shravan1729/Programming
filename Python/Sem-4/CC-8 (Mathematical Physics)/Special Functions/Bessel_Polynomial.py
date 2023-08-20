#important Modules to import
import numpy as np
from scipy.special import jv
import matplotlib.pyplot as plt

X=np.linspace(-10,10,1000)
mark=['o','*','P','s','d']

#Plotting of the Bessel Polynomial
n = 5
for j in range(n):
    bassel = jv(j,X)
    plt.plot(X,bassel,marker=mark[j],markevery=50,label=f'$J_{j!r}$')
plt.title('Bessel Polynomial')
plt.legend(loc='best')
plt.ylabel(r'$J_n(x)$')
plt.xlabel(r'$x$')
plt.grid()
plt.savefig('bassel.png')
plt.show()