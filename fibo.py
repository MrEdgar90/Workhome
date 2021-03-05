
n=int(input("Numero:"))
    
if n >= 2:
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

p= "postivo"
n="negativo"
c="cero"
