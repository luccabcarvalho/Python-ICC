def pal(frase,palantiga,palnova):
    frasenova=''
    frase.split(' ')
    cont1=0
    cont2=0
    contn=0
    contnn=''
    while(cont1<len(frase)):
        if (frase[cont1]==palantiga):
            contn=cont1
        cont1=cont1+1
    frasenova=frase[0:contn-1]+palnova+frase[contn+1:]
    return(frasenova)
fr=input("Insira a frase: ")
pa=input("Insira a palavra que deseja retirar: ")
pn=input("Insira a palavra que deseja colocar: ")
a=pal(fr,pa,pn)
print(a)

