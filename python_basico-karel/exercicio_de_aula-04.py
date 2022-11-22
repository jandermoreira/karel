"""
Objetivo: Fazer com que o Karel pegue todos os beepers presentes e fique
na retorne à sua posição inicial (avenida 1, rua 1, virado para leste)

..
    Licença: GNU GENERAL PUBLIC LICENSE V.3, 2007
    Jander Moreira, 2022
"""

# Suporte ao Karel
from stanfordkarel import *


# Ações do Karel
def main():
    """Karel pega os beeper no mundo!"""


# Iniciação do mundo e execução do programa
if __name__ == "__main__":
    # Commente uma linha e descomente a outra para verificar se seu
    # programa executa nos três mundos
    run_karel_program("../mundos/todos_os_beepers_1.w")
    # run_karel_program("../mundos/todos_os_beepers_2.w")
    # run_karel_program("../mundos/todos_os_beepers_3.w")
    # run_karel_program("../mundos/todos_os_beepers.w")
