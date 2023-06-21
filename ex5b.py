print("Este programa calcula a média aritmética da nota dos alunos e contabiliza quantos ficaram acima e abaixo de 5 pontos")
n=int(input("Insira o número de alunos:"))
soma=0
cont1=0
cont2=0
for i in range (0, n):
    p=float(input("Insira a nota da prova:"))
    soma=soma+p
    media=soma/n
    if (p>=5):
        cont1=cont1+1
    if (p<5):
        cont2=cont2+1
print("A média aritmética dos alunos é:", media, ", ", cont1, " alunos ficaram acima de 5 e ", cont2, " alunos ficaram abaixo de 5.")


