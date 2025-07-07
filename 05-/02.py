import re

def verificar_palindromo():
    texto = input("Digite uma palavra ou frase: ")

   
    texto_limpo = re.sub(r'[^a-zA-Z0-9]', '', texto).lower()

    
    if texto_limpo == texto_limpo[::-1]:
        print("Sim")
        return True
    else:
        print("Não")
        return False


verificar_palindromo()
