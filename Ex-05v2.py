import random

sorteio = random.randint(0, 100)
acertou = False

for i in range(1, 11):
    palpite = int(input('Informe seu palpite: '))

    if palpite == sorteio:
        print(f'Parabéns! Você acertou em {i} tentativas!')
        acertou = True
        break   #Interrompe uma estrutura de repetição
    else:
        print('Errouuuuuuuuuuu! Tenta de novo, mané!')

        if palpite < sorteio:
            print('Chutou muito baixo!')
        else:
            print('Chutou muito alto!')

if not acertou:
    print(f'O número sorteado foi {sorteio}')