#Modulo - Consultar
#Consultar un producto por medio de su nombre

def consultar(lista, nombre):
    band = False
    for prod in lista:
        if prod["Nombre"] == nombre:
            band = True
            print("NOMBRE        DESCRIPCION         CATEGORIA   PRECIO     IMAGEN   SKU   CANTIDAD    PESO  ALTO   ANCHO   CREACION  ACTUALIZACION")
            print("{0:13} {1:20} {2:11} {3:9} {4:9} {5:8} {6:8} {7:6} {8:6} {9:4}".format(
                prod["Nombre"], prod["Descripcion"], prod["Categoria"], prod["Precio (Bs)"],
                prod["Imagen"], prod["SKU"], prod["Cantidad"], prod["Peso (Gr)"], prod["Alto (Cm)"],
                prod["Ancho (Cm)"], prod["Creacion"], prod["Actualizacion"]))
            return

    if band == False:
        return print("NO EXITE ESE PRODUCTO EN LA LISTA!\n")