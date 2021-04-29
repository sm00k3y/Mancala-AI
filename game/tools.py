

def draw_board(a_player, b_player, a_basket, b_basket):
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


def is_int(string):
    try:
        int(string)
        return True
    except ValueError:
        return False
