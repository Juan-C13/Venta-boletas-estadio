#Juan Clavijo - 202225709
#Problema 2

a=1
cluneta=0
cbalcon=0
cpalco=0

while a==1:
    print("")
    ubicacion=int(input("Digite la ubicación (1-Luneta,2-Balcón,3-Palco):"))
    cantidad=int(input("Digite la cantidad de boletas a comprar:"))
    if (ubicacion==1 or ubicacion==2 or ubicacion==3)and(cantidad>0):
        a=int(input("¿Desea ingresar los datos de otra venta? (1-Sí,2-No):"))
    else:
        print("Esos válores no son válidos")

    if ubicacion==1:
        cluneta=cluneta+cantidad
    if ubicacion==2:
        cbalcon=cbalcon+cantidad
    if ubicacion==3:
        cpalco=cpalco+cantidad

total=(cluneta*40000)+(cbalcon*25000)+(cpalco*12000)
print("")
print("El ingreso por venta de boletas es de:",total)
print("El total de boletas vendidas en luneta es",cluneta)
print("El total de boletas vendidas en balcón es",cbalcon)
print("El total de boletas vendidas en palco es",cpalco)
