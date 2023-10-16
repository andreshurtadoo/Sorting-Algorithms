#Modulo - Crear
#Crear los productos con todas su propiedades

def crear():
    #Producto con valores por defecto
    producto = {
        "Nombre":"Generico",
        "Descripcion":"Producto Generico",
        "Categoria":"General",
        "Precio (Bs)":"1000",
        "Imagen":"c://img",
        "SKU":"002001",
        "Cantidad":"9",
        "Peso (Gr)":"1000",
        "Alto (Cm)":"9",
        "Ancho (Cm)":"9",
        "Creacion":"5/2/2023",
        "Actualizacion":"6/2/2023"
    }

    for x, y in producto.items():
        print(x + ": " + y)
        response = input("    Response: ")
        #ESCRIBE EXIT PARA DEJAR LOS VALORES POR DEFECTO
        if response == "exit":
            return producto
        producto[x] = response

    return producto
