print("<Primer ejercicio>")
num1 = int(input("Primer numero para multlipicarlos: "))
num2 = int(input("Segundo numero para multlipicarlos: "))
times = (num1*num2)
exp = (pow(times,5))
print("Tu resultado es: " + str(exp))
print("--------------------------------------------------------------")
print("<Segundo ejercicio>")
gradoC = int(input("Grados Celsius: "))
gradosF = (gradoC * 1.8)+32
print("Grados Fahrenheit: " + str(gradosF) + "°F")
print("--------------------------------------------------------------")
print("<Tercer ejercicio>")
ram1 = int(input("1°Numero aleatorio: "))
ram2 = int(input("2°Numero aleatorio: "))
while (ram1==ram2):
    print("No numeros iguales porfavor")
    ram1 = int(input("1°Numero aleatorio: "))
    ram2 = int(input("2°Numero aleatorio: "))  
if ram1 > ram2:
    print("Primer numero aleatorio es mayor")
elif ram1 < ram2:  
    print("Segundo numero aleatorio es mayor")

print("-------------------------------------------------------------")
print("<Cuarto ejercicio>")
n1 = int(input("1°Numero aleatorio: "))
n2 = int(input("2°Numero aleatorio: "))
n3 = int(input("3°Numero aleatorio: "))
while (n1==n2==n3):
    print("No numeros iguales porfavor")
    n1 = int(input("1°Numero aleatorio: "))
    n2 = int(input("2°Numero aleatorio: "))
    n3 = int(input("3°Numero aleatorio: "))
while (n1==n2):
    print("No numeros iguales porfavor")
    n1 = int(input("1°Numero aleatorio: "))
    n2 = int(input("2°Numero aleatorio: "))
    n3 = int(input("3°Numero aleatorio: "))
while (n2==n3):
    print("No numeros iguales porfavor")
    n1 = int(input("1°Numero aleatorio: "))
    n2 = int(input("2°Numero aleatorio: "))
    n3 = int(input("3°Numero aleatorio: "))
while (n1==n3):
    print("No numeros iguales porfavor")
    n1 = int(input("1°Numero aleatorio: "))
    n2 = int(input("2°Numero aleatorio: "))
    n3 = int(input("3°Numero aleatorio: "))
if n1>n2:
    mayor=n1
if not n1>n2:
    mayor=n2
if mayor>n3:
    ganador = mayor
if not mayor>n3:
    ganador = n3
print("El numero mayor es: " + str(ganador))

print("-------------------------------------------------------------")
print("<Quinto ejercicio>")
litros = int(input("Cantidad de litros: "))
mililitros = litros*1000
print("Cantidad de mililitros: " +str(mililitros)+ "ml")
