def verificar_senha(senha):
 
    if len(senha) < 8:
        return "Senha muito curta. Deve ter pelo menos 8 caracteres."

    
    if not any(caractere.isdigit() for caractere in senha):
        return "Senha fraca. Deve conter pelo menos um número."

    return "Senha válida e segura!"


senha_usuario = input("Digite sua senha: ")
resultado = verificar_senha(senha_usuario)

print(resultado)
