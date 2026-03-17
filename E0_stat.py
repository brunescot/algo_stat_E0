import numpy as np
g = 9.7864
in_i = 0.05

comp_br = [0.378, 0.289, 0.263, 0.264, 0.263]
comp_fe = [0.35, 0.228, 0.224, 0.251, 0.286]
comp_pe = [0.262, 0.226, 0.242, 0.249, 0.224]

med_br = [15.0, 16.9, 10.9, 14.0, 14.8]
med_fe = [18.1, 20.3, 8.6, 8.9, 6.5]
med_pe = [12.9, 14.4, 13.3, 13.9, 11.5]

def variancia (lista) :
    avg = np.mean(lista)
    sum = 0
    for item in lista:
        sum += (item - avg)**2
    return round((1/(len(lista) - 1))*sum, 5)

def desvio_medidas(lista):
    return round(np.sqrt(variancia(lista)), 5)

def desvio_medio (lista) :
    return round(desvio_medidas(lista)/np.sqrt(len(lista)), 5)

def desvio_c (lista) :
    return round(np.sqrt(in_i**2 + desvio_medio(lista)**2), 5)


def tempo_grav (h):
    return np.sqrt(2*h/(100*g))

def tempo (lista) :
    t = []
    for h in lista:
        t.append(round(tempo_grav(h), 5))
    return np.array(t)

def propag (dist, tempo):
    d_medio = np.mean(dist)
    t_medio = np.mean(tempo)

    dddist = (1/2*d_medio*g)*(desvio_c(dist)**2)
    ddtempo = ((t_medio**2)/(2*(g**3)))*(desvio_c(tempo)**2)

    return round(np.sqrt(dddist + ddtempo), 5)


def medir(lista):
    avg = round(np.mean(lista), 5)
    d_c = round(desvio_c(lista), 5)
    print("valor medio = ", round(np.mean(lista), 5))
    print("desvio_medidas = ", round(desvio_medidas(lista), 5))
    print("desvio_medio =", round(desvio_medio(lista), 5))
    print("desvio_c =", d_c)
    print("v_medio + inc = ", avg, "+-",d_c)





t_br = tempo(med_br)
t_fe = tempo(med_fe)
t_pe = tempo(med_pe)

print("y bruno: ")
medir(med_br)
print("\n")
print("tempo bruno:")
print(t_br)
medir(t_br)
print("\n")
print("propag. de erros: ", propag(med_br, t_br))
print("desv. medio relativo comp = ", round(desvio_medidas(comp_br) / round(np.mean(comp_br),5), 5))
print("desv. medio relativo regua = ", round(desvio_medidas(t_br) / np.mean(t_br), 5))
print("\n")

print("y felps: ")
medir(med_fe)
print("\n")
print("tempo felps: ")
print(t_fe)
medir(t_fe)
print("\n")
print("propag. de erros: ", propag(med_fe, t_fe))
print("desv. medio relativo comp = ", round(desvio_medidas(comp_fe) / np.mean(comp_fe), 5))
print("desv. medio relativo regua = ", round(desvio_medidas(t_fe) / np.mean(t_fe), 5))
print("\n")


print("y pedrao: ")
medir(med_pe)
print("\n")
print("tempo pedrao: ")
print(t_pe)
medir(t_pe)
print("\n")
print("propag. de erros: ", propag(med_pe, t_pe))
print("desv. medio relativo comp = ", round(desvio_medidas(comp_pe) / np.mean(comp_pe),5))
print("desv. medio relativo regua = ", round(desvio_medidas(t_pe) / np.mean(t_pe),5))
print("\n")




