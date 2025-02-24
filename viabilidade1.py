while True:
    valorCapital = int(input ("Digite o valor do seu capital: \n"))
    print("Vamos considerar uma Selic de 13,25 por cento e ver quanto renderá seu capital")
    rentabilidadeBruta = valorCapital * 1.1325

    print(f"Se você investir seu dinheiro na selic no fim do ano você terá:\n{rentabilidadeBruta}")

    faturamento = int(input("Digite o faturamento do seu negócio em um ano."))

    lucroLiquido = faturamento *0.15

    if(lucroLiquido < rentabilidadeBruta-valorCapital):
        print("O negócio não é viável ")
        print(f"o seu lucro liquido é {lucroLiquido}")
        break
    else:
        print("O negócio é viável ")
        print(f"O seu lucro liquido é {lucroLiquido}")
        break