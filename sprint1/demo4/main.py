import json

from utils.example_1 import func_1
from utils.json_handler import read_json, write_json

# print('dunder name main.py -> ', __name__)

FILEPATH = 'db.json'


def main():
    # func_1()
    # try:
    #     print(read_json())
    # # except json.JSONDecodeError:
    # #     print('json decode error')
    # # except FileNotFoundError:
    # #     print('file not found error')
    # except (json.JSONDecodeError, FileNotFoundError):
    #     print('json error')

    data = read_json(FILEPATH)
    user = {'name': "Lucira"}
    user2 = {'name': "Marcelo"}
    data.append(user)
    data.append(user2)

    print(data)

    write_json(FILEPATH, data)


if __name__ == '__main__':
    main()
