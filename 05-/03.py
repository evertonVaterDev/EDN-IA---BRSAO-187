def calcular_desconto():
    try:
        
        preco_original = float(input("Digite o preço original do produto (R$): "))
        percentual_desconto = float(input("Digite o percentual de desconto (ex: 20 para 20%): "))

        
        valor_desconto = preco_original * (percentual_desconto / 100)

        
        preco_final = preco_original - valor_desconto

        
        print(f"\nValor do desconto: R$ {round(valor_desconto, 2)}")
        print(f"Preço final com desconto: R$ {round(preco_final, 2)}")

        return preco_final

    except ValueError:
        print("Erro: Insira apenas números válidos.")
        return None


calcular_desconto()
