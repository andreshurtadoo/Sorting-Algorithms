#Modulo - Modificar
#Modificando productos por su nombre

def modificar(lista, nombre):
    band = False
    for producto in lista:
        if (producto["Nombre"] == nombre):
            print('MODIFIQUE EL PRODUCTO:', producto["Nombre"])
            print("Espacio para no alterar, exit para salir sin cambios\n")

            for x, y in producto.items():
                print(x + " anterior: " + y)
                response = input("  Modificacion: ")
                if response == "": pass
                elif response == "exit": return print("\n")
                else: producto[x] = response

            band = True
            return print('\n')

    #Verificar si no exite el item
    if band == False:
        return print('NO EXISTE PRODUCTO CON EL NOMBRE:',nombre, "\n")