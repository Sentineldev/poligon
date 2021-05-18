"""
    Proyecto Realizado por Jesus Figuera - Jesus Tineo
                            29660012       28412470

Se tomaron como limites en la aplicacion
*Se aceptan solo numeros de 3 - 12
Esto para evitar que se generen tantas repeticiones y causar un posible crash en la aplicacion
ya que se pueden generar miles y miles de combinaciones.

"""

from tkinter import messagebox
from typing import get_args
from tkinter import *  
from tkinter import ttk
import math
from lados import puntos_lados    #Modulos propios de python y funciones para trabajar con el poligono
from vertices import *              
from vertices_indices import *
from diagonales import *
from combinaciones import *
import time

def poligono_interno_lista(vertices_indices,vertices):
    lista3.delete(0,END)  #Borrando lo que existe actualmente en la lista
    combinaciones1 = combinaciones(vertices_indices,vertices)
    for comb in combinaciones1: #Insertando los vertices donde se forman las figuras en lista
        lista3.insert(END,comb['puntos'])
    


def puntos_lados_diagonales_lista(vertices,lista1,lista2):
    lista1.delete(0,END)
    lista2.delete(0,END)
    puntos = puntos_lados(vertices)
    for punto in puntos:
        lista1.insert(END,punto["Lado"])
    diagonales = indice_diagonales(vertices)
    for diagonal in diagonales:
        lista2.insert(END,diagonal["Lado"])
def dibujar_etiquetas(lados,canvas):
    canvas.delete('texto')
    grados = 0   #Dibujar etiquetas para identificar los vertices por numero
    radio = 170
    centro = (210,200)
    for i in range(lados):
        x = round(radio*math.cos(math.pi/180*grados)+centro[0]) #COordenadas de las etiquetas
        y = round(radio*math.sin(math.pi/180*grados)+centro[1]) #calculo en coordenadas cuadradas de los vertices
        grados+=360/lados  #calculo de los grados
        canvas.create_text(x,y,text=str(i+1),tags='texto') #identificador de la etiqueta text
def dibujar_vertice(vertices,canvas):
    for vertice in vertices: #dibujar el punto de cada vertice en pantalla
        canvas.create_polygon(vertice,outline='red',width=6,fill='white',tags='poligono')


def dibujar_figura(lados,canvas,lista,lista2,p1):
    try:
        int(entrada.get()) #tomar el valor de la primera entrada,  que se encuentra en la pantalla
        canvas.delete('poligono') #borrar el poligono que se encuentre actualmente en la pantalla
        lados = int(lados.get()) #COnvertir lo digitado por el usuario en entero
        if(lados >=3 and lados <=12 and int(lados)): #verificar que sea un numero entre 3 y 12
            lista3.delete(0,END) #borrar lo que se encuentre en la lista con las coordenadas de las figuras generadas apartir de los vertices del ppoligono
            global vertices,vertices_indices #variables globales para trabajar las listas de vertices
            vertices = definir_vertices(lados) #definir los vertices del poligono
            vertices_indices = definir_vertices_indices(lados) #definir los vertices pero con un identificador
            dibujar_etiquetas(lados,canvas) #dibujar las etiquetas que identificar los vertices
            canvas.create_polygon(vertices,outline='white',width=4,fill='purple',tags='poligono') #crear el poligono
            dibujar_vertice(vertices,canvas) #dibujar los vertices del poligono
            puntos_lados_diagonales_lista(vertices,lista,lista2) #mostrar en la lista los vertices de los lados y las diagonales del poligono
            label1.config(text=len(vertices),foreground='white',bg='#263d42') #configurar las etiquetas que muestra el numero de lados y diagonales
            label1.place(x=110,y=250)
            label2.config(text=len(indice_diagonales(vertices)),fg='white',bg='#263d42')
            label2.place(x=140,y=270)
        else:
            canvas.delete('poligono') #caso de que no se cumplan las condiciones limpiar la interfaz y enviar un mensaje de error
            canvas.delete('texto')
            lista.delete(0,END)
            lista2.delete(0,END)
            lista3.delete(0,END)
            messagebox.showerror(message='Digite numeros entre 3-12, enteros.')
    except:
        messagebox.showerror(message='Error intente denuevo')

def generar_interno(vertices): #generar la lista con las coordenadas de las figuras dentro del poligono principal
    try:
        vertices = int(vertices.get())
        if(vertices <= int(entrada.get()) and vertices >=3 ):
            poligono_interno_lista(vertices_indices,vertices)
            label3.config(text=len(combinaciones(vertices_indices,vertices)),foreground='white',bg='#263d42')
            label3.place(x=130,y=250)
        else:
            messagebox.showerror(message="Debe ser mayor que 3 o menor que el numero de vertices de el poligono principal")
    except:
        messagebox.showerror(message='Error intente denuevo.') #mensajes de error

def seleccionar_lado(ev): #mostrar el lado seleccionado en lista por el usuario
    try:
        canvas.delete('lado') #borrar el lado que se encuentre actualmente para mostrar el seleccionado por el usuario
        puntos = puntos_lados(vertices)
        for punto in puntos:
            if punto["Lado"] == lista.selection_get(): #comparar si el identificador dentro del diccionario es igual al seleccionado por el usuario
                canvas.create_polygon(punto["punto"],outline='red',width=5,fill='purple',tags='lado')
    except:
        pass

def seleccionar_diagonal(ev): #mostrar la diagonal seleccionada en lista por el usuario
    try:
        canvas.delete('diagonal') #borrar la diagonal que se encuentre actualmente para mostrar la seleccionada
        diagonales = indice_diagonales(vertices)
        for diagonal in diagonales:
            if diagonal["Lado"] == lista2.selection_get(): #comparar si el identificador en el diccionario es igual al seleccionado por el usuario en la lista
                canvas.create_polygon(diagonal["punto"],outline='red',width=5,fill='purple',tags='diagonal')      #mostrar la diagonal
    except:
        pass
def seleccionar_interno(ev): #mostrar la figura interna seleccionada en lista por el usuario
    try:
        canvas.delete('figura') #borrar la ffigura actual
        combinaciones1 = combinaciones(vertices_indices,int(entrada2.get()))
        for comb in combinaciones1:
            if comb['puntos'] == lista3.selection_get(): #verificar que el identificador sea igual
                canvas.create_polygon(comb['coordenadas'],outline='red',width=5,fill='green',tags='figura')
    except:
        pass
def crear_accesorios_opc2(p2,canvas): #crear los botones y entradas de la segunda pestaña
    global entrada2
    entrada2 = Entry(p2,width=10,font=('arial',20))
    entrada2.place(x=10,y=30)
    boton2 = Button(p2,text='Generar',width=10,command=lambda:generar_interno(entrada2))
    boton2.place(x=30,y=80)

    #crear lista
    global lista3
    etiqueta_lista = Label(p2,text="Figuras",bg='#263d42',fg='white')
    etiqueta_lista.place(x=15,y=120)
    frame_lista = Frame(p2,width=85,height=125,bg='white')
    frame_lista.place(x=5,y=140)
    scrollbar = Scrollbar(frame_lista,orient=VERTICAL)
    lista3 = Listbox(frame_lista,width=15,height=5,yscrollcommand=scrollbar.set)
    scrollbar.pack(side=RIGHT,fill=Y)
    lista3.pack()
    lista3.bind('<<ListboxSelect>>',seleccionar_interno)
    
    #etiquetas
    Label(p2,text="Numero de figuras:",fg='white',bg='#263d42').place(x=3,y=250)

def crear_accesorios_opc1(p1,canvas):
    global entrada
    entrada = Entry(p1,width=10,font=('arial',20))
    entrada.place(x=10,y=30)
    #crear los botones y entradas de la primera pestaña

    #Crear lista
    global lista
    etiqueta_lista = Label(p1,text="Lados",bg='#263d42',fg='white')
    etiqueta_lista.place(x=15,y=120)
    frame_lista = Frame(p1,width=85,height=125,bg='white')
    frame_lista.place(x=5,y=140)
    scrollbar = Scrollbar(frame_lista,orient=VERTICAL)
    lista = Listbox(frame_lista,width=8,height=5,yscrollcommand=scrollbar.set)
    scrollbar.pack(side=RIGHT,fill=Y)
    lista.pack()
    lista.bind('<<ListboxSelect>>',seleccionar_lado)

    #Crear segunda lista
    global lista2
    etiqueta_lista2 = Label(p1,text='Diagonales',bg='#263d42',fg='white')
    etiqueta_lista2.place(x=95,y=120)
    frame_lista2 = Frame(p1,width=85,height=125,bg='white')
    frame_lista2.place(x=95,y=140)
    scrollbar2 = Scrollbar(frame_lista2,orient=VERTICAL)
    lista2 = Listbox(frame_lista2,width=8,height=5,yscrollcommand=scrollbar2.set)
    scrollbar2.pack(side=RIGHT,fill=Y)
    lista2.pack()
    lista2.bind('<<ListboxSelect>>',seleccionar_diagonal)

    #etiquetas
    etiqueta_lados = Label(p1,text='Numero de lados:',bg='#263d42',fg='white',font=('Arial',10))
    etiqueta_lados.place(x=5,y=250)
    etiqueta_diagonales = Label(p1,text='Numero de Diagonales:',bg='#263d42',fg='white',font=('Arial',9))
    etiqueta_diagonales.place(x=5,y=270)

    #crear boton
    boton = Button(p1,text='Generar',width=10,command=lambda:dibujar_figura(entrada,canvas,lista,lista2,p1))
    boton.place(x=30,y=80)

def crear_ventana_botones(): #crear la ventana principal
    global canvas,frame,p1,p2
    global puntos
    global ventana_pes
    global label1,label2,label3
    ventana = Tk()
    ventana.title("Poligono")
    ventana.geometry("600x400")

    canvas = Canvas(ventana,bg='white')
    canvas.place(relwidth=0.7,relheight=1,x=180)

    frame = Frame(ventana,bg='white')
    frame.place(relwidth=0.3,relheight=1)

    ventana_pes = ttk.Notebook(frame)
    ventana_pes.pack(fill='both',expand='yes')

    p1 = Frame(ventana_pes,bg='#263d42')
    p2 = Frame(ventana_pes,bg='#263d42')
    crear_accesorios_opc1(p1,canvas)
    crear_accesorios_opc2(p2,canvas)

    ventana_pes.add(p1,text='Opcion1')
    ventana_pes.add(p2,text='Opcion2')
    label1 = Label(p1)
    label2 = Label(p1)
    label3 = Label(p2)
    ventana.mainloop()



def main():
    crear_ventana_botones()

if __name__ == '__main__':
    main()


