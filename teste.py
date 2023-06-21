def qntd(frase):
    frase=frase.strip(' ')
    f=len(frase.split(' '))
    return f
print("Este programa contabiliza a quantidade de palavras presentes em uma frase")
fr=input("Insira a frase desejada: ")
resultado=qntd(fr)
print("A palavra contém ", resultado, " palavras.")

