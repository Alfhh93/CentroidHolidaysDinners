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

# Lista of coordinates
coordenadas_amigos = [madrid, gran_canaria, haarlem]

centroide_optimo = encontrar_centroide(coordenadas_amigos)

print("El punto óptimo de encuentro es:", centroide_optimo)
