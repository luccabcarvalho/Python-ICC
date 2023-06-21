print("Este programa realiza a conversão entre diferentes unidades de medida")
print("As opções de conversão são: 1. Libra -> Quilograma 2. Quilograma -> Libra 3. Onça -> Grama 4. Grama -> Onça")
op=int(input("Insira a opção desejada:"))
if (op!=1 or op!=2 or op!=3 or op!=4):
    print("Insira um valor válido.")
if (op==1):
    v1=float(input("Insira o valor em Libras:"))
    kg=v1*0.4536
    print("O resultado da conversão para Quilograma é:", kg)
if (op==2):
    v2=float(input("Insira o valor em Quilograma:"))
    lb=v2/0.4536
    print("O resultado da conversão para Libra é: ", lb)
if (op==3):
    v3=float(input("Insira o valor em Onça:"))
    g=v3*28.3495
    print("O resultaddo da conversão para Grama é:", g)
if (op==4):
    v4 = float(input("Insira o valor em Grama:"))
    on=v4/28.3495
    print("O resultado em Onça é:", on)




