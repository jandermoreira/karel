'''
Karel: apresentação do robô

..
    Licença: GNU GENERAL PUBLIC LICENSE V.3, 2007
    Jander Moreira, 2022
'''

# Suporte ao Karel
from stanfordkarel import *


def turn_right():
    turn_left()
    turn_left()
    turn_left()


# Ações do Karel
def main():
    """
    Aqui são definidas as ações que o robô irá executar
    """
    move()
    move()
    turn_left()
    move()
    move()
    turn_right()
    move()


# Iniciação do mundo e execução do programa
if __name__ == "__main__":
    run_karel_program()
