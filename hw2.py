################################################################################################
# Nombre de archivo: hw2.py (No cambiar el nombre de este archivo)
# El repositorio donde esta tu HW2 es: https://github.com/unlu-edu-ar/homework-1-santiagobdar
#
# Completa con tu nombre, apellido y DNI
# Nombre y Apellido: Santiago Ezequiel Bdar
# DNI:45738134
################################################################################################


#################################################
# Funciones que tenés que programar
#################################################

# Escribir una función que reciba dos números enteros: a y b. 
# La función debe retonar True si a es impar y menor que b. 
# Caso contrario, debe retornar False

def imparYmenor(a, b):
    if a%2 != 0 and a < b:
        return True
    else:
        return False

# Cree una función que recibe dos string como parámetro(a,b), y retorna un string con 
# la leyenda "Gana a", si el string a tiene mayor cantidad de caracteres que el string b.
# Si el string b tiene mayor cantidad de caracteres que el string a, debe retornar "Gana b".
# Si ambos strings tienen la misma cantidad de caracteres, debe retornar "Empate".
def quienGana(a, b):
    if len(a) > len(b):
        return f"Gana {a}"
    elif len(a) < len(b):
        return f"Gana {b}"
    else:
        return f"Empate"
    
# Cree una función que recibe dos números de parámetro, y realiza la resta de ambos. 
# ( a - b)
# Si el resultado de la resta es mayor a 0, debe retornar true, caso contrario, debe
# retornar false.
def restaPositiva(a, b):
    if a-b > 0:
        return True
    else:
        return False
    

# Cree una función que recibe un número entero entre 1 y 10 de parámetro, 
# correspondiente a una materia de la carrera y retorna un  string, con el nombre de la materia en 
# lenguaje natural. La relación entre números y materias es la siguiente:
# 1: "Introducción a la Programación", 2: "Algebra y Lógica Computacional", 3: "Matemática Discreta",
# 4: "Introducción a los Sistemas", 5: "Organización de computadoras", 6: "Ingles 1", 7: "Análisis Matemático",
# 8: "Algoritmos y Estructuras de Datos", 9: "Programación 1",
# 10: "Arquitectura de Computadoras"
def materia(x):    
    materias = {
        1: "Introducción a la Programación",
        2: "Algebra y Lógica Computacional",
        3: "Matemática Discreta",
        4: "Introducción a los Sistemas",
        5: "Organización de computadoras",
        6: "Ingles 1",
        7: "Análisis Matemático",
        8: "Algoritmos y Estructuras de Datos",
        9: "Programación 1",
        10: "Arquitectura de Computadoras"
    }
    return materias.get(x)

# Cree una función que recibe un número entero, entre 1 y 12, correspondiente a
# un mes y retorna un  string, con el nombre de la estación. Considera la 
# relación entre números y estaciones de la siguiente forma: 1, 2, 3: "Verano", 
# 4, 5, 6: "Otoño", 7, 8, 9: "Invierno", 10, 11, 12: "Primavera"
def estacion(x):
    if 1 <= x <= 3:
        return "Verano"
    elif 4 <= x <= 6:
        return "Otoño"
    elif 7 <= x <= 9:
        return "Invierno"
    elif 10 <= x <= 12:
        return "Primavera"


# Cree una función que recibe un número entero, entre 1 y 12, correspondiente a
# un mes, y retorna un booleano, que es True si el número de letras del mes fuese par, 
# y False si el número del mes fuese impar
def mesLetrasPar(x):
    meses = {
        1: "Enero",
        2: "Febrero",
        3: "Marzo",
        4: "Abril",
        5: "Mayo",
        6: "Junio",
        7: "Julio",
        8: "Agosto",
        9: "Septiembre",
        10: "Octubre",
        11: "Noviembre",
        12: "Diciembre"
    }
    if len(meses.get(x)) % 2 == 0:
        return True
    else:
        return False

# Cree una función que recibe dos numeros y un booleano como parámetros,
# los numeros indican la nota de dos parciales de un alumno, y el booleano
# indica si el alumno tiene los homeworks aprobados.
# La función debe retornar un string con la condición del alumno, 
# que puede ser "Promovido", "Regular" o "Libre".
# -Un alumno está promovido si tiene las dos notas de parciales mayores o iguales a 7,
#  y tiene los homeworks aprobados.
# -Un alumno está regular si tiene las dos notas de parciales
#  mayores o iguales a 4, y tiene los homeworks aprobados.
# -Un alumno está libre si tiene
#  alguna nota de parcial menor a 4, o no tiene los homeworks aprobados. 
def condicionAlumno(nota1, nota2, homeworks):
    if nota1 >= 7 and nota2 >= 7 and homeworks:
        return "Promovido"
    elif nota1 >= 4 and nota2 >= 4 and homeworks:
        return "Regular"
    else:
        return "Libre"

# Realice una función que reciba cuatro numeros enteros como parámetros,
# que corresponden a las longitudes de los lados de una figura.
# esta funcion debera retornar un string con la leyenda:
# "Es un cuadrado", si todos los lados son iguales
# "Es un rectangulo", si hay dos pares de lados iguales
# "No es un cuadrado ni un rectangulo", si no se cumplen las condiciones anteriores
def tipoFigura(a, b, c, d): 
    if a>0 and b>0 and c>0 and d>0:
        if a == b == c == d:
            return "Es un cuadrado"
        elif (a == b and c == d) or (a == c and b == d) or (a == d and b == c):
            return "Es un rectangulo"
        else: 
            return "No es un cuadrado ni un rectangulo"
    else:
        return "No es un cuadrado ni un rectangulo"

# Cree una función que recibe 3 números enteros como parámetros, y retorna un 
# string con la leyenda:
# "No es un triangulo", si los longitudes no pueden corresponder a un triángulo
# "Equilatero", si puede ser un triángulo y todos las longitudes son iguales
# "Isosceles", si puede ser un triángulo y tiene dos longitudes iguales
# "Escaleno", si puede ser un triángulo y todas las longitudes son diferentes
def tipoTriangulo(x, y, z):
    if x == y == z:
        return "Equilatero"
    elif x == y or x == z or y == z:
        return "Isosceles"
    elif x + y <= z or x + z <= y or y + z <= x:
        return "No es un triangulo"
    else:
        return "Escaleno"
    

#################################################
# Funciones de Test (no modificar)
#################################################

def testImparYmenor():
    print('Testeando testImparYmenor()... ', end='')
    assert imparYmenor(3, 5) == True
    assert imparYmenor(4, 5) == False
    assert imparYmenor(4, 4) == False
    print('Pasó!')

def testQuienGana():
    print('Testeando testQuienGana()... ', end='')
    assert quienGana("Hola", "Bye") == "Gana Hola"
    assert quienGana("Bye", "Hola") == "Gana Hola"
    assert quienGana("Hola", "Hola") == "Empate"
    print('Pasó!')

def testRestaPositiva():
    print('Testeando testRestaPositiva()... ', end='')
    assert restaPositiva(5, 3) == True
    assert restaPositiva(3, 5) == False
    assert restaPositiva(3, 3) == False
    print('Pasó!')

def testMateria():
    print('Testeando testMateria()... ', end='')
    assert materia(1) == "Introducción a la Programación"
    assert materia(2) == "Algebra y Lógica Computacional"
    assert materia(3) == "Matemática Discreta"        
    assert materia(4) == "Introducción a los Sistemas"
    assert materia(5) == "Organización de computadoras"
    assert materia(6) == "Ingles 1"
    assert materia(7) == "Análisis Matemático"
    assert materia(8) == "Algoritmos y Estructuras de Datos"
    assert materia(9) == "Programación 1"    
    assert materia(10) == "Arquitectura de Computadoras"
    print('Pasó!')

def testEstacion():
    print('Testeando testEstacion()... ', end='')
    assert estacion(1) == "Verano"
    assert estacion(2) == "Verano"
    assert estacion(3) == "Verano"        
    assert estacion(4) == "Otoño"
    assert estacion(5) == "Otoño"
    assert estacion(6) == "Otoño"
    assert estacion(7) == "Invierno"
    assert estacion(8) == "Invierno"
    assert estacion(9) == "Invierno"    
    assert estacion(10) == "Primavera"
    assert estacion(11) == "Primavera"
    assert estacion(12) == "Primavera"
    print('Pasó!')


def testMesLetrasPar():
    print('Testeando testMesLetrasPar()... ', end='')
    assert mesLetrasPar(1) == False
    assert mesLetrasPar(2) == False
    assert mesLetrasPar(3) == False
    assert mesLetrasPar(4) == False
    assert mesLetrasPar(5) == True
    assert mesLetrasPar(6) == False
    assert mesLetrasPar(7) == False
    assert mesLetrasPar(8) == True
    assert mesLetrasPar(9) == True
    assert mesLetrasPar(10) == False
    assert mesLetrasPar(11) == False
    assert mesLetrasPar(12) == False
    print('Pasó!')

def testCondicionAlumno():
    print('Testeando testCondicionAlumno()... ', end='')
    assert condicionAlumno(7,7,True) == "Promovido"
    assert condicionAlumno(7,7,False) == "Libre"
    assert condicionAlumno(4,4,True) == "Regular"
    assert condicionAlumno(4,4,False) == "Libre"
    assert condicionAlumno(3,3,True) == "Libre"
    assert condicionAlumno(3,3,False) == "Libre"
    print('Pasó!')

def testTipoFigura():
    print('Testeando testTipoFigura()... ', end='')
    assert tipoFigura(2,2,2,2) == "Es un cuadrado"
    assert tipoFigura(2,3,2,3) == "Es un rectangulo"
    assert tipoFigura(3,3,4,5) == "No es un cuadrado ni un rectangulo"
    assert tipoFigura(2,2,2,4) == "No es un cuadrado ni un rectangulo"
    assert tipoFigura(0,0,0,0) == "No es un cuadrado ni un rectangulo"
    assert tipoFigura(0,0,1,1) == "No es un cuadrado ni un rectangulo"
    print('Pasó!')

def testTipoTriangulo():
    print('Testeando testTipoTriangulo()... ', end='')
    assert tipoTriangulo(6,6,3) == "Isosceles"
    assert tipoTriangulo(2,2,2) == "Equilatero"
    assert tipoTriangulo(5,3,7) == "Escaleno"
    assert tipoTriangulo(1,2,3) == "No es un triangulo"
    print('Pasó!')

#################################################
# testearTodo y main
#################################################

def testearTodo():
    # comentá los tests que no querés correr!
    testImparYmenor()
    testQuienGana()
    testRestaPositiva()
    testMateria()
    testEstacion()
    testMesLetrasPar()
    testCondicionAlumno()
    testTipoFigura()
    testTipoTriangulo()
    

def main():
    testearTodo()

if __name__ == '__main__':
    main()
