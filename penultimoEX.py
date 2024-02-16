def comp(lista,listb):
    if (lista==listb):
        return 1
    else:
        return 0
print("Este programa analisa se duas listas são iguais.")
list1=[]
list2=[]
n1=int(input("Insira o número de elementos da primeira lista: "))
for i in range(0,n1):
    l1=input("Insira os elementos da primeira lista:")
    list1.append(l1)
n2=int(input("Insira o número de elementos da segunda lista: "))
for x in range(0,n2):
    l2=input("Insira os elemementos da segunda lista: ")
    list2.append(l2)
resultado=comp(list1,list2)
print(resultado)
