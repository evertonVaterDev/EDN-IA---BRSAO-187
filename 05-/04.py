from datetime import datetime

def dias_vivo(data_nascimento_str):
    
    data_nascimento = datetime.strptime(data_nascimento_str, "%d/%m/%Y")
    
    
    data_hoje = datetime.now()
    
    
    dias_vivo = (data_hoje - data_nascimento).days
    
    return dias_vivo


data_nascimento = input("Digite sua data de nascimento (dd/mm/aaaa): ")
dias = dias_vivo(data_nascimento)
print(f"Você está vivo há {dias} dias.")
