"""
Listar productos de forma ascendente o descendente según sus
dimensiones y antigüedad en un rango de fecha(Utilizar algoritmo de
ordenamiento de su elección)
"""
from listar import listar

def merge_sort(list):
    list_length = len(list)

    if list_length == 1:
        return list

    mid_point = list_length // 2

    left_partition = merge_sort(list[:mid_point])
    right_partition = merge_sort(list[mid_point:])

    return merge(left_partition, right_partition)

def merge(left, right):
    output = []
    i = j = 0
    while i < len(left) and j < len(right):
        #RELACION ENTRE DIMENSION Y ANTIGUEDAD
        dim_left = int(left[i]["Alto (Cm)"]) * int(left[i]["Ancho (Cm)"])
        dim_right = int(right[i]["Alto (Cm)"]) * int(right[i]["Ancho (Cm)"])

        left_string = left[i]["Creacion"].split('/')
        left_suma = sum((list(map(int, left_string))))
        right_string = right[j]["Creacion"].split('/')
        right_suma = sum((list(map(int, right_string))))

        if left_suma+dim_left < right_suma+dim_right:
            output.append(left[i])
            i += 1
        else:
            output.append(right[j])
            j += 1

    output.extend(left[i:])
    output.extend(right[j:])
    return output

def run_merge_sort2(lista):
    sorted_list = merge_sort(lista)
    listar(sorted_list)



