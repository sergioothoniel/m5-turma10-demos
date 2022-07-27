# Referencia de listas
lista = [1, 2, 3]
id(lista)

lista_2 = lista
lista

lista_2

id(lista)

id(lista_2)

id(lista) == id(lista_2)

lista_2[0]

lista_2[0] = 100
lista_2

lista

lista is lista_2

# Copy (copia rasa)
lista = [1, 2, 3]
lista_copy = lista.copy()

lista
lista_copy

lista is lista_copy

lista_copy[0] = 100

lista_copy
lista

# Copy com estrutura profunda
lista = [1, 2, ['lista', 'interna']]
lista_copy = lista.copy()

lista
lista_copy

lista_copy[2][0]

lista_copy[2][1]

lista is lista_copy

lista_copy[0] = 100

lista_copy
lista

lista_copy[2][0] = 'teste'

lista_copy
lista


# Deepcopy
from copy import deepcopy

lista = [1, 2, ['lista', 'interna']]
lista_copy = deepcopy(lista)

lista
lista_copy

lista is lista_copy

lista_copy[0] = 100

lista_copy
lista

lista_copy[2][0] = 'teste'

lista_copy
lista
