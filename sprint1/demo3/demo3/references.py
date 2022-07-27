def ref_int(number: int) -> None:
    number = 10
    print(f'dentro de ref_int - {number}')


def ref_list(lst: list) -> None:
    # lst.copy()

    lst[0] = 'Novo Valor'
    print(f'dentro de ref_list - {lst}')


def ref_dict(my_dict: list) -> None:
    my_dict['nova_chave'] = 'Novo Valor'
    print(f'dentro de ref_dict - {my_dict}')
