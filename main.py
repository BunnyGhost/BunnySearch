from os import system
from time import sleep

def clear(): system('clear')
while True:
    print('''Bunny Search
    █       █
    █████████
    █▄█████▄█
    █▼▼▼▼▼▼██
       Bunny Ghost
    █▲▲▲▲▲▲██
    █████████''')

    itens = ['Port Scanner', 'Brute force', 'Varredura de rede', 'Locaizador de ip', 'Sair']
    for c, item in enumerate(itens):
        print(f'[{c+1}] - {item}')
    escolha = str(input('opção: '))
    clear()
    from data import Port_Scanner, Brute_force, Varredura_de_rede, Localizador_ip
    if escolha == '1':
        Port_Scanner.scanner()
        clear()
    elif escolha == '2':
        Brute_force.brute()
        clear()
    elif escolha == '3':
        Varredura_de_rede.var()
        clear()
    elif escolha == '4':
        Localizador_ip.ip()
        clear()
    elif escolha == '5':
        break
    else:
        print('Comando não identificado...')
        sleep(2)
        clear()
