def fundamentals():
    # my_dict = {"chave": "valor", 1: True}
    # print(my_dict)
    # print(type(my_dict))

    my_dict = {"chave": "valor", "chave": "valor_2"}
    print(my_dict)

    # my_dict_2 = dict(chave='valor', chave2='valor')
    # print(my_dict_2)

    # print(my_dict['chave'])
    # my_dict['chave'] = 'novo valor'
    # print(my_dict['chave'])
    # print(my_dict)

    # my_dict['nova_chave'] = 'algum valor'
    # print(my_dict)

    # my_dict.update({'nova_chave': 'novo valor nova chave', "modulo": 'M5'})
    # print(my_dict)

    # print(my_dict['chave_nao_existente'])
    my_value = my_dict.get('chave_nao_existente', 'CHURROS')
    print(my_value)


def dict_looping():
    user = {'name': 'Chrystian', 'age': '30', 'module': 'M5'}
    # print(user)
    # print(user.keys())
    # print(type(user.keys()))
    # print(list(user.keys()))

    # print(user.values())
    # print(type(user.values()))
    # print(list(user.values()))

    # print(user.items())
    # print(type(user.items()))
    # print(list(user.items()))
    # print(dict(user.items()))

    # for key in user.keys():
    #     print(key)

    # for value in user.values():
    #     print(value)

    for unknown in user.items():
        print(type(unknown))
        print(unknown)

    # for key, value in user.items():
    #     print(type(key))
    #     print(type(value))
    #     print(key, value)
