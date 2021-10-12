import Ordenacion as ord
running = True

while(running):

    print("Introduce una lista en formato : 1 2 3 4 5")
    print("con espacio entre los dígitos pero sin espacio a principio y final")
    print("si quieres cerrar escribe q")

    lista_string = ""
    lista_string = input()

    if lista_string == "q":
        running = False

    else:
        lista = []
        try:
            i=0
            while i < (len(lista_string)):
                numero = ""
                while i<len(lista_string) and lista_string[i]!=" ":
                    numero = numero + lista_string[i]
                    i+=1

                lista.append(int(numero))
                i+=1

            list_result = ord.stupidsort(lista)
            print(list_result)

        except ValueError:
            print("Introduce una lista válida")
