# import absoluto
from utils.example_2 import func_2

# import relativo
# from .example_2 import func_2

# import absoluto (executando módulo)
# from example_2 import func_2

# print('dunder name example_1.py -> ', __name__)


def func_1():
    func_2()
    print('func_1 execution')
