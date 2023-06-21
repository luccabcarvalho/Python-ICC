def verif(n1,n2):
#Esta função verifica se o primeiro valor é multiplo do segundo
    multi=n1%n2
    return multi
print("Este programa verifica se os números são multiplos entre si.")
x=int(input("Insira o primeiro número:"))
while (x<0):
    x=int(input("Insira um valor natural:"))
y=int(input("Insira o segundo número:"))
while (y<0):
    y=int(input("Insira um valor natural:"))
mult=verif(x,y)
if (mult==0):
    print("1")
else:
    print("0")
print("FIM")