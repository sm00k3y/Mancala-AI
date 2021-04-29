

def draw_board(a_player, b_player, a_basket, b_basket):
    print_hint_board()
    print("\n             GAME BOARD")
    print("---------------------------------------")
    print("|      |", end="")
    for i in range(6):
        print(f" {a_player[5 - i]} |", end="")
    print("      |")

    print(f"|  {a_basket}   |-----------------------|   {b_basket}  |")

    print("|      |", end="")
    for i in range(6):
        print(f" {b_player[i]} |", end="")
    print("      |")
    print("---------------------------------------\n")


def print_hint_board():
    print("             HINT BOARD")
    print("---------------------------------------")
    print("|      |", end="")
    for i in range(6):
        print(f" {6 - i} |", end="")
    print("      |")

    print(f"|      |-----------------------|      |")

    print("|      |", end="")
    for i in range(6):
        print(f" {i + 1} |", end="")
    print("      |")
    print("---------------------------------------")


def is_int(string):
    try:
        int(string)
        return True
    except ValueError:
        return False
