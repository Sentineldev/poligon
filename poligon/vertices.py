import math
def definir_vertices(lados):
    grados = 0 #grados
    radio = 160 #distancia entre los puntos
    centro = (210,200) #punto central del poligono
    vertices = [] #lista para guardar las coordenadas
    for i in range(lados):
        x = round(radio*math.cos(math.pi/180*grados-math.pi/2)+centro[0]) #se calcula la posicion x en la pantalla sumandole el centro
        y = round(radio*math.sin(math.pi/180*grados-math.pi/2)+centro[1])# secalcula la posicion de y en la pantalla sumandole el centro
        grados+=360/lados #y los grados para la separacion que tendran los vertices unos de otros
        vertices.append([])
        vertices[i].append(x) #se añaden en lista
        vertices[i].append(y)
    return vertices