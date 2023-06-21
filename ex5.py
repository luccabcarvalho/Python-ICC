print("Este programa calcula a média aritmética da nota dos alunos e contabiliza quantos ficaram acima e abaixo de 5 pontos")
n=int(input("Insira o número de alunos:"))
cont=1
soma=0
cont1=0
cont2=0
while (cont<=n):
    i=float(input("Insira a nota do " + str(cont) + ":"))
    soma=soma+i
    cont=cont+1
    media=soma/n
    if (i>=5):
        cont1=cont1+1
    if (i<5):
        cont2=cont2+1
print("A média aritmética dos alunos é:", media,",", cont1, " aluno(s) ficaram acima de 5 e ", cont2, " aluno(s) ficaram abaixo de 5.")
