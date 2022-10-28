import math
# Entrada: calcetines
socks = [9, 10, 20, 10, 10, 30, 50, 10, 20]
# Arreglo donde se guardarán los calcetines repetidos
repeated = []
# Arreglo donde se guardarán los calcetines únicos
unique = []
for i in socks:
    #Se agregan los únicos
    if i not in unique:
        unique.append(i)
    #Se agregan los repetidos, junto a su concurrencia, se asegura que no se repita item
    elif not (any(d['value'] == i for d in repeated)):
        repeated.append({"value": i, "repetitions": socks.count(i)})
# Variable donde se contarán los pares
couple_total = 0
for j in repeated:
    # Se saca la parte entera de las concurrencias divididas entre 2 para saber cuántos pares se pueden extraer
    couple_number = math.trunc(j['repetitions']/2)
    # Se van sumando los pares totales
    couple_total += couple_number
# Salida: cantidad de pares de calcetines
print(couple_total)
