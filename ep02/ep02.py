import numpy as np
from sympy import *
import matplotlib.pyplot as plt

def diff_y(t, y):
    '''Retorna a derivada da função fornecida no ponto (t, y)'''
    f = lambdify([x, y_var], fuser)  # Função f(t, y) a ser aproximada
    return f(t, y)

# passo
def step(t0, tf, n):
    '''Calcula o tamanho do passo'''
    return (tf-t0)/n 

def aprox(a, b, n, y0):
    '''Aproximação pelo método de Euler explícito'''
    passo = step(a, b, n)
    # valores para t
    t = np.arange(a, b+passo, passo)
    # valores da função y(t)
    y_values = np.zeros(len(t))
    y_values[0] = y0  # Condição inicial
    
    # Calcula os valores aproximados usando o método de Euler
    for i in range(len(t)-1):
        y_values[i+1] = y_values[i] + passo * diff_y(t[i], y_values[i])
    
    return t, y_values

def main(a, b):
    '''Compila os valores da aproximação para diferentes valores de n'''
    listn = [16, 64, 256, 1024]  # lista de valores de n (passos)
    T = []
    Y = []
    y0 = float(input('Insira o valor inicial de y(0): '))  # Valor inicial de y(0)
    
    for n in listn:
        t, y_values = aprox(a, b, n, y0)
        T.append(t)
        Y.append(y_values)

    # plotar aproximação
    linestyles = ['--', '-.', ':', '-']
    plt.figure(figsize=(12, 8))
    plt.style.use('grayscale')

    # loop para plotar todos os valores de T e Y
    for i in range(len(listn)):
        plt.plot(T[i], Y[i], linestyle=linestyles[i], label=f'n={listn[i]}')  # Usando a lista para o label

    plt.title('Método de Euler')
    plt.xlabel('t')
    plt.ylabel('y(t)')
    plt.grid()
    plt.legend(loc='lower right')
    plt.show()

if __name__ == "__main__":
    x, y_var = symbols('x y')  # Declara as variáveis simbólicas t e y
    user_input = input("Insira uma equação diferencial f(t, y): ")
    fuser = sympify(user_input)
    a = float(input('Intervalo de integração - valor mínimo (a): '))
    b = float(input('Intervalo de integração - valor máximo (b): '))
    main(a, b)
