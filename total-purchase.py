# Programa que pide el nombre del producto, la cantidad y el precio y muestra en pantalla el total de la compra con su información.

productName = input("Ingrese el nombre del producto: ")

quantityProduct = int(input("Ingrese la cantidad del producto: "))

priceProduct = float(input("Ingrese el precio del producto: $"))

totalPurchase = quantityProduct * priceProduct

print("\n----------------------------------------------------")
print("Informacion de la Compra:" +
        "\n----------------------------------------------------" +
        "\nProducto: ", productName +
        "\nCantidad: ", str(quantityProduct) +
        "\nPrecio: $", str(priceProduct) +
        "\nTotal: $", str(totalPurchase))
print("----------------------------------------------------")