
import matplotlib.pyplot as plt
print("Laboratorio Suma Acumulativa ")
cant=int (input("Ingrese los numeros a sumar"))

acumulativa=0
sumas_acumulativas= []

for_ in range(cant):
  num= float (input("ingrese un número:"))
   acumulativa +=num
  sumas_acumulativas.append(acumulativa)
 
    print(" La Suma acumulativa de los numeros es:", acumulativa)
   

   etiquetas = [str(i+1)] for  i in range (cant)]
    plt.bar(etiquetas, sumas_acumulativas)
    plt.xlabel("Índice")
    plt.ylabel("Suma Acumulativa")
    plt.title("Gráfico de Suma Acumulativa")
    plt.show()




