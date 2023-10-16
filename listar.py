#Modulo - Listar
#Imprime los datos de forma tabulada

def listar(lista):
    print("NOMBRE        DESCRIPCION           CATEGORIA     PRECIO    IMAGEN      SKU     CANTIDAD    PESO   ALTO   ANCHO   CREACION   ACTUALIZACION")
    for prod in lista:
        print("{0:13} {1:21} {2:13} {3:9} {4:11} {5:10} {6:8} {7:6} {8:6} {9:7} {10:10} {11:0}".format(
            prod["Nombre"], prod["Descripcion"], prod["Categoria"], prod["Precio (Bs)"],
            prod["Imagen"], prod["SKU"], prod["Cantidad"], prod["Peso (Gr)"],
            prod["Alto (Cm)"],prod["Ancho (Cm)"], prod["Creacion"], prod["Actualizacion"]))





