from tkinter import *

def puntos_lados(vertices):
    vertices_lados = []
    for i in range(len(vertices)):
        if i+1 < len(vertices): # setoman los valores de 0 y 0+1 para generar los lados
            vertices_lados.append({})
            vertices_lados[i] = {
                "Lado":str(i+1)+" - "+str(i+2),
                "punto":(vertices[i][0],vertices[i][1],vertices[i+1][0],vertices[i+1][1]),
            }
    punto1 = vertices[-1]
    punto2 = vertices[0]  #se le añade identificadores a los lados para ser mostrados en lista
    lado1 = vertices_lados[0]["Lado"][0]+"-"
    cadena = vertices_lados[-1]["Lado"].split()
    lado1 = cadena[2]+" - "+vertices_lados[0]["Lado"][0]
    dicti = {
        "Lado":lado1,
        "punto":(punto1,punto2)
    }
    vertices_lados.append(dicti)
    return vertices_lados