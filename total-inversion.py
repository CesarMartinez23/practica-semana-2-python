# Programa que pregunta al usuario una cantidad de dinero a invertir, el interés anual y el número de años, y muestra por pantalla el capital obtenido en la inversión.

userName = input("Ingrese su nombre: ")

amountMoney = float(input("Ingrese la cantidad de dinero a invertir: $"))

annualInterest = float(input("Ingrese el interes anual: %"))

amountYears = int(input("Ingrese el numero de años: "))

totalInversion = (amountMoney * (1 + annualInterest / 100) ** amountYears)-amountMoney

print("El capital obtenido de la inversion de $" + str(amountMoney) + " con un interes anual del " + str(annualInterest) + "% y una duracion de " + str(amountYears) + " años es de $" + str(totalInversion))