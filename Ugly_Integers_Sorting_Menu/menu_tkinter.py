try:
    from tkinter import *
except ImportError:
    print("No se ha encontrado tkinter en el ordenador")

import Ordenacion as ord
from time import time
import multiprocessing
import re

#iniciar tkinter
ventana = Tk()
ventana.resizable(width=False,height=False)
ventana.geometry("1000x600")

lista_string = StringVar(value="aqui va la lista")
algoritmo    = IntVar(value=0)
tipo         = StringVar(value="int")
lista = []
tiempo = 0

#activado al pulsar aceptar
def introducir_lista():
    global lista 
    global tipo
    valor = entry_lista.get()

    del lista[:]
    '''i = 0
    while i< len(valor):
        numero = ""
        while i<len(valor) and valor[i]!=" ":
            if(valor[i] != " "):
                numero = numero + valor[i]
                i+=1
                print(valor[i])

        if tipo.get()=="int":
            lista.append(int(numero))
        else:
            lista.append(numero)
        i+=1'''
    #if tipo==int:
    lista = [int(num) for num in re.findall(r"\d+", valor)]
    #else:
        #lista = [num for num in re.findall(r"\d+", valor)]

    if(len(lista)>15):
        label_selec.config(font=(None,10))
    else:
        label_selec.config(font=(None,20))

    if(len(lista)>20):
        label_resultado.config(font=(None,10))
    else:
        label_resultado.config(font=(None,20))

    label_selec.config(text=str(lista))
    

#activado al pulsar eliminar 
def eliminar_lista():
    global lista
    label_selec.config(text="Aquí se mostrará la lista seleccionada")
    lista = []
    entry_lista.delete(0, 'end')
 
#ordena la lista
def ordenar():
    try:
        global algoritmo
        global lista
        button_del.config(state=DISABLED)
        radio_merge.config(state=DISABLED)
        radio_quick.config(state=DISABLED)
        radio_stupid.config(state=DISABLED)
        radio_super.config(state=DISABLED)
        button_acep.config(state=DISABLED)
        t1 = time()
        
        if algoritmo.get() == 0: 
            ord.quicksort(lista,0,len(lista)-1)
            print(lista)
        elif algoritmo.get() == 1:
            lista = ord.mergesort(lista).copy()
        elif algoritmo.get() == 2:
            ord.stupidsort(lista)
        elif algoritmo.get() == 3:
            ord.superstupidsort(lista)

        t2 = time()
        lista_fin = lista
        label_resultado.config(text=str(lista_fin))
        label_tiempo_res.config(text=str(t2-t1))
        entry_lista.delete(0, 'end')
        label_selec.config(text="Aquí se mostrará la lista seleccionada")
        button_acep.config(state=NORMAL)
        radio_merge.config(state=NORMAL)
        radio_quick.config(state=NORMAL)
        radio_stupid.config(state=NORMAL)
        radio_super.config(state=NORMAL)
        button_del.config(state=NORMAL)

    except:
        label_resultado.config(text="ABORTADO!!")
        del lista[:]
        entry_lista.delete(0, 'end')
        label_selec.config(text="Aquí se mostrará la lista seleccionada")

def parar():
    raise Exception("ABORTAR!")

#crear los distintos frames
frame_lista     = Frame(ventana,bg="white smoke",relief=RIDGE,borderwidth=3)
frame_algoritmo = Frame(ventana,bg="white smoke",relief=RIDGE,borderwidth=3)
frame_resultado = Frame(ventana,bg="white smoke",relief=RIDGE,borderwidth=3)

#definir su tamaño y lo que ocupan(esto último mediante grid)
frame_lista.config(width=500,height=300,relief=RIDGE)
frame_algoritmo.config(width=500,height=300)
frame_resultado.config(width=1000,height=300)

frame_lista.grid(row=0,column=0,sticky="nsew")
frame_algoritmo.grid(row=0,column=1)
frame_resultado.grid(row=1,column=0,columnspan=2,sticky="nsew")

#frame de la lista
entry_lista  = Entry(frame_lista,width=60)
#radio_string = Radiobutton(frame_lista,text="String",bg="white smoke",variable=tipo,value="str")
#radio_int    = Radiobutton(frame_lista,text="int",bg="white smoke",variable=tipo,value="int")
button_del   = Button(frame_lista,text="Eliminar",command=eliminar_lista)
button_acep  = Button(frame_lista,text="Aceptar",command=introducir_lista)
label_intro1  = Label(frame_lista,font=(None,11),bg="white smoke",text="Introduce la lista a continuación")
label_selec  = Label(frame_lista,bg="white smoke",text="Aquí se mostrará la lista seleccionada",font=(None,15))
label_intro2  = Label(frame_lista,bg="white smoke",text="separando cada elemento con un espacio en blanco:",font=(None,11))
#label_tipo   = Label(frame_lista,bg="white smoke",text="Elige el tipo de dato")

entry_lista.place(x=10,y=80)
button_del.place(x=10,y=110)
button_acep.place(x=100,y=110)
label_intro1.place(x=10, y=20)
label_intro2.place(x=10, y=40)
label_selec.place(x=10,y=160)
#label_tipo.place(x=200,y=20)
#radio_int.place(x=200,y=50)
#radio_string.place(x=200,y=80)

#frame del algoritmo
radio_quick  = Radiobutton(frame_algoritmo,text="QUICKSORT",bg="white smoke",variable=algoritmo,value=0)
radio_merge  = Radiobutton(frame_algoritmo,text="MERGESORT",bg="white smoke",variable=algoritmo,value=1)
radio_stupid = Radiobutton(frame_algoritmo,text="STUPIDSORT",bg="white smoke",variable=algoritmo,value=2)
radio_super  = Radiobutton(frame_algoritmo,text="SUPERSTUPIDSORT",bg="white smoke",variable=algoritmo,value=3)
label_algoritmo = Label(frame_algoritmo,text="Selecciona el algoritmo a utilizar:",bg="white smoke",font=(None,11))

radio_quick.place(x=100,y=80)
radio_merge.place(x=100,y=110)
radio_stupid.place(x=100,y=140)
radio_super.place(x=100,y=170)
label_algoritmo.place(x=10,y=20)

#frame del resultado
button_ordenar   = Button(frame_resultado,text="ORDENAR!",command=ordenar)
label_resultado  = Label(frame_resultado,text="Aquí aparecerá la lista ordenada",font=(None,20),bg="white smoke")
label_tiempo     = Label(frame_resultado,text="Tiempo empleado:",bg="white smoke")
label_tiempo_res = Label(frame_resultado, text="")
#button_parar     = Button(frame_resultado,text="STOP!",comman=parar)
#label_parar      = Label(frame_resultado, text="Si tarda mucho pulsa este botón para terminar:")

button_ordenar.config(height=4,width=15)
label_resultado.config(width=50)
button_ordenar.place(x=435,y=30)
label_resultado.place(x=10,y=170)
label_tiempo.place(x=10, y=210)
#button_parar.place(x=700, y=50)
#label_parar.place(x=700, y=30)
label_tiempo_res.place(x=450, y=210)

ventana.mainloop()
        

    