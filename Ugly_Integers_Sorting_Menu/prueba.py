import Ordenacion as ord
import re
string = "5   1 2 33 4 5"
lista = [int(num) for num in re.findall(r"\d+", string)]

'''lista = [11,10,9]
ord.quicksort(lista,0,2)'''
for i in lista:
    print(i)