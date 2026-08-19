def bubble_sort(lista):
    n= len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):         
            if lista[j]>lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

number = [5,3,8,2,4,9,7,3,1,6]
print(f"original list: {number}")

order = bubble_sort(number)
print(f"sort list: {order}")
