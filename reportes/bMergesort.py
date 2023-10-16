#Listar productos de forma descendente según su peso en un rango de
#fecha de actualización introducido por el usuario, utilizando el
#algoritmo de mergesort
from listar import listar

def merge_sort(list, desde, hasta):
    list_length = len(list)

    if list_length == 1:
        return list

    mid_point = list_length // 2

    left_partition = merge_sort(list[:mid_point], 0, 0)
    right_partition = merge_sort(list[mid_point:], 0, 0)

    return merge(left_partition, right_partition, desde, hasta)

def merge(left, right, desde, hasta):
    output = []
    i = j = 0

    while i < len(left) and j < len(right):
        #SUMAMOS LOS DATOS DE LA FECHA
        left_string = left[i]["Actualizacion"].split('/')
        left_int_suma = sum((list(map(int , left_string))))
        right_string = right[j]["Actualizacion"].split('/')
        right_int_suma = sum((list(map(int, right_string))))

        listaNueva = []
        if( ((left_int_suma and right_int_suma) > desde) and ((right_int_suma and left_int_suma) < hasta)):
            listaNueva.append(left[i])
            listaNueva.append(right[j])

        if left[i]["Peso (Gr)"] > right[j]["Peso (Gr)"]:
            output.append(left[i])
            i += 1
        else:
            output.append(right[j])
            j += 1

    output.extend(left[i:])
    output.extend(right[j:])
    return output

def run_merge_sort(lista, desde, hasta):
    desdeV = desde.split('/')
    desdeSum = sum((list(map(int , desdeV))))
    hastaV = hasta.split('/')
    hastaSum = sum((list(map(int , hastaV))))

    sorted_list = merge_sort(lista, desdeSum, hastaSum)
    listar(sorted_list)


lista = [
{'Nombre': 'Harina', 'Descripcion': 'Harina Pan', 'Categoria': 'Alimento', 'Precio (Bs)': '1000', 'Imagen': 'c://img', 'SKU': '001001', 'Cantidad': '20', 'Peso (Gr)': '1100', 'Alto (Cm)': '10', 'Ancho (Cm)': '10', 'Creacion': '5/2/2023', 'Actualizacion': '14/2/2023'},
{'Nombre': 'Pasta', 'Descripcion': 'Pasta Larga', 'Categoria': 'Alimento', 'Precio (Bs)': '2400', 'Imagen': 'c://img', 'SKU': '001001', 'Cantidad': '19', 'Peso (Gr)': '1200', 'Alto (Cm)': '10', 'Ancho (Cm)': '10', 'Creacion': '8/2/2023', 'Actualizacion': '13/2/2023'},
{'Nombre': 'Cafe', 'Descripcion': 'Cafe la Pastora', 'Categoria': 'Alimento', 'Precio (Bs)': '2000', 'Imagen': 'c://img', 'SKU': '001001', 'Cantidad': '18', 'Peso (Gr)': '1300', 'Alto (Cm)': '10', 'Ancho (Cm)': '10', 'Creacion': '9/2/2023', 'Actualizacion': '12/2/2023'},
{'Nombre': 'Leche', 'Descripcion': ' Leche Parmalat', 'Categoria': 'Alimento', 'Precio (Bs)': '3000', 'Imagen': 'c://img', 'SKU': '001001', 'Cantidad': '17', 'Peso (Gr)': '1400', 'Alto (Cm)': '10', 'Ancho (Cm)': '10', 'Creacion': '10/2/2023', 'Actualizacion': '11/2/2023'},
{'Nombre': 'Arroz', 'Descripcion': 'Arroz Mary', 'Categoria': 'Alimento', 'Precio (Bs)': '1500', 'Imagen': 'c://img', 'SKU': '001001', 'Cantidad': '16', 'Peso (Gr)': '1500', 'Alto (Cm)': '10', 'Ancho (Cm)': '10', 'Creacion': '11/2/2023', 'Actualizacion': '10/2/2023'},
{'Nombre': 'Detergente', 'Descripcion': 'Detergente', 'Categoria': 'Hogar', 'Precio (Bs)': '3600', 'Imagen': 'c://img', 'SKU': '002001', 'Cantidad': '15', 'Peso (Gr)': '1600', 'Alto (Cm)': '10', 'Ancho (Cm)': '10', 'Creacion': '11/2/2023', 'Actualizacion': '9/2/2023'},
{'Nombre': 'Jabon', 'Descripcion': 'Jabon Avon', 'Categoria': 'Hogar', 'Precio (Bs)': '500', 'Imagen': 'c://img', 'SKU': '002001', 'Cantidad': '14', 'Peso (Gr)': '1700', 'Alto (Cm)': '10', 'Ancho (Cm)': '10', 'Creacion': '12/2/2023', 'Actualizacion': '8/2/2023'},
{'Nombre': 'Talco', 'Descripcion': 'Talco Blanco', 'Categoria': 'Hogar', 'Precio (Bs)': '2000', 'Imagen': 'c://img', 'SKU': '002001', 'Cantidad': '13', 'Peso (Gr)': '1800', 'Alto (Cm)': '10', 'Ancho (Cm)': '10', 'Creacion': '13/2/2023', 'Actualizacion': '7/2/2023'},
{'Nombre': 'Desodorante', 'Descripcion': 'Rexona', 'Categoria': 'Hogar', 'Precio (Bs)': '1900', 'Imagen': 'c://img', 'SKU': '002001', 'Cantidad': '12', 'Peso (Gr)': '1900', 'Alto (Cm)': '10', 'Ancho (Cm)': '10', 'Creacion': '14/2/2023', 'Actualizacion': '6/2/2023'},
{'Nombre': 'Suavizante', 'Descripcion': 'Ariel', 'Categoria': 'Hogar', 'Precio (Bs)': '2650', 'Imagen': 'c://img', 'SKU': '002001', 'Cantidad': '11', 'Peso (Gr)': '2000', 'Alto (Cm)': '10', 'Ancho (Cm)': '10', 'Creacion': '15/2/2023', 'Actualizacion': '5/2/2023'}
]


