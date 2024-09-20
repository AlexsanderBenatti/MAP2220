import numpy as np 
from sympy import *
import matplotlib.pyplot as plt

def diff_y(t):
    '''aproximação da derivada'''
    delta_t = 10**-5
    x = symbols('x')
    f = lambdify(x,fuser)
    return (f(t+delta_t)-f(t))/delta_t

# passo
def step(t0,tf,n):
    '''calcula o passo'''
    return (tf-t0)/n 

def aprox(a,b,n):
    '''calcula a aproximação da derivada'''
    passo = step(a,b,n)
    #valores para t
    t = np.arange(a,b+passo,passo)
    #valores da derivada
    flinha = np.zeros(len(t))
    diff_f = lambdify(x, diff(fuser, x,1)) #permite calcular a derivada
    flinha[0] = diff_f(0) #calcula a derivada no ponto zero
    #calcula os valores aproximados
    for i in range(len(t)-1):
        flinha[i+1] = flinha[i] + passo*diff_y(t[i])
    return t, flinha

def main(a,b):
    '''compila os valores da aproximação para diferentes valores de n'''
    listn = [16,64,256,1024] #lista de valores de n 
    T = []
    F = []
    for n in listn:
        t,flinha = aprox(a,b,n)
        T.append(t)
        F.append(flinha)

    #plotar aproximação
    linestyles = ['--', '-.', ':', '-']
    plt.figure(figsize = (12, 8))
    plt.style.use('grayscale')

    #loop para plotar todos os valores de T e F
    for i in range(len(listn)):
        plt.plot(T[i], F[i], linestyle=linestyles[i], label=f'n={listn[i]}')  #usando a lista para o label

    plt.title('Método de Euler')
    plt.xlabel('t')
    plt.ylabel('f(t)')
    plt.grid()
    plt.legend(loc='lower right')
    plt.show()

if __name__ == "__main__":
    x = symbols('x')
    user_input = input("Insira uma função f(x): ")
    fuser = sympify(user_input)
    a = float(input('Intervalo de integração - valor mínimo (a): '))
    b = float(input('Intervalo de integração - valor máximo (b): ')) 
    main(a,b)