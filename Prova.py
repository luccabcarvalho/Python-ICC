def subs(frase,palnova,palant):
    frase=frase.split(' ')
    cont1=0
    while(cont1<len(frase)):
        if (list[cont1]==palant):
            frase.remove(palant)
            frase.insert(cont1,palnova)
        cont1=cont1+1
    return frase
fr=input("Escolha a frase:")
paln=input("Escolha a palavra nova:")
palv=input("Escolha a palavra que deseja retirar:")
a=subs(fr,paln,palv)
print(a)






