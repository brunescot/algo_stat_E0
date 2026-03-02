import numpy as np
g = 9.7864
in_i = 0.05

med_br = [15.0, 16.9, 10.9, 14.0, 14.8]
med_fe = [18.1, 20.3, 8.6, 8.9, 6.5]
med_pe = [12.9, 14.4, 13.3, 13.9, 11.5]

t_bruno = t_felps = t_pedrao = []

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


def tempo_grav (h):
    return np.sqrt(2*h/(100*g))

def tempo (lista) :
    t = []
    for h in lista:
        t.append(round(tempo_grav(h), 4))
    return np.array(t)



def medir(lista):
    avg = round(np.mean(lista), 4)
    d_c = round(desvio_c(lista), 4)
    print("valor medio = ", round(np.mean(lista), 4))
    print("desvio_medidas = ", round(desvio_medidas(lista), 4))
    print("desvio_medio =", round(desvio_medio(lista), 4))
    print("desvio_c =", d_c)
    print("v_medio + inc = ", avg, "+-",d_c)





print("y bruno: ")
medir(med_br)
print("\n")
print("tempo bruno:")
print(tempo(med_br))
medir(tempo(med_br))
print("\n")

print("y felps: ")
medir(med_fe)
print("\n")
print("tempo felps: ")
print(tempo(med_fe))
medir(tempo(med_fe))
print("\n")

print("y pedrao: ")
medir(med_pe)
print("\n")
print("tempo pedrao: ")
print(tempo(med_pe))
medir(tempo(med_pe))




