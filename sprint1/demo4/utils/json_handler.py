import json


def read_json(filepath: str) -> list[dict]:
    # Forma manual
    # file = open('db.json', 'r')
    # json_data = json.load(file)
    # file.close()
    # return json_data

    # Forma com gerenciador de contexto
    with open(filepath, 'r') as file:
        # posso conter lógica qualquer
        # json_data = json.load(file)

        # return json_data

        return json.load(file)


def write_json(filepath: str, payload: list):
    with open(filepath, 'w') as file:
        json.dump(payload, file, indent=2)
