#Distintos algoritmos de ordenacion
import math
import random as rand

# mezcla las dos divisiones del mergesort
def merge(izq, der):

    merged = []

    while len(izq) > 0 and len(der) > 0:
        if izq[0] <= der[0]:
            merged.append(izq.pop(0))
        else:
            merged.append(der.pop(0))

    if len(izq) > 0:
        merged = merged + izq
    if len(der) > 0:
        merged = merged + der

    return merged

#mergesort recursivo
def mergesort(lista):

    if len(lista) in (0,1):
        return lista

    mid = math.floor(len(lista)/2)
    izq = mergesort(lista[:mid])
    der = mergesort(lista[mid:])

    if izq[len(izq)-1] < der[0]:
        return izq + der

    return merge(izq, der)

#mediana de primero mitad y ultimo
def mediana(lista, ini, fin):
    primero = lista[ini]
    mitad   = lista[math.floor((fin-ini)/2)]
    ultimo  = lista[fin]

    if min(primero, mitad, ultimo) in (primero, ultimo) and \
       max(primero, mitad, ultimo) in (primero, ultimo):
        return mitad, math.floor((fin-ini)/2)

    elif min(primero, mitad, ultimo) in (mitad, ultimo) and \
       max(primero, mitad, ultimo) in (mitad, ultimo):
       return primero, ini

    else:
       return ultimo, fin

#quicksort recursivo con mediana(primero-mitad-ultimo) como pivote
def quicksort(lista, ini, fin):
    if ini < fin:
        medi, index = mediana(lista, ini, fin)

        if index != fin:
            lista[fin], lista[index] = lista[index], lista[fin]

        piv = particion(lista, medi, ini, fin)
        
        quicksort(lista, ini, piv - 1)
        quicksort(lista, piv + 1, fin)
        print(lista)

#reposiciona los elementos partiendo del pivote y devuelve la posicion de este
def particion(lista, mediana, ini, fin):
    pos_pivote = fin
    while ini<fin:
        while ini<fin and lista[ini]<=mediana:
            ini+=1


        while ini<fin and lista[fin]>=mediana:
            fin-=1

        if ini < fin:
            lista[ini], lista[fin] = lista[fin], lista[ini]


    lista[pos_pivote], lista[ini] = lista[ini], lista[pos_pivote]
    return ini

#comprueba si una lista esta ordenada
def ordenada(lista):
    i=0
    while i< len(lista)-1 and lista[i]<=lista[i+1]:
        i+=1
    return i==len(lista)-1

#stupidSort lmao
def stupidsort(lista):
    if lista == []:
        return []
    while not ordenada(lista):
        '''indices = list(range(0,len(lista)))
        indices_shuffled = rand.shuffle(indices)
        print(indices_shuffled)
        lista_nueva = [1 for i in range(len(lista))]
        print(lista_nueva)
        for i in range(len(lista)):
            lista_nueva[indices_shuffled[i]] = lista[i]'''
        rand.shuffle(lista)

#superstupidsort lmfao
def superstupidsort(lista):
    if lista == []:
        return []
    while not ordenada(lista):
        for i in range(len(lista)):
            indice = rand.randint(0,len(lista)-1)
            lista[indice], lista[i] = lista[i], lista[indice]
