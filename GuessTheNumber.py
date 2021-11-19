import random
while True:
    computer_action = random.choice(range(1, 10))

    player_action = int(input('Chute um número de 1 a 10: '))
    if player_action < 0:
        print('Digite um valor válido!')
    elif player_action == computer_action:
        print('Parabéns, você acertou!')
    elif player_action > computer_action:
        print(f'Você errou! o número gerado foi {computer_action}')
    elif player_action < computer_action:
        print(f'Você errou! o número gerado foi {computer_action} ')

    play_again = input('Gostaria de tentar novamente? (s/n)')
    if play_again.lower() != 's':
        break
