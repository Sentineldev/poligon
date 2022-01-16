import math

def definir_vertices_indices(lados):
    grados = 0
    radio = 160
    centro = (210,200) #el mismo procedimiento para conseguir los vertices, solo que añadiendole identificador mediante un diccionario
    vertices = []
    for i in range(lados):
        x = round(radio*math.cos(math.pi/180*grados-math.pi/2)+centro[0])
        y = round(radio*math.sin(math.pi/180*grados-math.pi/2)+centro[1])
        grados+=360/lados
        vertices.append({
            "punto":str(i),
            "coordenada":[x,y]
        })
    vertices2 = []
    return vertices