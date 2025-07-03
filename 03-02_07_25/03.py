
def converter_temperatura(valor, origem, destino):

    if origem == "C":
        celsius = valor
    elif origem == "F":
        celsius = (valor - 32) * 5 / 9
    elif origem == "K":
        celsius = valor - 273.15
    else:
        return "A unidade de origem inválida."

    if destino == "C":
        return celsius
    elif destino == "F":
        return (celsius * 9 / 5) + 32
    elif destino == "K":
        return celsius + 273.15
    else:
        return "Unidade de destino inválida."

valor = float(input("Digite o valor da temperatura: "))
origem = input("Digite a unidade de origem (C, F ou K): ").upper()
destino = input("Digite a unidade de destino (C, F ou K): ").upper()


resultado = converter_temperatura(valor, origem, destino)

if isinstance(resultado, str):
    print("Erro:", resultado)
else:
    print(f"{valor}°{origem} é igual a {resultado:.2f}°{destino}")
