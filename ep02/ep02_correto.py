import numpy as np 
from sympy import *
import matplotlib.pyplot as plt

# def diff_y(t):
#     '''aproximação da derivada'''
#     delta_t = 10**-5
#     x = symbols('x')
#     f = lambdify(x,fuser)
#     return (f(t+delta_t)-f(t))/delta_t

# passo
def step(t0,tf,n):
    '''calcula o passo'''
    return (tf-t0)/n 

def aprox(t_0,t_f,n):
    '''calcula a aproximação da derivada'''
    passo = step(t_0,t_f,n)
    #valores para t
    t = np.arange(t_0,t_f+passo,passo)
    #valores da derivada
    y = np.zeros(len(t))
    y[0] = y_0
    #calcula os valores aproximados
    for i in range(len(t)-1):
        y[i+1] = y[i] + passo*ylinha(t[i])
    return t, y

def main(t_0,t_f):
    '''compila os valores da aproximação para diferentes valores de n'''
    listn = [16,64,256,1024] #lista de valores de n 
    T = []
    F = []
    for n in listn:
        t,f_t = aprox(t_0,t_f,n)
        T.append(t)
        F.append(f_t)

    #plotar aproximação
    linestyles = ['--', '-.', ':', '-']
    plt.figure(figsize = (6, 3))
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
    user_input = input("Insira uma função y'(x): ")
    fuser = sympify(user_input)
    ylinha = lambdify(x,fuser)
    t_0 = float(input('Valor inicial do intervalo: '))
    y_0 = float(input(f'Valor inicial (y({t_0})): '))
    t_f = float(input('Valor final do intervalo: ')) 
    main(t_0,t_f)