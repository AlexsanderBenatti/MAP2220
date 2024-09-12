import numpy as np
from sympy import diff, symbols, lambdify, sympify, E, exp

# 2° e 4° derivada da função integrada
def diff2_f(a):
    # Declara a variável x
    x = symbols('x')
    # Cria uma função para a 2° derivada
    diff2_f = lambdify(x, diff(fuser, x, 2))
    # Retorna o valor da 2° derivada no ponto a
    return diff2_f(a)

def diff4_f(a):
    x = symbols('x')
    # Cria uma função para a 4° derivada
    diff4_f = lambdify(x, diff(fuser, x, 4))
    return diff4_f(a)


#########
# Método dos Trapézios
#########

# Cálculo do delta_i

def calc_delta_i(a, b, i):
    return (b-a)/(2**i)

# Implementação do Método dos Trapézios

def trapz(a, b, t, i):
    if i == 0:
        return (f(a)+f(b))*(b-a)/2
    t = trapz(a, b, t, i-1)
    delta_i = calc_delta_i(a, b, i)

    # Processo para calcular os valores de f apenas nos novos pontos acrescentados
    input_array = np.array([a + (2*j-1)*delta_i for j in range(1, 2**(i-1)+1)])
    sum = np.sum(f(input_array))

    return t*0.5 + delta_i*sum

# Cálculo do erro de aproximação

def error_trapz(a, b, i):
    delta_i = calc_delta_i(a, b, i)
    num = 100

    # Calcula 100 (num) pontos exóticos ξ pertencentes a [a,b] para encontrar o erro máximo
    csi_values = np.array([a + (b-a)/num*j for j in range(1, num+1)])
    # Verifica se a derivada é um valor constante
    if type(diff2_f(csi_values)) == int or type(diff2_f(csi_values)) == float:
        diff = diff2_f(csi_values)
    else:
        diff = max(diff2_f(csi_values))

    return -(b-a) * delta_i**2 * diff/12


#########
# Método de Simpson
#########

def simps(a, b, i):
    if i == 0:
        return (b-a)/3 * (f(a) + 4*f((a+b)/2) + f(b))
    delta_n = (b-a)/(2*i)

    # Valores de x_1, x_2, ... x_(2i)
    x_values = np.array([a + n*delta_n for n in range(0, 2*i+1)])

    # 4f(x_1) + 2f(x_2) + 4f(x_3) + 2f(x_4) + ... + 4f(x_2i-1) + f(x_2i)
    aux_sum = np.array([2**(j%2+1) * f(x_values[j]) for j in range(1, 2*i)])
    sum = f(x_values[0]) + f(x_values[-1]) + np.sum(aux_sum)
    
    return delta_n/3 * sum

def error_simps(a, b, n):
    num = 100

    csi_values = np.array([a + (b-a)/num*j for j in range(1, num+1)])
    if type(diff4_f(csi_values)) == int or type(diff4_f(csi_values)) == float:
        diff = diff4_f(csi_values)
    else:
        diff = max(diff4_f(csi_values))

    return -(b-a)**5/(2880*n**4) * diff

#########
# Método de Romberg
#########

def romb(a, b, e, maxi):
    # Define a primeira entrada da tabela T_0_0
    t_0_0 = (f(a) + f(b)) * (b - a) / 2
    # a variável "tabela" será a matriz que representará a tabela de Romberg
    tabela = [[t_0_0]]
    print(t_0_0)

    i = 1
    # Processo que calcula os valores de cada linha i da tabela
    while i <= maxi:
        t_i_0 = trapz(a, b, tabela[i-1], i)
        # Matriz que representa a linha i
        t_i = [t_i_0]
        print(t_i_0, end=' ')

        for k in range(1, i+1):
            t_i_k = t_i[k-1] + (t_i[k-1] - tabela[i-1][k-1]) / ((4**k) - 1)
            t_i.append(t_i_k)
            print(t_i_k, end=' ')

        # Adiciona a linha i na tabela
        tabela.append(t_i)
        print()
        i += 1
        # Verifica se os valores de T_n_n e T_n_n-1 são próximos o suficiente
        if abs(t_i[-1] - t_i[-2]) < e*abs(t_i[-1]):
            break
    
    return tabela[-1][-1], i


def main(f,a,b):
    # Valor inicialmente arbitrário para o erro e limite de erro = 0,05%
    error, lim_error = 1, 0.0005
    
    print("Método dos Trapézios:")
    i = 0
    while True:
        if abs(error) < lim_error:
            break
        t_delta = (f(a) + f(b))*(b-a)/2
        trapz_value = trapz(a, b, t_delta, i)
        error = error_trapz(a, b, i)
        # Incrementa o valor de i, fazendo o valor até achar uma aproximação com erro menor que 0,05%
        i += 1

    print(f"Número de iterações: {i} \nValor aproximado da integral: {trapz_value} \nErro máximo: {abs(error)}")
    print()

    print("Método de Simpson:")
    n, c, error = 1, 0, 1
    while True:
        if abs(error) < lim_error:
            break
        simps_value = simps(a, b, n)
        error = error_simps(a, b, n)
        # Duplica o intervalo
        n *= 2
        # Contador de iterações
        c += 1
    
    print(f"Número de iterações: {i} \nValor aproximado da integral: {simps_value} \nErro máximo: {abs(error)}")
    print()

    print("Método de Romberg:")
    romb_value, i = romb(a, b, lim_error, 10)
    print()
    print(f"Número de iterações: {i} \nValor aproximado da integral: {romb_value}")


if __name__ == "__main__":
    x = symbols('x')
    user_input = input("Insira uma função f(x): ")
    user_input = user_input.replace('exp', 'E**')
    fuser = sympify(user_input)
    f = lambdify(x, fuser)
    a = float(input('Intervalo de integração - valor mínimo (a): '))
    b = float(input('Intervalo de integração - valor máximo (b): '))
    main(f,a,b)