def calcular_gorjeta():
    def ler_float(mensagem):
        while True:
            try:
                return float(input(mensagem))
            except ValueError:
                print("Erro: Digite um número válido.")

    valor_conta = ler_float("Digite o valor total da conta (ex: 150.00): R$ ")
    porcentagem_gorjeta = ler_float("Digite a porcentagem da gorjeta (ex: 10 para 10%): ")

    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    print(f"Valor da gorjeta: R$ {round(gorjeta, 2)}")
    return gorjeta

calcular_gorjeta()
