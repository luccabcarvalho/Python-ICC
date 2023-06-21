print("Este programa calcula a média aritmética dos alunos e contabiliza quantos ficaram abaixo de 3 e quantos ficaram acima de 6")
n=int(input("Insira o número de alunos:"))
while (n<=0):
    n=int(input("Insira um valor válido:"))
soma=0
cont1=0
cont2=0
for i in range (1, n+1):
    p=float(input("Insira a nota do aluno " +str(i)+ ":"))
    soma=soma+p
    if (p < 3):
        cont1 = cont1 + 1
    if (p > 6):
        cont2 = cont2 + 1
media=soma/n
print("A média aritmética dos alunos é:", media,", ", cont1, "alunos obtiveram menos de 3 pontos e ", cont2, "alunos obtiveram mais de 6 pontos.")