# from demo3.references import ref_int
from demo3 import comprehensions, packing_unpacking, references


def main():
    # Tipo de dado imutável
    # n = 5
    # print(f'antes de chamar ref_int - {n}')
    # references.ref_int(n)
    # print(f'depois de chamar ref_int - {n}')

    # Tipo de dado mutável
    # Passagem por referencia
    # lista = [1, 2, 3]
    # print(f'antes de chamar ref_list - {lista}')
    # references.ref_list(lista)
    # print(f'depois de chamar ref_list - {lista}')

    # Tipo de dado mutável
    # Passagem por referencia
    # d = {'name': "Chrystian"}
    # print(f'antes de chamar ref_dict - {d}')
    # references.ref_dict(d)
    # print(f'depois de chamar ref_dict - {d}')

    # Packing Unpacking
    # packing_unpacking.func_args(1, 2, 3, 5)
    # Sequencia
    # lista = [10, 20, 30]
    # tupla = (10, 20, 30, 100)
    # string = 'aaa'
    # packing_unpacking.func_args(lista)
    # packing_unpacking.func_args(*lista)
    # packing_unpacking.func_args(*tupla)
    # packing_unpacking.func_args(*string)
    # packing_unpacking.func_args(*lista, *tupla)

    # Referencia args
    # lista = [10, 20, 30]
    # packing_unpacking.func_args_2(*lista)
    # print(lista)

    # d = {'name': "chrystian"}
    # packing_unpacking.func_kwargs(**d)
    # packing_unpacking.func_kwargs(**{'name': "chrystian"})
    # packing_unpacking.func_kwargs(name='Chrystian', age=30)

    # Comprehensions
    # result = comprehensions.list_c(10)
    # print(result)

    # Zip
    # k = ['name', 'age']
    # v = ['chrystian', '30']

    k = ["John"]
    v = ["25"]
    # z = zip(x, y)
    # comprehensions.zip_example(k, v)
    comprehensions.zip_example(values=v, keys=k)


main()
