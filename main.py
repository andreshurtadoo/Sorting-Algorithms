#Modulo - Principal
#Importacion de modulos
from menu import menu
from crear import crear
from modificar import modificar
from csvReader import cargarProductosCSV
from consultar import consultar
from listar import listar
#REPORTES
from reportes.sub_menu import subMenu
from reportes.aQuicksort import quicksort
from reportes.bMergesort import run_merge_sort
from reportes.dHeapsort import heapSort
from reportes.eCualquier import run_merge_sort2

#VARIABLES
lista = []
band = True

#PROGRAMA PRINCIPAL
while(band):
    try:
        opc = menu()
        #OPCION 1 - CREAR
        if opc == 1:
            print('\nCREAR NUEVO PRODUCTO - exit para dejar los valores por defecto')
            lista.append(crear())

        #OPCION 2 - MODIFICAR
        elif opc == 2:
            print('\nMODIFICAR PRODUCTO')
            if len(lista) == 0:
                print('NO HAY PRODUCTOS EN LA LISTA!')
            else:
                nombreProducto = input('Indique el nombre del producto: ')
                modificar(lista, nombreProducto)

        #OPCION 3 - CONSULTAR
        elif opc == 3:
            print('\nCONSULTAR PRODUCTO')
            if len(lista) == 0:
                print('NO HAY PRODUCTOS EN LA LISTA!')
            else:
                nombreProducto = input('Indique el nombre del producto: ')
                consultar(lista, nombreProducto)

        #OPCION 4 - LISTAR
        elif opc == 4:
            print('\nLISTAR PRODUCTOS')
            if len(lista) == 0:
                print('NO HAY PRODUCTOS EN LA LISTA!')
            else:
                listar(lista)

        #OPCION 5 - CARGAR PRODUCTOS DE PRUEBA
        elif opc == 5:
            print('\nCARGAR PRODUCTOS DE PRUEBA')
            lista = cargarProductosCSV(lista)

        #OPCION 6 - RESPORTES
        elif opc == 6:
            opcReporte = subMenu()
            #QUICKSORT
            if opcReporte == 1:
                lista = quicksort(0, len(lista)-1 ,lista)
                listar(lista)

            #MERGESORT
            elif opcReporte == 2:
                desde = input('Indique desde que fecha: ')
                hasta = input('Indique hasta que fecha: ')
                run_merge_sort(lista, desde, hasta)

            #SHELLSORT - REPARANDO
            elif opcReporte == 3:
                pass

            #HEAPSORT
            elif opcReporte == 4:
                heapSort(lista)

            #DECICION ALEATORIA
            elif opcReporte == 5:
                run_merge_sort2(lista)

        #OPCION 7 - FINALIZAR
        elif opc == 7:
            print('\nFINALIZAR')
            band = False

        #OPCION NO DESEADA
        else:
            print('\nESCOJA UNA OPCION EXISTENTE\n')

    except ValueError:
        print("\nSOLO VALORES NUMERICOS\n")

