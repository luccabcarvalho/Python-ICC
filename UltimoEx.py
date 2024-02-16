def op1(valor):
    vf=valor-(valor*0.1)
    return vf
def op2(valor):
    vf=valor/2
    return vf
def op3(valor):
    vp=(valor/p)
    vf=vp+(vp*0.03)
    return vf
print("Este ambiente mostra o valor total de suas compras, as opções de pagamento e calcula seu valor final, com suas prestações caso houverem.")
value=float(input("Insira o valor total de sua compra:"))
while (value<0):
    value=float(input("Insira o valor correto de sua compra:"))
if (value<100):
    op=int(input("As opções de pagamento são:" "\nOpção 1: a vista com 10% de desconto" "\nOpção 2: em duas vezes (preço da etiqueta)" "\nInsira a opção desejada:"))
    while (op!=1 and op!=2):
        op=int(input("Insira uma opção válida:"))
else:
    op=int(input("As opções de pagamento são:" "\nOpção 1: a vista com 10% de desconto" "\nOpção 2: em duas vezes (preço da etiqueta)" "\nOpção 3: de 3 até 10 vezes com 3% de juros ao mês (somente para compras acima de R$ 100,00)." "\nInsira a opção desejada:"))
    while (op!=1 and op!=2 and op!=3):
        op=int(input("Insira uma opção válida:"))
if (op==1):
    valor1=op1(value)
    print("O valor final da compra é ", valor1, " reais.")
if (op==2):
    valor2=op2(value)
    print("O valor final da compra é de 2 parcelas de ", valor2, " reais.")
if (op==3):
    p=int(input("Insira o número de parcelas (DE 3 ATÉ 10):"))
    while (p<3 or p>10):
        p=int(input("Insira um número válido de parcelas:"))
    valor3=op3(value)
    print("O valor final da compra é de " +str(p)+ " parcelas de", valor3)
print("Obrigado por comprar conosco!")







