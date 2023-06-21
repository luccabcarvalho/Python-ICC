print("Este programa traduz o tempo de duração doe evento em segundos para dias, horas, minutos e segundos.")
n1=int(input("Insira o tempo de duração do evento em segundos: "))
if (n1>86400):
    dias=n1//86400
    horas=(n1%86400)//3600
    minutos=((n1%86400)%3600)//60
    segundos=((n1%86400)%3600)%60
if (n1<86400):
    dias=0
    horas=n1//3600
    minutos=(n1%3600)//60
    segundos=(n1%3600)%60
if (n1<3600):
    dias=0
    horas=0
    minutos=n1//60
    segundos=n1%60
if (n1<60):
    dias=0
    horas=0
    minutos=0
    segundos=n1
print("O tempo de duração é de", dias, "dia(s),",horas, "hora(s),", minutos, "minuto(s),", segundos, "segundo(s)")
