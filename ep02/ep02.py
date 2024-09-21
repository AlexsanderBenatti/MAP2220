import numpy as np
from sympy import *
import matplotlib.pyplot as plt

def diff_y(t, y, fuser):
    '''Retorna a derivada da função fornecida no ponto (t, y)'''
    t_var, y_var = symbols('t y')  # Declara as variáveis simbólicas t e y
    f = lambdify([t_var, y_var], fuser)  # Função f(t, y) a ser aproximada
    return f(t, y)

# passo
def step(t0, tf, n):
    '''Calcula o tamanho do passo'''
    return (tf-t0)/n 

def aprox(a, b, n, y0, fuser):
    '''Aproximação pelo método de Euler explícito'''
    passo = step(a, b, n)
    # valores para t
    t = np.arange(a, b+passo, passo)
    # valores da função y(t)
    y_values = np.zeros(len(t))
    y_values[0] = y0  # Condição inicial
    
    # Calcula os valores aproximados usando o método de Euler
    for i in range(len(t)-1):
        y_values[i+1] = y_values[i] + passo * diff_y(t[i], y_values[i], fuser)
    
    return t, y_values

def main(a, b, fuser):
    '''Compila os valores da aproximação para diferentes valores de n'''
    listn = [16, 64, 256, 1024]  # lista de valores de n (passos)
    T = []
    Y = []
    y0 = float(input('Insira o valor inicial de y(0): '))  # Valor inicial de y(0)
    
    for n in listn:
        t, y_values = aprox(a, b, n, y0, fuser)
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

def problem(num):
    n = 2500
    t_0, t_n = 0, 140
    y_0 = 10
    alpha, beta = 0.2, float("0.02" + str(num))
    #t_var, y_var = symbols('t y')
    fuser = sympify(f"y*({alpha} - {beta}*y)")
    t, y_values = aprox(t_0, t_n, n, y_0, fuser)

    plt.figure(figsize=(12, 8))
    plt.style.use('grayscale')
    plt.plot(t, y_values, linestyle='-', label=f"x\'(t) = x(t)*({alpha} - {beta}*x(t))")
    plt.title(f"x\'(t) = x(t)*(0.2 - {beta}*x(t))")
    plt.xlabel('t')
    plt.ylabel('x(t)')
    plt.grid()
    plt.legend(loc='upper right')
    plt.show()

if __name__ == "__main__":
    option = input("Para fazer o gráfico do problema de x'(t) = x*(0.2 - 0.02ab*x) insira 1: ")
    if option == "1":
        problem(int(input("Insira o valor de ab: ")))
        exit()
    #t_var, y_var = symbols('t y')  # Declara as variáveis simbólicas t e y
    user_input = input("Insira uma equação diferencial f(t, y): ")
    fuser = sympify(user_input)
    a = float(input('valor mínimo do intervalo (a): '))
    b = float(input('valor máximo do intervalo (b): '))
    main(a, b, fuser)
