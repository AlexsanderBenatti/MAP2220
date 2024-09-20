import numpy as np 
from sympy import *
import matplotlib.pyplot as plt

'''método explícito'''
# f'(x)
def diff_f(fuser):
    '''calcula a derivada da função no ponto a'''
    # Declara a variável x
    x = symbols('x')
    # Cria uma função para a 2° derivada
    diff_f = lambdify(x, diff(fuser, x, 2))
    # Retorna o valor da 2° derivada no ponto a
    return diff_f

# passo
def step(tf,t0,n):
    return (tf-t0)/n 

def aprox(fuser,a,b,n):
    passo = step(b,a,n)
    #valores para t
    t = np.arange(a,b+passo,passo)
    #valores da derivada
    flinha = np.zeros(len(t))
    flinha[0] = diff(0) #derivada no ponto zero
    #transforma input em função
    f = lambdify(x,fuser)
    #calcula os valores aproximados
    for i in range(len(t)-1):
        flinha[i+1] = (f(t[i+1])-f(t[i]))/passo
    return t, flinha

def main(fuser,a,b):
    listn = [16,64,256,1024] #lista de valores de n 
    T = []
    F = []
    for n in listn:
        t,flinha = aprox(fuser,a,b,n)
        T.append(t)
        F.append(flinha)

    #plotar aproximação
    linestyles = ['--', '-.', ':', '-']
    plt.figure(figsize = (12, 8))
    plt.style.use('grayscale')

    # Loop para plotar todos os valores de T e F
    for i in range(len(listn)):
        plt.plot(T[i], F[i], linestyle=linestyles[i], label=f'n={listn[i]}')  # Usando a lista para o label

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
    main(fuser,a,b)