def indice_diagonales(vertices):
    diagonales = [] #lista para coordenadas de los diagonales
    for i in range(len(vertices)): 
        aux = i+1# se inicializa una variable auxiliar un numero mayor al inicio del bucle
        for j in range(len(vertices)-3): #se hace un ciclo iterativo desde el vertice, y pasando por todos los vertices
            if aux+1 < len(vertices): # severifica que el numero qu contengan la variabele auxiliar sea menor que el tamaño de la lista y no generar un error
                diagonal = (vertices[i],vertices[aux+1]) # se añade la coordenada en el primer indice de la lista, y la coordenada dos valores siguiente en el indice de lista
                diagonales.append({
                    "Lado":str(i+1)+" - "+str(aux+2),
                    "punto":diagonal
                })
                aux+=1
        
    return diagonales