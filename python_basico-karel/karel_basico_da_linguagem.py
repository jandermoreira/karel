"""
Karel: exemplificação da estrutura da linguagem
    - Documentação
    - Erros de sintaxe
    - Erros de execução
    - Execução sequencial
    - Execução repetida
    - Execução condicional

..
    Licença: GNU GENERAL PUBLIC LICENSE V.3, 2007
    Jander Moreira, 2021, 2022
"""

# Suporte ao Karel
from stanfordkarel import *


# Ações do Karel
def main():
    """
    Aqui são definidas as ações que o robô irá executar
    """
    move()
    move()
    move()


# Iniciação do mundo e execução do programa
if __name__ == "__main__":
    run_karel_program()
