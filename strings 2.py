def qntd(frase,pal):
    f=len(frase.split(pal))
    return (f-1)
fr=input("Insira a frase desejada: ")
palavra=input("Insira a palavra que deseja contabilizar: ")
a=qntd(fr,palavra)
print("A palavra", palavra, " aparece ", a, " vezes.")

