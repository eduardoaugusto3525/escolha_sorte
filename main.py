import random

print("Bem-vindo ao jogo 'Escolha da Sorte'!")
print("Tente adivinhar o número secreto entre 1 e 10.")

# Gera um número aleatório entre 1 e 10
numero_secreto = random.randint(1, 10)
tentativas = 3

# Loop para dar ao jogador 3 tentativas
while tentativas > 0:
    escolha = int(input("Digite o seu palpite: "))
    
    # Verifica se o palpite é igual ao número secreto
    if escolha == numero_secreto:
        print("Parabéns! Você acertou o número secreto!")
        break
    else:
        tentativas -= 1
        print("Errado! Tente novamente.")
        if tentativas > 0:
            print(f"Você tem {tentativas} tentativas restantes.")

# Mensagem ao final do jogo
if tentativas == 0:
    print(f"Que pena! Suas tentativas acabaram. O número secreto era {numero_secreto}.")
