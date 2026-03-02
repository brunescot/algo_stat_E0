import numpy as np

in_i = 0.05

med_br = [15.0, 16.9, 10.9, 14.0, 14.8]
med_fe = [18.1, 20.3, 8.6, 8.9, 6.5]
med_pe = [12.9, 14.4, 13.3, 13.9, 11.5]

def variancia (lista) :
    avg = np.mean(lista)
    sum = 0
    for item in lista:
        sum += (item - avg)**2
    return round((1/(len(lista) - 1))*sum, 4)

def desvio_medidas(lista):
    return round(np.sqrt(variancia(lista)), 4)

def desvio_medio (lista) :
    return round(desvio_medidas(lista)/np.sqrt(len(lista)), 4)

def desvio_c (lista) :
    return round(np.sqrt(in_i**2 + desvio_medio(lista)**2), 4)

def medir (lista) :
    avg = round(np.mean(lista), 4)
    d_m = desvio_medidas(lista)
    d_mm = desvio_medio(lista)
    d_c = desvio_c(lista)

    print("t_medio = ", avg)
    print("desvio_medidas = ", d_m)
    print("desvio_medio =", d_mm)
    print("desvio_c =",d_c)
    print("t_medio + inc = ", avg, "+-", d_c)

print("bruno: ")
medir(med_br)
print("\n")

print("felps: ")
medir(med_fe)
print("\n")

print("pedrao: ")
medir(med_pe)




