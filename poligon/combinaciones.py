from itertools import combinations

def combinaciones(vertices,lados):
    combinaciones = [] #una lista para guardar las combinaciones
    for i in combinations(vertices,lados): #se haran combinaciones dependiendo del numero de vertices ingresado por el usuario
        combinaciones.append(i)#se guardan en una lista las combinaciones generadas 
    combinaciones_indices = []
    puntos = ''  # se toman las mismas combinaciones y se les añade un identificador para ser mostrado en lista
    coordenadas = []
    combinaciones2 = []
    for i in range(len(combinaciones)):
        for j in range(len(combinaciones[i])):
            puntos += str(combinaciones[i][j]['punto']+" - ")
            coordenadas.append([
                combinaciones[i][j]["coordenada"]
            ])
        combinaciones2.append({
            "puntos":puntos,
            "coordenadas":coordenadas
        })
        puntos = ''
        coordenadas = []
    return combinaciones2

