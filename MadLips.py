# MadLips, game.

print("\n----Spanish version----\nBienvenido a mi primer juego hecho en Python.\n\nEl juego consiste en que se te va a pedir que ingreses algunos datos, mira con detenimiento el tipo de dato que te piden para que el resultado final sea el deseado.\nEso es todo, espero les guste.\n\n----English Version----\n\nWelcome to my first game made in Python.\nThe game consists in that the program will ask you to insert some data, watch carefully the kind of data the program is asking you so that the final product is the desirable.\nThat's all, hope ya'll like it.\n")

Languaje = input("Spanish or English? For spanish type S or s, for english type E or e.\n¿Ejecutar el programa en español o en inglés? Escriba S o s para español, para inglés ingrese E o e: ")

if Languaje =="S" or Languaje =="s":
    Adj1 = input("\nIngrese el primer adjetivo: ")
    Adj2 = input("Ingrese el segundo adjetivo: ")
    Adj3 = input("Ingrese el tercer adjetivo: ")
    sustant_plural = input("Ingrese un sustantivo en plural (ejemplos: casas, cosas, metas, tipos): ")
    nothing = f"\nResultado: Programar es tán ____, siempre me emociona porque me encanta ____ problemas. ¡Aprende a ____ con freeCodeCamp y alcanza tus ____!\n"

    if Adj1 =="" or Adj2=="" or Adj3 =="" or sustant_plural =="":
        print(nothing)
    else:
        madlib = f"\nResultado: Programar es tán {Adj1}, siempre me emociona porque me encanta {Adj2} problemas. ¡Aprende a {Adj3} con freeCodeCamp y alcanza tus {sustant_plural}!\n"

        print(madlib)
elif Languaje=="E" or Languaje =="e":
    Adj1 = input("\nType the first adjective: ")
    Adj2 = input("Type the second adjective: ")
    Adj3 = input("Type the third adjective: ")
    sustant_plural = input("Type the plural sustantive (examples: houses, things, metas, types): ")
    nothing = "\nInput: Programming is so ____, I always get excited because I love ____ problems. ¡Learn to ____ with freeCodeCamp and achieve your ____!\n"

    if Adj1 =="" or Adj2=="" or Adj3 =="" or sustant_plural =="":
        print(nothing)
    else:
        
        madlib = f"\nInput: Programming is so {Adj1}, I always get excited because I love {Adj2} problems. ¡Learn to {Adj3} with freeCodeCamp and achieve your {sustant_plural}!\n"

        print(madlib)
else:
    print("\n~~ Error. Try Again. ~~\n")