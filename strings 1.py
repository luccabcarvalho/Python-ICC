def atomo(cadeia):
    lista=list(cadeia)
    cadeiacomp=' '
    cont=0
    while (cont<len(cadeia)):
    #bases A e T
        if (cadeia[cont]=='A'):
            cadeiacomp=cadeiacomp+'T'
        if (cadeia[cont]=='T'):
            cadeiacomp=cadeiacomp+'A'
    #bases C e G
        if (cadeia[cont]=='C'):
            cadeiacomp=cadeiacomp+'G'
        if (cadeia[cont]=='G'):
            cadeiacomp=cadeiacomp+'C'
        cont=cont+1
    return cadeiacomp
cadeia1=input("Insira a sequência de DNA: ")
a=atomo(cadeia1)
print(a)




