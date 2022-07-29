# from top_dyno import (create_random_dyno_deck, generate_players_decks,
#                       generate_random_dynos_data)

# from .deck import (create_random_dyno_deck, generate_players_decks,
#                    generate_random_dynos_data)

import random

from utils import print_card_vs_card

from . import create_random_dyno_deck, generate_players_decks


def get_random_attr(card: dict) -> str:
    # name, strength, agility, heigth
    card_keys = [key for key in card.keys() if key != 'name']

    # rand_int = random.randint(0, len(card_keys) - 1)

    # return card_keys[rand_int]

    return random.choice(card_keys)


def play(filepath: str) -> None:
    create_random_dyno_deck(filepath)
    p1_deck, p2_deck = generate_players_decks(filepath)

    # p1_deck e p2_deck são listas de mesmo tamanho
    for index, p1_card in enumerate(p1_deck):
        # print('p1_card:')
        # print(p1_card)

        # print('p2_card:')
        # # p2_deck[0]
        # print(p2_deck[index])
        # p2_deck[index]
        attr_to_compare = get_random_attr(p1_card)
        p2_card = p2_deck[index]

        # p1_card é um dict
        # x = 'agility'
        # p1_card[x]

        # quem vs quem

        print_card_vs_card(p1_card, p2_card, attr_to_compare)
