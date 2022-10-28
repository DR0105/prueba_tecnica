# Entradas: años a cumplir y altura de las velas
years = 5
candles = [2, 8, 8, 3, 10]
# Se coloca la primera vela como máximo provisional
max = candles[0]
for i in candles:
    # Se compara una por una las alturas de la vela para saber cuál es la mayor
    if i > max:
        max = i
# Se inicializa el valor de la cantidad de velas que puede apagar
candles_off = 0
for j in candles:
    # Se comparan de nuevo las alturas de las velas para saber la concurrencia de la más alta
    if j == max:
        # Se aumenta la cantidad cada vez que encuentra la más alta
        candles_off+=1
# Salida: velas que puede apagar
print(candles_off)