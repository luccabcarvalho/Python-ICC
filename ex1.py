print("Este programa analisa se duas listas apresentam os mesmos elementos.")
n1=int(input("Insira o número de elementos presentes na primeira lista: "))
list1=[]
for i in range(0,n1):
    l1=input("Insira os elementos da primeira lista: ")
    list1.append(l1)
n2=int(input("Insira o número de elementos presentes na segunda lista: "))
list2=[]
for x in range(0,n2):
    l2=input("Insira os elementos da segunda lista: ")
    list2.append(l2)
list1.sort()
list2.sort()
if (list1==list2):
    print("True")
else:
    print("False")