#Listar productos según su cantidad de forma ascendente utilizando el
#algoritmo de quicksort

def partition(l, r, nums):
    pivot, ptr = nums[r]["Cantidad"], l
    for i in range(l, r):
        if nums[i]["Cantidad"] <= pivot:
            nums[i], nums[ptr] = nums[ptr], nums[i]
            ptr += 1

    nums[ptr], nums[r] = nums[r], nums[ptr]
    return ptr


def quicksort(l, r, nums):
    if len(nums) == 1:
        return nums
    if l < r:
        pi = partition(l, r, nums)
        quicksort(l, pi - 1, nums)
        quicksort(pi + 1, r, nums)
    return nums


