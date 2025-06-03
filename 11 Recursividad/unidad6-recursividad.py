##1)Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
##--función para calcular y mostrar en pantalla el factorial de todos los números enteros
##--entre 1 y el número que indique el usuario

def factorial(num):
    if num == 1 or num == 0:
        return num
    else:
        return num * factorial(num - 1)
    
n = int(input("Ingrese un numero"))

if n <= 1:
    print("Ingrese un numero valido")
else:
    print(f"El factorial del numero ingresado es: {factorial(n)}")
    for i in range(1, n + 1):
        print(f"{i}!: {factorial(i)}")
    
    
##2)Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
##--indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
##--especifique.

def fribonacci(n):
    if n == 0 or n == 1 or n == 2:
        return 1
    elif n<0:
        return 0
    else:
        return fribonacci(n-1) + fribonacci(n-2)
    
n = int(input("Ingrese un numero: "))

if n <= 2:
    print("Ingrese un numero mayor a 1")
else:
    for i in range(1, n+1):
        print(f"Secuencia {i}: {fribonacci(i)}")
        
        
##3)Crea una función recursiva que calcule la potencia de un número base elevado a un
##--exponente, utilizando la fórmula 𝑛𝑚 = 𝑛 ∗ 𝑛(𝑚−1). Prueba esta función en un
##--algoritmo general.

def potencia(n, m):
    if m == 0:
        return 1
    else:
        return n * potencia(n, m-1)
    
num = int(input("Ingrese un num: "))
expo = int(input("Ingrese el exponente: "))

if num <= 1:
    print("Ingrese un numero mayor a 1")
elif expo == 0:
    print("Ingrese un exponente mayo a 0")
else:
    print(f"La potencia es: {potencia(num, expo)}")
    

##4)Crear una función recursiva en Python que reciba un número entero positivo en base
##--decimal y devuelva su representación en binario como una cadena de texto.

def decimal_a_binario(nun):
    if nun == 0:
        return "0"
    elif nun == 1:
        return "1"
    else:
        return decimal_a_binario(nun // 2) + str(nun % 2)

n = int(input("Ingrese el numero a convertir: "))
print(f"El numero {n} pasado a binario es: {decimal_a_binario(n)}")



##5)Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
##--cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no
##--lo es.

def es_palindromo(palabra, i = 0, f = None):
    f = len(palabra) - 1
    
    if palabra[i] != palabra[f]:
        return False
    if palabra[i] == palabra[f]:
        return True
    return es_palindromo(palabra, i+1, f-1)
    
p = input("Ingrese una palabra para saber si es o no un palindromo")
print(es_palindromo(p))



#6)Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
#--número entero positivo y devuelva la suma de todos sus dígitos.

def suma_digitos(n):
    if n < 10:
        return n
    return (n%10) + suma_digitos(n//10)

    
num = int(input("Ingrese un numero:"))
print(f"La suma de los digitos de {num} es: {suma_digitos(num)}")




#7)Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n
#--bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al
#--último nivel con un solo bloque.
#--Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el
#--nivel más bajo y devuelva el total de bloques que necesita para construir toda la
#--pirámide.

def contar_bloques(n):
    if n == 0 or n == 1:
        return n
    else:
        return  n + contar_bloques(n - 1)
    

nu = int(input("Ingrese la cantidad de bloques en la base:"))

print(f"Si la base es de {nu} bloques, se necesian: {contar_bloques(nu)}")



#8)Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
#--número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
#--aparece ese dígito dentro del número.

def contar_digito(numero, digito):
    if numero == 0:
        return 0
    
    return (1 if numero % 10 == digito else 0) + contar_digito(numero // 10, digito)

num = int(input("Ingrese el numero:")) 
dig = int(input("Ingrese el digito:")) 

print(f"El digito {dig}, dentro del numero {num}, aparece: {contar_digito(num, dig)} veces")