"""
Listar los productos de forma ascendente según su cantidad
utilizando el algoritmo de heapsort
"""
from listar import listar

def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i]["Cantidad"] < arr[l]["Cantidad"]:
        largest = l

    if r < n and arr[largest]["Cantidad"] < arr[r]["Cantidad"]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i] # swap
        heapify(arr, n, largest)

def heapSort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] # swap
        heapify(arr, i, 0)


    print(listar(arr))