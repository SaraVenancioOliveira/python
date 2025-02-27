print("*******************")
print("Bem vindo ao jogo")
print("*******************")

palavra_secreta = "morango"

enforcou = False
acertou = False

while(not enforcou and not acertou):
    chute = input("Qual a letra?")
    chute = chute.strip()

    index = 0

    for letra in palavra_secreta:
        if (chute.upper() == letra.upper()):
            print(f"encontre a letra {letra} na posição{index}")
        index = index + 1
    print("jogando....")
print("Fim de jogo")