"""
Listar productos de forma ascendente o descendente según su fecha
de creación utilizando el algoritmo de shellsort. La opción de
ordenamiento será seleccionada por el usuario
"""

def shellSort(array, n):
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i

            while j >= interval and array[j - interval] < temp:
                array[j] = array[j - interval]
                j -= interval

            array[j] = temp
        interval //= 2

dataa = [
    {'Nombre': 'Harina', 'Descripcion': 'Harina Pan', 'Categoria': 'Alimento', 'Precio (Bs)': '1000', 'Imagen': 'c://img', 'SKU': '001001', 'Cantidad': '20', 'Peso (Gr)': '1000', 'Alto (Cm)': '10', 'Ancho (Cm)': '10', 'Creacion':'5/2/2023', 'Actualizacion':'5/3/2023'},
    {'Nombre': 'Pasta', 'Descripcion': 'Pasta Larga', 'Categoria': 'Alimento', 'Precio (Bs)': '2400', 'Imagen': 'c://img', 'SKU': '001001', 'Cantidad': '19', 'Peso (Gr)': '1000', 'Alto (Cm)': '10', 'Ancho (Cm)': '10', 'Creacion':'6/2/2023', 'Actualizacion':'6/3/2023'},
    {'Nombre': 'Cafe', 'Descripcion': 'Cafe la Pastora', 'Categoria': 'Alimento', 'Precio (Bs)': '2000', 'Imagen': 'c://img', 'SKU': '001001', 'Cantidad': '40', 'Peso (Gr)': '1000', 'Alto (Cm)': '10', 'Ancho (Cm)': '10', 'Creacion':'7/2/2023', 'Actualizacion':'7/3/2023'},
    {'Nombre': 'Leche', 'Descripcion': ' Leche Parmalat', 'Categoria': 'Alimento', 'Precio (Bs)': '3000', 'Imagen': 'c://img', 'SKU': '001001', 'Cantidad': '50', 'Peso (Gr)': '1000', 'Alto (Cm)': '10', 'Ancho (Cm)': '10', 'Creacion':'8/2/2023', 'Actualizacion':'8/3/2023'},
    {'Nombre': 'Arroz', 'Descripcion': 'Arroz Mary', 'Categoria': 'Alimento', 'Precio (Bs)': '1500', 'Imagen': 'c://img', 'SKU': '001001', 'Cantidad': '55', 'Peso (Gr)': '1000', 'Alto (Cm)': '10', 'Ancho (Cm)': '10', 'Creacion':'9/2/2023', 'Actualizacion':'9/3/2023'},
    {'Nombre': 'Detergente', 'Descripcion': 'Detergente', 'Categoria': 'Hogar', 'Precio (Bs)': '3600', 'Imagen': 'c://img', 'SKU': '002001', 'Cantidad': '31', 'Peso (Gr)': '1000', 'Alto (Cm)': '10', 'Ancho (Cm)': '10', 'Creacion':'10/2/2023', 'Actualizacion':'10/3/2023'},
    {'Nombre': 'Jabon', 'Descripcion': 'Jabon Avon', 'Categoria': 'Hogar', 'Precio (Bs)': '500', 'Imagen': 'c://img', 'SKU': '002001', 'Cantidad': '36', 'Peso (Gr)': '1000', 'Alto (Cm)': '10', 'Ancho (Cm)': '10', 'Creacion':'11/2/2023', 'Actualizacion':'11/3/2023'},
    {'Nombre': 'Talco', 'Descripcion': 'Talco Blanco', 'Categoria': 'Hogar', 'Precio (Bs)': '2000', 'Imagen': 'c://img', 'SKU': '002001', 'Cantidad': '18', 'Peso (Gr)': '1000', 'Alto (Cm)': '10', 'Ancho (Cm)': '10', 'Creacion':'12/2/2023', 'Actualizacion':'12/3/2023'},
    {'Nombre': 'Desodorante', 'Descripcion': 'Rexona', 'Categoria': 'Hogar', 'Precio (Bs)': '1900', 'Imagen': 'c://img', 'SKU': '002001', 'Cantidad': '45', 'Peso (Gr)': '1000', 'Alto (Cm)': '10', 'Ancho (Cm)': '10', 'Creacion':'13/2/2023', 'Actualizacion':'13/3/2023'},
    {'Nombre': 'Suavizante', 'Descripcion': 'Ariel', 'Categoria': 'Hogar', 'Precio (Bs)': '2650', 'Imagen': 'c://img', 'SKU': '002001', 'Cantidad': '22', 'Peso (Gr)': '1000', 'Alto (Cm)': '10', 'Ancho (Cm)': '10', 'Creacion':'14/2/2023', 'Actualizacion':'14/3/2023'}
]
data = [9, 8, 3, 7, 5, 6, 4, 1]
size = len(data)
shellSort(data, size)
print('Sorted Array in Ascending Order:')
print(data)