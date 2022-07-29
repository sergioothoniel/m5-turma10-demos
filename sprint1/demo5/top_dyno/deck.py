import random

from utils import read_json, write_json

# from utils.json_handler import read_json, write_json

DYNO_NAMES = ("Alênossauro Rex", "Marcerátops", "Lucirodonte", "Alexraptor")


def generate_random_dynos_data() -> list[dict]:
    # dyno_cards = []

    # for dyno_name in DYNO_NAMES:
    #     dyno_dict = {
    #         "name": dyno_name,
    #         "strength": random.randint(1, 10),
    #         "agility": round(random.uniform(0, 10), 1),
    #         "heigth": round(random.uniform(0, 10), 2)
    #     }
    #     dyno_cards.append(dyno_dict)

    # return dyno_cards

    return [
        {
            "name": dyno_name,
            "strength": random.randint(1, 10),
            "agility": round(random.uniform(0, 10), 1),
            "heigth": round(random.uniform(0, 10), 2)
        }
        for dyno_name in DYNO_NAMES
    ]


def create_random_dyno_deck(filepath: str) -> None:
    generated_dynos = generate_random_dynos_data()

    write_json(filepath, generated_dynos)


def generate_players_decks(filepath: str) -> tuple[list]:
    dyno_deck = read_json(filepath)

    # Inteiro
    split_deck = len(dyno_deck) // 2

    random.shuffle(dyno_deck)

    # Retornar uma tupla com 2 decks
    return (dyno_deck[:split_deck], dyno_deck[split_deck:])
    # return (dyno_deck[:2], dyno_deck[2:])
