import random

print(***********************************)
print("Bem vindos ao jogo da adivinhação")
print(***********************************)

numero_secreto = random.randrange(1,101)
total_de_tentativas = 10
rodada = 1

while (rodada <= total_de tentativas):
    print("Você digitou o número", chute_str)
    chute = int(chute_str)

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
print("fim de jogo")


