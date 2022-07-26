def list_fundamentals():
    my_lst = [1, "String", True, 3.8, ["Outra", "Lista"], 'ultimo item']
    print(my_lst)
    print(type(my_lst))

    # my_lst_2 = list('uma string')
    # print(my_lst_2)

    # Tamanho
    # print(len(my_lst))

    # print(my_lst[0])
    # print(my_lst[-1])
    # print(my_lst[-1][0])
    # print(my_lst[-1][1])

    # Slicing
    # print(my_lst[1:3])
    # print(my_lst[:3])
    # print(my_lst[::-1])

    my_lst[0] = 'Novo Valor'
    print(my_lst)

    # my_lst.append(-8000)
    # print(my_lst)

    removed_item = my_lst.pop()
    print(my_lst)
    print(removed_item)

    my_lst.remove("String")
    print(my_lst)

    # Copiando lista
    # new_lst = my_lst[:]
    # print(new_lst)
    # print(new_lst.copy())

    my_lst.clear()
    print(my_lst)


def list_looping():
    names = ['Chrystian', "Lucira", "Alexandre", "Marcelo", "Alex"]

    # for name in names:
    #     print(name)

    for index, name in enumerate(names):
        print(index, name)
