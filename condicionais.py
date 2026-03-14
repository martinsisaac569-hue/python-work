"""
n1=11
n2=20
result= n1+n2
print(result)
if result% 2 == 0:
    print(f"A soma de {n1} + {n2} é igual {result} par")
else:
    print(f"A soma de {n1} + {n2} é igual {result} ímpar")
    """
n1= int(input("digite o primeiro número:"))
n2= int(input("digite o segundo número:"))
if (n1+n2)%2==0:
    print("Deu certo")
else:
    print("Deu ruim")