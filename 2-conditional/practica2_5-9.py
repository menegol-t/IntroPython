a = int(input("a: "))
b = int(input("b: "))

print("act 5)")
if a < 4 :
    print("debe recuperar")

print("\nact 6)A)")
if a > b : 
    print(a)
else : 
    print (b)

print("\nact 6)B)")
if a < b : 
    print(a)
else : 
    print (b)

print("\nact 7)")
A = float(input("A: "))
B = float(input("B: "))
C = (A + B) / 2
print(C)
if C > 7 :
    print("aprobado")
else : 
    print("desaprobado")

print("\nact 8)")
d = int(input("Ingresa un numero entero positivo: "))
if d > 9 :
    print("Ingresaste un numero de mas de 1 cifra.")
else :
    print("Ingresaste un numero de una cifra.")

print("\nact 9)")
e = int(input("Ingresa tu DNI: "))
if e == 30612453 or e == 23763290 or e == 21448503 or e == 34582048 or e == 15364857 :
    print("ese DNI ya estaba en el listado")
else :
    print("ese DNI es nuevo")