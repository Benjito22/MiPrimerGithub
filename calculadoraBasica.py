
lista_sum = []

def menu():
    print("menu")
    print("1 . sumar")
    print("2. restar")
    print("3. salir")

def sumar():
    a = int(input("ingrese cuantos numeros desee sumar: "))
    for i in range(a):
        num = int(input("ingrese el numero a sumar: "))
        print("sumando..")
        lista_sum.append(num)
        suma_total = sum(lista_sum)
        print("la suma es de ", suma_total )
            

def restar():
    res = int(input("ingrese el numero a restar: "))
    rest = int(input("ingrese el otro numero a restar: "))
    resta = res - rest
    print("la resta es de ",resta )

while True:
    menu()
    op = input("ingrese la opcion a realizar: ")
    match op:
        case "1":
            sumar()
        case "2":
            restar()
        case "3":
            print("saliendo..")
            break
        case _:
            print("ingrese una opcion valida...") 
                       
