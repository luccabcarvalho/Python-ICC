def qntd(lista,num):
    cont=0
    contp=''
    while (cont<num):
        if len(lista[cont])>(len(contp)):
            contp=lista[cont]
        cont=cont+1
    return contp
def ordem(lista):
    lista.sort()
    return lista
list=[]
n=int(input("Insira o número de elementos na lista: "))
for i in range(0,n):
    l1=input("Insira os elementos da lista: ")
    list.append(l1)
result=qntd(list,n)
alfabetica=ordem(list)
print("A maior palavra é", result,",",alfabetica)

