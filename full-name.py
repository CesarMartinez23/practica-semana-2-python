# En una variable guarda tu nombre completo y haz que se muestre en pantalla solo tu apellido.

fullName = "Cesar Jacob Martinez Alvarenga"

lastName = fullName[12 : len(fullName)]

print("-----------------------------------------------" + 
        "\nNombre Completo: " + fullName + "\n" +
        "\nApellidos: " + lastName +
        "\n-----------------------------------------------")