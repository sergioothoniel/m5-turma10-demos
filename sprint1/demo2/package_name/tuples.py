def tuple_fundamentals():
    # my_tuple = (1,)
    my_tuple = ('String', True, 1, 3.7, ['2', 3])
    print(my_tuple)
    # print(type(my_tuple))

    # my_tuple_2 = tuple('Minha String')
    # print(my_tuple_2)

    print(my_tuple[0])
    print(my_tuple[-1])
    print(my_tuple[1:3])

    # Imutável
    # my_tuple[0] = "Nova String"

    my_lst = list(my_tuple)
    my_lst[0] = "Nova String"
    my_tuple_2 = tuple(my_lst)
    print(my_tuple_2)
