#Modulo - Sub menu
#Sub-menu de reportes

def subMenu():
    opc = 0
    opc += int(input("\nLISTAR PRODUCTOS POR \n 1-Su Cantidad => quicksort \n 2-Su Peso => mergesort \n 3-Su Fecha => shellsort \n 4-Su Cantidad => heapsort \n 5-Su Dimension => su elección \n 6-Volver \n Opcion: "))
    return opc

