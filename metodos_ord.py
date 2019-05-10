def insercionDirecta(lista, tam):
    for i in range(1, tam):
        v = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > v:
            lista[j + 1] = lista[j]
            j = j - 1
        lista[j + 1] = v

def heapsort(lista, tam):
    for k in range(tam - 1, -1, -1):
        for i in range(0, k):
            item = lista[i]
            j = (i + 1) / 2
            while j >= 0 and lista[j] < item:
                lista[i] = lista[j]
                i = j
                j = j / 2
            lista[i] = item
        temp = lista[0];
    lista[0] = lista[k];
    lista[k] = temp;


def quicksort(lista, izq, der):
    i = izq
    j = der
    x = lista[(izq + der) / 2]

    while (i <= j):
        while lista[i] < x and j <= der:
            i = i + 1
        while x < lista[j] and j > izq:
            j = j - 1
        if i <= j:
            aux = lista[i];
            lista[i] = lista[j];
            lista[j] = aux;
            i = i + 1;
            j = j - 1;

        if izq < j:
            quicksort(lista, izq, j);
    if i < der:
        quicksort(lista, i, der);

def count_sort(arr, max):
    m = max + 1
    counter = [0] * m
    for i in arr:
     counter[i] += 1
    a = 0

    for i in range(m):
        for k in range(counter[i]):
            arr[a] = i
            a += 1
    return arr


def radix_sort(random_list):
    len_random_list = len(random_list)
    modulus = 10
    div = 1
    while True:
        # empty array, [[] for i in range(10)]
        new_list = [[], [], [], [], [], [], [], [], [], []]
        for value in random_list:
            least_digit = value % modulus
            least_digit /= div
            new_list[least_digit].append(value)
        modulus = modulus * 10
        div = div * 10

        if len(new_list[0]) == len_random_list:
            return new_list[0]

        random_list = []
        rd_list_append = random_list.append
        for x in new_list:
            for y in x:
                rd_list_append(y)

                def mergeSort(alist):
                    # ("Desordenado ",alist)
                    if len(alist) > 1:
                        mid = len(alist) // 2
                        lefthalf = alist[:mid]
                        righthalf = alist[mid:]

                        mergeSort(lefthalf)
                        mergeSort(righthalf)

                        i = 0
                        j = 0
                        k = 0
                        while i < len(lefthalf) and j < len(righthalf):
                            if lefthalf[i] < righthalf[j]:
                                alist[k] = lefthalf[i]
                                i = i + 1
                            else:
                                alist[k] = righthalf[j]
                                j = j + 1
                            k = k + 1

                        while i < len(lefthalf):
                            alist[k] = lefthalf[i]
                            i = i + 1
                            k = k + 1

                        while j < len(righthalf):
                            alist[k] = righthalf[j]
                            j = j + 1
                            k = k + 1
                            # print("Ordenando ",alist)
def mergesort(alist):
    #("Desordenado ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergesort(lefthalf)
        mergesort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    #print("Ordenando ",alist)