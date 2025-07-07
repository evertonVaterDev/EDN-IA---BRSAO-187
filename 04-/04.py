pares = 0
impares = 0

print("Digite números inteiros (digite 0 para encerrar):")

while True:
    numero = int(input("Número: "))

    if numero == 0:
        break

    if numero % 2 == 0:
        print("Par")
        pares += 1
    else:
        print("Ímpar")
        impares += 1

print("\nResumo:")
print(f"Total de números pares: {pares}")
print(f"Total de números ímpares: {impares}")

