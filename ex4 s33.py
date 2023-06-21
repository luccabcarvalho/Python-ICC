print("Este programa calcula o número de alunos com a nota acima de 6 e abaixo de 3")
n=int(input("Insira o número de alunos:"))
cont=1
soma=0
cont2=0
cont3=0
while (cont<=n):
    i=float(input("Insira a nota do aluno " + str(cont) + ":"))
    soma=soma+i
    cont=cont+1
    if i > 6:
        cont2 = cont2 + 1
    if i < 3:
        cont3 = cont3 + 1
media=soma/n
print("A média aritmética dos alunos é:", media, "," ,cont2, " alunos ficaram acima de 6 e ", cont3, " alunos ficaram abaixo de 3.")


