import matplotlib.pyplot as plt
import numpy as np
from E0_stat import variancia, desvio_medidas, desvio_medio

g = 9.7864
G = 6.67384e-11

def desvio_c (lista, in_inst) :
    return round(np.sqrt(in_inst**2 + desvio_medio(lista)**2), 5)



def s():

    t = int(input("t: "))

    s_0 = int(input("s_0: "))

    v_0 = int(input("v_0: "))

    v = int(input("v: "))

    print("a: ")
    a = int(input())


    if ~t : return (v**2 - v_0**2)/(2*a) ## Torricelli
    elif ~v : return s_0 + v_0*t + (a/2)*(t**2) ## Sorvetao
    return None

# retorna a força gravitacional
def f_grav():
    print("M: ")
    M = int(input())

    print("m: ")
    m = int(input())

    print("r: ")
    r = int(input())

    try:
        return -G*M*m/(np.square(r))
    except:
        print("Division by zero!")
        return None

# retorna a velocidade em função de (v_0, a, Dx) ou (v_0, a ,t)
def v () :
    print("t: ")
    t = int(input())

    print("v_0: ")
    v_0 = int(input())

    print("v: ")
    Dx = int(input())

    print("a: ")
    a = int(input())

    if ~t : return np.sqrt(v_0**2 + 2*a*Dx) ## Torricelli
    elif Dx : return v_0 + a*t
    return None

## equação de Stokes
def f_visc ():
    print("eta: ")
    eta = int(input())

    print("R: ")
    R = int(input())

    print("v: ")
    vel = int(input())

    return 6*np.pi*eta*R*vel

def init():
    exit = 1
    inst = int(input("Insira a instrução: "))
    while(exit==1):
        match inst:
            case 0:
                print("posição: ", s())
            case 1:
                print("velocidade em t: ", v())
            case 2:
                print("força grav: ", f_grav())
            case 3:
                print("força viscoso: ", f_visc())

            case 4:
                i = 0
                n = int(input("Tamanho do vetor: "))
                vec = []
                in_i = float(input("Incerteza do instrumento: "))

                while i < n:
                    print("Valor ", i, ":")
                    k = float(input())
                    vec.append(k)
                    i += 1

                print(vec)
                print("Media: ", np.mean(vec))
                print("Variancia: ", variancia(vec))
                print("Desvio padrao (raiz da variancia): ", desvio_medidas(vec))
                print("Desvio medio: ", desvio_medio(vec))
                print("Desvio final (medio com inst): ", desvio_c(vec, in_i))
                exit = input("Continuar? 1 para sim, 0 para nao")
            case _:
                print("foi pro default :/ ")


init()