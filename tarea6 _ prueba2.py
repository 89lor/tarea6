
import matplotlib.pyplot as plt

def suma_acumulativa(nums):
    suma = 0
    acumulativa = []
    for num in nums:
        suma += num
        acumulativa.append(suma)
    return acumulativa

def main():
    print("Laboratorio de Suma Acumulativa")
    entrada = input("Ingrese una serie de números separados por comas: ")
    
    try:
        numeros = [float(num.strip()) for num in entrada.split(',')]
    except ValueError:
        print("Error: Ingrese números separados por comas válidos.")
        return

    acumulativa = suma_acumulativa(numeros)

    
    print("Suma acumulativa:")
    print(acumulativa)

   
    plt.bar(range(1, len(acumulativa) + 1), acumulativa)
    plt.xlabel("Índice")
    plt.ylabel("Suma Acumulativa")
    plt.title("Gráfico de Suma Acumulativa")
    plt.show()

if __name__ == "__main__":
    main()


