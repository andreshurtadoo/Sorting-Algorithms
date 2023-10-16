#Modulo - Lectura de archivo .CSV
#Leer CVS de productos y cargarlos a la lista de productos
import csv

def cargarProductosCSV(lista):
    #ABRIR ARCHIVO .CSV
    with open("productos.csv") as f:
        reader = csv.reader(f)
        print("NOMBRE           DESCRIPCION      CATEGORIA  PRECIO     IMAGEN   SKU   CANTIDAD    PESO  ALTO   ANCHO  CREACION  ACTUALIZACION")

        for row in reader:
            #LECTURA DE DATOS
            print("{0:16} {1:16} {2:10} {3:10} {4:8} {5:8} {6:8} {7:6} {8:6} {9:4} {10:10} {11}".format(
                row[0], row[1], row[2], row[3], row[4], row[5], row[6],
                row[7], row[8], row[9], row[10], row[11]))

            #AGREGAR DATA A LA LISTA
            producto = {
                "Nombre": row[0],
                "Descripcion": row[1],
                "Categoria": row[2],
                "Precio (Bs)": row[3],
                "Imagen": row[4],
                "SKU": row[5],
                "Cantidad": row[6],
                "Peso (Gr)": row[7],
                "Alto (Cm)": row[8],
                "Ancho (Cm)": row[9],
                "Creacion": row[10],
                "Actualizacion": row[11]
            }

            lista.append(producto)

        print("CARGA DE PRODUCTOS EXITOSA!!")
        return lista

