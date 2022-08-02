# Un alumno desea saber cuál será su calificación final en la materia de Cálculo. Dicha calificación se compone de los siguientes porcentajes: 30% su primer laboratorio. 30 % su segundo laboratorio. 40 % su parcial.

fullName= input("Ingrese su nombre completo: ")

subjectName = input("Ingrese el nombre de la materia: ")

lab1 = float(input("Ingrese la nota del primer laboratorio: "))
lab2 = float(input("Ingrese la nota del segundo laboratorio: "))
partial = float(input("Ingrese la nota del parcial: "))

finalScore = ((lab1*0.30) + (lab2*0.30) + (partial*0.40))



print("\n-----------------------------------------------------------------------------------------" +
        "\nCalificacion Final del Alumno:" , fullName + " ,en la Materia: ", subjectName +
        "\n-----------------------------------------------------------------------------------------" +
        "\nCalificacion Final: ", str(finalScore) +
        "\n-----------------------------------------------------------------------------------------")