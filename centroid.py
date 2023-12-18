# Script para calcular el centroide de una lista de coordenadas

def encontrar_centroide(coordenadas):
    n = len(coordenadas)
    if n == 0:
        return None

    sum_x = sum(coor[0] for coor in coordenadas)
    sum_y = sum(coor[1] for coor in coordenadas)

    centroide_x = sum_x / n
    centroide_y = sum_y / n

    return (centroide_x, centroide_y)

# Generic Coordinates:
madrid = (40.4168, -3.7038)
gran_canaria = (27.9836, -15.5926)
haarlem = (52.3874, 4.8990)
lastablas = (40.501412355861895, -3.6759313124370827)
algete = (40.59348518385892, -3.4939150293491417)
tetuan = (40.46006964728371, -3.697117475996144)
cobenya = (40.57411313255811, -3.5029425855559206)
elcanya = (40.401718600008515, -3.5585429388276837)

# Lista of coordinates
coordenadas_amigos = [madrid, gran_canaria, haarlem]

centroide_optimo = encontrar_centroide(coordenadas_amigos)

print("El punto óptimo de encuentro es:", centroide_optimo)
