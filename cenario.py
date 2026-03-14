print("Olá, bem vindo(a),para a inscrição.\nInforme seus dados")
nome = input("Digite seu nome completo:\n")
idade = input("Digite seu Idade:\n")
cpf = input("Digite seu CPF:\n")
end = input("Digite seu Endereço:\n")
tel = input("Digite seu Telefone com DDD:\n")
email = input("Digite seu email:\n")
telem = input("Digite seu Telefone de emergência com DDD:\n")
sexo =  input("Informe seu sexo:\n")
print(f"\nConfirme se seus dados estão corretos:\n\n Nome:{nome}\n Idade:{idade}    CPF:{cpf}    Sexo:{sexo}\n Endereço:{end}\n Telefone:{tel}\n E-mail:{email}")
"""confirmação = input("Confirma os dados para a inscrição? sim ou não\n")
if confirmação == "sim":
    print(f"{nome} dados confirmados.")
else:
    print(f"{nome} Dados incorretos")"""
modalidade = input("Qual modalidade você vai escolher:2km ,5km ,10km ,meia,maratona?\n")
if modalidade == "2km":
    print(f"{nome}segue horário da largada:\n - 10:00")
elif modalidade == "5km":
    print(f"{nome} segue o horário da largada:\n - 9:00")
elif  modalidade == "10km":
    print(f"{nome} segue o horário da largada\n - 8:00")
    elif modalidade == "Meia"
temp: input ("Escolha uma das opções:\n 1-<1hora\n 2-> 1hora\n 3->2horas\n")