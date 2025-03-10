print("**************************")
print("Bem vindo ao jogo da forca")
print("**************************")

palavra_secreta = "amora".upper()

letras_acertadas = ["_", "_", "_", "_", "_"]
print(letras_acertadas)

enforcou = False
acertou = False
erros = 0
while(not enforcou and not acertou):
    chute = input("Qual a letra? ")
    chute = chute.strip().upper()

    if (chute in palavra_secreta):
        index = 0
        for letra in palavra_secreta:
            if (chute.upper() == letra.upper()):
                letras_acertadas[index] = letra
            index = index + 1  
        enforcou = erros == 6
        acertou = "_" not in letras_acertadas                                                                                                                                
        print(letras_acertadas)


if(acertou):
    print("você ganhou!")
else:
    print("você perdeu!")

