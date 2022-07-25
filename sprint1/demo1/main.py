# Comentário

"""
    Funções
"""


# def greetings():
#     return 'olá M5'


# print(type(greetings))
# print(greetings())


"""
    Tipos Primitivos
"""

# # Inteiro
# num = 10
# print(num)
# print(type(num))

# # Float
# f_num = 5.2
# print(f_num)
# print(type(f_num))

# # String
# string = "uma string"
# print(string)
# print(type(string))

# # Booleano
# t_boolean = True
# f_boolean = False

# print(t_boolean)
# print(type(t_boolean))

# print(f_boolean)
# print(type(f_boolean))

# Tipagem forte
# print(1 + '1')


"""
    Estruturas Condicionais
"""

# x = 5

# if x > 5:
#     print('x é maior que 5')
# elif x == 5:
#     print('x é igual a 5')
# else:
#     print('x é menor que 5')

# y = 10

# # 2 iguais
# if x == 5 and y == 10:
#     print('x = 5 E y = 10')

# if x == 5 or y == 10:
#     print('x = 5 OU y = 10')

# if not x == 20:
#     print('x NÃO é 20')

"""
    Estruturas de Repetição
"""

my_str = 'olá M5!'

# for char in my_str:
#     # print(char, end='+')
#     print(char)

for index, item in enumerate(my_str, 1):
    # print(type(item))
    # if item == 'M':
    #     print(item)
    # print(index, item)
    # print(index)
    # print(item)
    # pass
    ...


# for num in range(1, 10, 2):
#     print(num)


# for num in range(11):
#     print(num)
#     if num == 3:
#         break

# z = 0

# while z < 3:
#     print('loop while ', z)
#     z += 1


for num in range(11):
    if num == 3:
        continue
    print(num)
