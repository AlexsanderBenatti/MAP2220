import numpy as np
from sympy import *
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

# Calcula o passo
def step(t0, tf, n):
    '''Calcula o tamanho do passo'''
    return (tf - t0) / n

def aprox(t_0, t_f, n, fuser, y_0):
    '''Aproximação pelo método de Euler Implícito'''
    passo = step(t_0, t_f, n)
    # Pontos no tempo
    t_vals = np.arange(t_0, t_f + passo, passo)
    # Soluções aproximadas
    y_vals = np.zeros(len(t_vals))
    y_vals[0] = y_0  # Condição inicial

    # Iteração para calcular os valores de y
    for i in range(len(t_vals) - 1):
        tn = t_vals[i]
        tn1 = t_vals[i + 1]

        # Define g(y_{n+1}) para encontrar a raiz
        def g(yn1):
            return yn1 - passo * fuser(tn1, yn1) - y_vals[i]

        # Resolve g(y_{n+1}) = 0 usando fsolve
        y_vals[i + 1] = fsolve(g, y_vals[i])[0]  # Usa y_n como chute inicial

    return t_vals, y_vals

def main(t_0, t_f, fuser):
    '''Compila os valores da aproximação para diferentes valores de n'''
    listn = [16, 64, 256, 1024]  # Lista de valores de n (passos)
    T = []
    Y = []
    y_0 = float(input(f'Insira o valor inicial y({t_0}): '))  # Condição inicial

    for n in listn:
        t_vals, y_vals = aprox(t_0, t_f, n, fuser, y_0)
        T.append(t_vals)
        Y.append(y_vals)

    # Plotar aproximação
    linestyles = ['--', '-.', ':', '-']
    plt.figure(figsize=(6, 3))
    plt.style.use('grayscale')

    # Loop para plotar todos os valores de T e Y
    for i in range(len(listn)):
        plt.plot(T[i], Y[i], linestyle=linestyles[i], label=f'n={listn[i]}')  # Usando a lista para o label

    plt.title('Método de Euler Implícito')
    plt.xlabel('t')
    plt.ylabel('y(t)')
    plt.grid()
    plt.legend(loc='lower right')
    plt.show()

if __name__ == "__main__":
    t, y = symbols('t y')  # Declara variáveis simbólicas
    user_input = input("Insira uma equação diferencial y'(t, y): ")
    fuser_sympy = sympify(user_input)  # Converte a entrada em função simbólica
    fuser = lambdify([t, y], fuser_sympy)  # Converte a função simbólica em computável
    t_0 = float(input('Valor inicial do intervalo: '))
    t_f = float(input('Valor final do intervalo: '))
    main(t_0, t_f, fuser)
