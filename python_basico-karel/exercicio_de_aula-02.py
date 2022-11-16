'''
    Objetivo: Fazer com que o Karel pegue todos os beepers presentes e
    retorne exatamente à mesma posição em que estava no início (avenida 1,
    rua 1, olhando para leste)

..
    Licença: GNU GENERAL PUBLIC LICENSE V.3, 2007
    Jander Moreira, 2022
'''

# Suporte ao Karel
from stanfordkarel import *


# Ações do Karel
def main():
    """Karel pega os beeper nas bordas do mundo!"""


# Iniciação do mundo e execução do programa
if __name__ == "__main__":
    run_karel_program("../mundos/beepers_nos_cantos.w")
