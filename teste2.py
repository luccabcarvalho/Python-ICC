def espaço(frase):
    novafrase=''
    pal=frase.split(' ')
    for i in pal:
        novafrase=novafrase+(i+'#')
    novafrase=novafrase.strip('#')
    return novafrase
def insert():
    f1=input("Insira a string desejada: ")
    return f1
print("Este programa substitui as ocorrências de espaço por #, na string.")
a=insert()
b=espaço(a)
print(b)