p=("Es Positivo")
i=("Es Igual")
n=("Es Negativo")
n1=0
while(n1 == 0):
    n1 = int(input("1° Numero: "))    
if (n1 < 0):
    print(n)
elif (n1 > 0):
    print(p)

n2=0
while(n2 == 0):
    n2 = int(input("2° Numero: "))    
if (n2 < 0):
    print(n)
elif (n2 > 0):
    print(p)

n3=0
while(n3 == 0):
    n3 = int(input("3° Numero: "))    
if (n3 < 0):
    print(n)
elif (n3 > 0):
    print(p)

n4=0
while(n4 == 0):
    n4 = int(input("4° Numero: "))    
if (n4 < 0):
    print(n)
elif (n4 > 0):
    print(p)

n5=0
while(n5 == 0):
    n5 = int(input("5° Numero: "))    
if (n5 < 0):
    print(n)
elif (n5 > 0):
    print(p)

print("Fibonacci")

v=6
def resultado(i):
    if i<2:
        return i
    return resultado(i-1)+resultado(i-2)
for n in range(v):
    print(resultado(n))
    
print("Numeros primos")

n=int(input("Numero:"))
if n >= 3:
    aumento=0
    for i in range(2,n):
        residuo=n%i
        
        if residuo==0:
                aumento+=1
    if aumento==0:
        print("El numero es primo")
    else:
        print("El numero no es primo")
else:
    print("El numero no es primo")


