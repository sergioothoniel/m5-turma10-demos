import top_dyno

FILEPATH = 'top_dyno.json'


def main():
    # print(top_dyno.generate_random_dynos_data())
    # top_dyno.create_random_dyno_deck(FILEPATH)
    # p1_deck, p2_deck = top_dyno.generate_players_decks(FILEPATH)
    # print('p1 deck')
    # print(p1_deck)
    # print('p2 deck')
    # print(p2_deck)

    # print(top_dyno.get_random_attr(p1_deck[0]))
    top_dyno.play(FILEPATH)


if __name__ == '__main__':
    main()
