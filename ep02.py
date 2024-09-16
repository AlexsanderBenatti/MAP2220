import numpy as np 
from sympy import *

# f(x,yx)
def f(x):
    return np.exp(-x)

def delf(x):
    return -1*np.exp(-x)

#domínio de integração
t0 = 0
tf = 3
n = 64
# passo
def step(tf,t0,n):
    return (tf-t0)/n 

passo = step(tf,t0,n)

# valores para t
t = np.arange(t0, tf+passo, passo)

# valores da derivada
flinha = np.zeros(len(t))
flinha[0] = -1 #valor da derivada no ponto 0

for i in range(len(t)-1):
    flinha[i+1] = (f(t[i+1])-f(t[i]))/passo

# plotar aproximação x real
import matplotlib.pyplot as plt
plt.figure(figsize = (12, 8))
plt.plot(t, flinha, 'bo--', label='Approximate')
plt.plot(t, delf(t), 'g', label='Exact')
plt.title('Approximate and Exact Solution')
plt.xlabel('t')
plt.ylabel('f(t)')
plt.grid()
plt.legend(loc='lower right')
plt.show()


