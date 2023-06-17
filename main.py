from cosas import *

def main ():
    per1 = Persona ("José",19)
    print(per1)
    print(Persona.descripcion)

    print ("-----Herencia-------")
    al1 = Alumno("Jose", 19, "31232312", "ICO")
    print(al1)
    print(Alumno.descripcion)

    al2 = Alumno.constructor_defecto()
    print(al2)
    al2.nombre = "Juan"
    print(al2)
    al2.dormir()
    print("-------herencia ayudante------")
    ayudante = AyudanteProfesor("Adrian ", 20, "421424141", "ICO ", 2123, " Ing. de Sfotware ", 7)
    print(ayudante)
    ayudante.dormir()
    ayudante.nombre = "Adrian"
    ayudante.dar_calase("POO")
main()