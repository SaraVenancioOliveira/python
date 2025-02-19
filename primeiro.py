import random

print(*"**********************************")
print("Bem vindos ao jogo da adivinhação")
print("***********************************")

numero_secreto = random.randrange(1,101)
total_de_tentativas = 10
rodada = 1

while (rodada <= total_de_tentativas):
    print(f"Tentativa {rodada} de {total_de_tentativas}")

    chute_str = input("digite o seu número:")
    print("Você digitou o número", chute_str)
    
    try:
        chute = int(chute_str)
    except ValueError:
        print("caractere invalido. Use apenas números")
        continue

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
        print("parabens, você acertou")
    else:
        if(maior):
           print("o seu chute foi maior do que o número secreto")
        elif(menor):
           print("o seu chute foi menor do queo número secreto")
    rodada = rodada +1
print("fim de jogo", numero_secreto)


