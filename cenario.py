print("Olá, bem vindo(a),para a inscrição.\nInforme seus dados")
nome = input("Digite seu nome completo:\n")
#idade = input("Digite seu Idade:\n")
#cpf = input("Digite seu CPF:\n")
#end = input("Digite seu Endereço:\n")
#tel = input("Digite seu Telefone com DDD:\n")
#email = input("Digite seu email:\n")
#telem = input("Digite seu Telefone de emergência com DDD:\n")
sexo =  input("Informe seu sexo:\n")
#print(f"\nConfirme se seus dados estão corretos:\n\n Nome:{nome}\n Idade:{idade}    CPF:{cpf}    Sexo:{sexo}\n Endereço:{end}\n Telefone:{tel}\n E-mail:{email}")
"""confirmação = input("Confirma os dados para a inscrição? sim ou não\n")
if confirmação == "sim":
    print(f"{nome} dados confirmados.")
else:
    print(f"{nome} Dados incorretos")"""
modalidade = input("Qual modalidade você vai escolher:\n1-2km \n2-5km \n3-10km \n4-Meia \n5-Maratona\n")
if modalidade == "1":
    print(f"{nome} segue horário da largada:\n - 10:00")
elif modalidade == "2":
    print(f"{nome} segue o horário da largada:\n - 9:00")
elif  modalidade == "3":
    print(f"{nome} segue o horário da largada\n - 8:00")
elif modalidade == "4":
    temp = input("Escolha uma das opções:\n 1-<1hora\n 2-> 1hora\n 3->2horas\n")
    if temp == "1" and sexo == "feminino":
        print("Seu pelotão de elite, larga às 06:10.")
    elif temp == "1" and sexo == "masculino":
        print("Seu pelotão de elite, larga às 06:00.")
    elif temp == "2" and sexo == "feminino":
        print("Seu pelotão A, larga às 06:40.")
    elif temp == "2" and sexo == "masculino":
        print ("Seu pelotão A, larga às 06:30.")
    else:
        print("Seu pelotão Geral, larga às 07:00.")
elif modalidade == "5": 
   temp = input("Escolha uma das opções:\n 1-<1hora\n 2-> 1hora\n 3->2horas\n")
   if temp == "1" and sexo == "feminino":
        print("Seu pelotão de elite, larga às 05:10.")
   elif temp == "1" and sexo == "masculino":
        print("Seu pelotão de elite, larga às 05:00.")
   elif temp == "2" and sexo == "feminino":
        print("Seu pelotão A, larga às 05:40.")
   elif temp == "2" and sexo == "masculino":
        print ("Seu pelotão A, larga às 05:30.")
   else:
        print("Seu pelotão Geral, larga às 05:50.")