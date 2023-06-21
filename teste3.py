def maior_elemento(lista,num):
    cont=0
    contn=0
    while(cont<num):
        if (lista[cont]>contn):
            contn=lista[cont]
        cont=cont+1
    return contn
def soma_elementos(lista,num):
    cont=0
    contn=0
    while(cont<num):
        contn=contn+lista[cont]
        cont=cont+1
    return contn
def num_ocorrencias(lista):
    oc=lista.count(lista[0])
    return oc
def Media(lista,num):
    cont=0
    contn=0
    while(cont<num):
        contn=contn+lista[cont]
        cont=cont+1
    media=contn/num
    return Media
def val_mais_prox_media(lista,num,media):
    cont1=0
    cont2=0
    result1=0
    result2=0
    lista.sort()
    while(cont1<num):
        if(lista[cont1]<media):
            result1=lista[cont1]
        cont1=cont1+1
    lista.sort(reverse=True)
    while(cont1<num):
        if(lista[cont2]>media):
            result2=lista[cont2]
        cont2=cont2+1
    if ((media-result1)<(result2-media)):
        return ("O valor mais próximo da média é:",result1)
    if ((media-result1)>(result2-media)):
        return ("O valor mais próximo da média é",result2)
    else:
        return("Os valores mais próximos a média são",result1,"e",result2,".")
print("Este programa analisa os dados da lista desejada.")
n=int(input("Insira o número de elementos da lista: "))
list=[]
for i in range(0,n):
    l1=int(input("Insira os elementos da lista: "))
    list.append(l1)
a=maior_elemento(list,n)
b=soma_elementos(list,n)
c=num_ocorrencias(list)
d=Media(list,n)
e=val_mais_prox_media(list,n,Media)
print("O maior elemento é:",a)
print("A soma dos elementos é",b)
print("O número de ocorrências do primeiro elemento é",c)
print("A média dos elementos é",d)
print(e)





