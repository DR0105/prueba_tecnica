def get_minimum_and_maximum_sum(integers):
    # Máximo provisional
    max = 0
    # Mínimo provisional
    min = sum(integers)
    # Se recorre el arreglo por medio de índices
    for i in range (0, len(integers)):
        # Se hace una copia del arreglo original en uno auxiliar
        array_sum = list(integers)
        # Se elimina el elemento del arreglo
        array_sum.pop(i)
        # Se suman los 4 valores restantes
        int_sum = sum(array_sum)
        # Se comparan con las sumas anteriores para hallar el máximo y el mínimo
        if int_sum > max:
            max = int_sum
        if int_sum < min:
            min = int_sum
    # Salida: mínima y máxima suma de 4 enteros
    return (str(min) + " "+ str(max))

if __name__ == "__main__":
    # Entrada: arreglo de enteros
    integers = [1,3,5,7,9]
    print (get_minimum_and_maximum_sum(integers))
