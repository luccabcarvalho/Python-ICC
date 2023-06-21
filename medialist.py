def valor(val,num,med):
    val.sort()
    cont1=0
    cont2=0
    result1=0
    result2=0
    while (cont1<num):
        if (val[cont1]<med):
            result1=val[cont1]
        cont1=cont1+1
    val.sort(reverse=True)
    while (cont2<num):
        if (val[cont2]>med):
            result2=val[cont2]
        cont2=cont2+1
    if ((med-result1)<(result2-med)):
        return result1
    if ((med-result1)>(result2-med)):
        return result2
    else:
        return("Os valores são",result1,"e",result2)
list=[]
cont=0
media=0
n=int(input("Insira o número de elementos presentes na lista: "))
while(cont<n):
    l1=int(input("Insira os elementos da lista: "))
    list.append(l1)
    media=media+l1
    cont=cont+1
media=media/n
a=valor(list,n,media)
print(a)

