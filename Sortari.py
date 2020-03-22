
f=open("file.txt")
def readNumbers(f):

    l = []
    for x in f.readlines():
        x = x.strip('\n').split()
        l.append(x)
    k = []
    for i in l:
        for j in i:
            k.append(int(j))
    return k

v1=v2=v3=v4=v5=readNumbers(f)
#COUNTSORT:

def CountSort(v):
    count = [0 for i in range(max(v) + 1)]
    for i in range(len(v)):
        count[v[i]] = v.count(v[i])
    mini=min(v)
    maxi=max(v)
    v=[]
    for i in range(mini, maxi + 1):
        while count[i] > 0:
            v.append(i)
            count[i] = count[i] - 1
    return v

def verificare(v):
    ok=1
    for i in range(len(v)-1):
        if v[i]>v[i+1]:
            ok=0
            break
    return ok

v1=CountSort(v1)

if(verificare(v1)==1):
    print("Count sort correct")
else:
    print("Count sort incorrect")











#BUBBLESORT:

def BubbleSort(v):
    for i in range(len(v)):
        for j in range(0, len(v) - i - 1):
            if v[j] > v[j + 1]:
                aux=v[j]
                v[j]=v[j+1]
                v[j+1]=aux
    return v

def verificare(v):
    ok=1
    for i in range(len(v)-1):
        if v[i]>v[i+1]:
            ok=0
            break
    return ok


v2=BubbleSort(v2)

if(verificare(v2)==1):
    print("Bubble sort correct")
else:
    print("Bubble sort incorrect")











#MergeSort:

def MergeSort(v):
    if len(v) > 1:
        mid = len(v) // 2
        left = v[:mid]
        right = v[mid:]


        MergeSort(left)
        MergeSort(right)

        i = 0
        j = 0


        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:

                v[k] = left[i]

                i += 1
            else:
                v[k] = right[j]
                j += 1

            k += 1


        while i < len(left):
            v[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            v[k] = right[j]
            j += 1
            k += 1
    return v

v3=MergeSort(v3)
if(verificare(v3)==1):
    print("Merge sort correct")
else:
    print("Merge sort incorrect")










#QUICKSORT:

def quicksort(v):
    if len(v) == 1 or len(v) == 0:
        return v
    else:
        pivot = v[0]
        i = 0
        for j in range(len(v)-1):
            if v[j+1] < pivot:
                v[j+1],v[i+1] = v[i+1], v[j+1]
                i += 1
        v[0],v[i] = v[i],v[0]
        first_part = quicksort(v[:i])
        second_part = quicksort(v[i+1:])
        first_part.append(v[i])
        return first_part + second_part
f=open("file.txt")
def readNumbers(f):

    l = []
    for x in f.readlines():
        x = x.strip('\n').split()
        l.append(x)
    k = []
    for i in l:
        for j in i:
            k.append(int(j))
    return k

if(verificare(v4)==1):
    print("Quick sort correct")
else:
    print("Quick sort incorrect")










#RadixSort:

def countingSort(v, place):
    n = len(av)
    output = [0] * n
    count = [0] * 10

    for i in range(0, n):
        index = v[i]
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n  - 1
    while i >= 0:
        index = v[i]
        output[count[index % 10] - 1] = array[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(0, size):
        array[i] = output[i]


def radixSort(array):
    max_element = max(array)
    place = 1
    while max_element // place > 0:
        countingSort(array, place)
        place *= 10

if(verificare(v5)==1):
    print("Radix sort correct")
else:
    print("Radix sort incorrect")


