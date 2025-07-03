# Função para converter a temperatura
def converter_temperatura(valor, origem, destino):
    # Converte a temperatura de origem para Celsius
    if origem == "C":
        celsius = valor
    elif origem == "F":
        celsius = (valor - 32) * 5 / 9
    elif origem == "K":
        celsius = valor - 273.15
    else:
        return "Unidade de origem inválida."

    # Converte a temperatura de Celsius para destino
    if destino == "C":
        return celsius
    elif destino == "F":
        return (celsius * 9 / 5) + 32
    elif destino == "K":
        return celsius + 273.15
    else:
        return "Unidade de destino inválida."

# Entrada do usuário
valor = float(input("Digite o valor da temperatura: "))
origem = input("Digite a unidade de origem (C, F ou K): ").upper()
destino = input("Digite a unidade de destino (C, F ou K): ").upper()

# Conversão
resultado = converter_temperatura(valor, origem, destino)

# Exibição do resultado
if isinstance(resultado, str):
    print("Erro:", resultado)
else:
    print(f"{valor}°{origem} é igual a {resultado:.2f}°{destino}")
