from datetime import datetime as dt


def print_card_vs_card(p1_card: dict, p2_card: dict, attr_to_compare: str) -> None:
    # TODO:
    # Adicionar hora atual que o jogo inicou

    print(f"{p1_card['name']} VERSUS {p2_card['name']}")

    print(f"{attr_to_compare}: {p1_card[attr_to_compare]} VERSUS", end=' ')
    print(f"{attr_to_compare}: {p2_card[attr_to_compare]}")

    if p1_card[attr_to_compare] > p2_card[attr_to_compare]:
        print(f"{p1_card['name']} wins!", end='\n\n')
    elif p2_card[attr_to_compare] > p1_card[attr_to_compare]:
        print(f"{p2_card['name']} wins!", end='\n\n')
    else:
        print('draw')
