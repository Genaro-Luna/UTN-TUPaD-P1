##1)Crear una función llamada imprimir_hola_mundo que imprima por
##--pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
##--programa principal.

def imprimir_hola_mundo():
    print("Hola mundo version funcion")
    
imprimir_hola_mundo()



##2)Crear una función llamada saludar_usuario(nombre) que reciba
##--como parámetro un nombre y devuelva un saludo personalizado.
##--Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá de-
##--volver: “Hola Marcos!”. Llamar a esta función desde el programa
##--principal solicitando el nombre al usuario.

def saludar_usuario(nombre):
    print(f"Hola, {nombre}, Como te va?")
    
nombre = input("Ingrese su nombre")
saludar_usuario(nombre)




##3)Crear una función llamada informacion_personal(nombre, apellido,
##--edad, residencia) que reciba cuatro parámetros e imprima: “Soy
##--[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pe-
##--dir los datos al usuario y llamar a esta función con los valores in-
##--gresados.

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} y vivo en {residencia}")
    
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su residencia: ")

informacion_personal(nombre, apellido, edad, residencia)




##4)Crear dos funciones: calcular_area_circulo(radio) que reciba el ra-
##--dio como parámetro y devuelva el área del círculo. calcular_peri-
##--metro_circulo(radio) que reciba el radio como parámetro y devuel-
##--va el perímetro del círculo. Solicitar el radio al usuario y llamar am-
##--bas funciones para mostrar los resultados.
import math

num_pi = math.pi

def calcular_area_circulo(radio):
    area = num_pi*(radio*radio)
    print(f"El area es: {area}")

def calcular_metro_circulo(radio):
    perimetro = 2*num_pi*radio
    print(f"El perimetro es: {perimetro}")
    
radio = float(input("Ingrese el radio del circulo: "))

calcular_area_circulo(radio)
calcular_metro_circulo(radio)




##5)Crear una función llamada segundos_a_horas(segundos) que reciba
##--una cantidad de segundos como parámetro y devuelva la cantidad
##--de horas correspondientes. Solicitar al usuario los segundos y mos-
##--trar el resultado usando esta función.

def segundos_a_horas(segundos):
    horas = segundos/3600
    print(f"Los segundos a horas son: {horas}")
    
segundos = int(input("Ingrese los segundos a convertir: "))
segundos_a_horas(segundos)




##6)Crear una función llamada tabla_multiplicar(numero) que reciba un
##--número como parámetro y imprima la tabla de multiplicar de ese
##--número del 1 al 10. Pedir al usuario el número y llamar a la fun-
##--ción.

def tabla_multiplicar(numero):
    resultado = []
    i = 0
    while i <= 10:
        resultado.append(numero * i)
        i+=1
    return resultado

numero = int(input("Ingrese un numero:"))
tabla_multiplicar(numero)




##7)Crear una función llamada operaciones_basicas(a, b) que reciba
##--dos números como parámetros y devuelva una tupla con el resulta-
##--do de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los re-
##--sultados de forma clara.

def operaciones_basicas(a,b):
    suma = a + b
    resta = a - b
    mult = a * b
    div = a/b
    return suma, resta, mult, div

a = float(input("Ingrese 1er numero: "))
b = float(input("Ingrese 2do numero: "))

resultados = operaciones_basicas(a,b) #De esta forma, se crea una tupla donde se guardan los resultados
print(f"Suma: {resultados[0]}")
print(f"Resta: {resultados[1]}")
print(f"Multiplicacion: {resultados[2]}")
print(f"Division: {resultados[3]}")




##8)Crear una función llamada calcular_imc(peso, altura) que reciba el
##--peso en kilogramos y la altura en metros, y devuelva el índice de
##--masa corporal (IMC). Solicitar al usuario los datos y llamar a la fun-
##--ción para mostrar el resultado con dos decimales.

def calcular_imc(peso, altura):
    return peso/(altura*altura)

peso = float(input("Ingrese su peso: "))
altura = float(input("Ingrese algura: "))
calcular_imc(peso, altura)




##9)Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
##--una temperatura en grados Celsius y devuelva su equivalente en
##--Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
##--resultado usando la función.

def celsius_a_fahrenheit(celsius):
    return (celsius*9/5)+32

celsius = int(input("Ingrese grados celsius: "))
celsius_a_fahrenheit(celsius)




##10)Crear una función llamada calcular_promedio(a, b, c) que reciba
##--tres números como parámetros y devuelva el promedio de ellos.
##--Solicitar los números al usuario y mostrar el resultado usando esta
##--función.

def calcular_promedio(a, b, c):
    return (a+b+c)/3

a = int(input("Ingrese 1er numero: "))
b = int(input("Ingrese 2do numero: "))
c = int(input("Ingrese 3er numero: "))

calcular_promedio(a,b,c)