import random

print('JOGO: PEDRA, PAPEL OU TESOURA!')
while True:

# Lista de strings
    p_p_t = ["PEDRA 🪨", "PAPEL 📜", "TESOURA ✂️"]

# Escolha aleatória pelo Computador
    chose_computer = random.choice(p_p_t)

# Escolha pelo Jogador
    chose_player = input('O que você escolhe: ')

# Revelação da Escolha do Computador
    print("O Computador Escolheu:", chose_computer)

# Condições em que o jogador escolhe PEDRA
    if chose_player.capitalize() == 'Pedra' and chose_computer == p_p_t[0]:
        print('Empate.')
    elif chose_player.capitalize() == 'Pedra' and chose_computer == p_p_t[1]:
        print('O Computador venceu.')
    elif chose_player.capitalize() == 'Pedra' and chose_computer == p_p_t[2]:
        print('Você venceu.')

# Condições em que o jogador escolhe PAPEL

    elif chose_player.capitalize() == 'Papel' and chose_computer == p_p_t[0]:
        print('Você venceu.')
    elif chose_player.capitalize() == 'Papel' and chose_computer == p_p_t[1]:
        print('Empate.')
    elif chose_player.capitalize() == 'Papel' and chose_computer == p_p_t[2]:
        print('O Computador venceu.')

# Condições em que o jogador escolhe TESOURA
    elif chose_player.capitalize() == 'Tesoura' and chose_computer == p_p_t[0]:
        print('O Computador venceu.')
    elif chose_player.capitalize() == 'Tesoura' and chose_computer == p_p_t[1]:
        print('Você venceu.')
    elif chose_player.capitalize() == 'Tesoura' and chose_computer == p_p_t[2]:
        print('Empate.')
        
        
# erro de lógica: o computador está mantendo a mesma escolha ao longo loop, 
# mas isso foi corrigido na versão final. 