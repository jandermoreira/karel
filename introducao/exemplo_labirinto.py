"""
Karel: pegar beepers ao longo do caminho

..
    Licença: GNU GENERAL PUBLIC LICENSE V.3, 2007
    Jander Moreira, 2022
"""

# Suporte ao Karel
from stanfordkarel import *

def turn_right():
    turn_left()
    turn_left()
    turn_left()

# Ações do Karel
def main():
    """
    Ações
    """
    while front_is_clear() or left_is_clear() or right_is_clear():
        if beepers_present():
            pick_beeper()

        if front_is_clear():
            move()
        elif left_is_clear():
            turn_left()
        elif right_is_clear():
            turn_right()

    while beepers_in_bag():
        put_beeper()
    turn_left()
    turn_left()
    move()

# Iniciação do mundo e execução do programa
if __name__ == "__main__":
    run_karel_program("../mundos/labirinto_3.w")