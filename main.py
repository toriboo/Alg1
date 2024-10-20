import random
import time
def swap(A,i, j):
    k = A[i]
    A[i] = A[j]
    A[j] = k
def insertion_sort(A):
    n = len(A)
    for i in range(1, n):
         j = i
         a = A[i]
         while(j > 0 and A[j-1]>a):
             if(A[j-1]>a):
                 A[j] = A[j-1]
             j -=1
         A[j] = a
    return A
def find_min(A, i,n):
    min_ind = i
    min_el = A[i]
    for j in range(i+1 ,n):
        if (A[j] < min_el):
            min_el = A[j]
            min_ind = j
    return min_ind
def selection_sort(A):
    n = len(A)
    for i in range(0, n):
        j = find_min(A, i, n)
        swap(A,i,j)
    return A
def is_sorted(A):
    n = len(A)
    for i in range(0, n-1):
        if (A[i]>A[i+1]):
            return False
    return True
def shuffle_elements(A):
    n = len(A)
    for i in range(0, n):
        rand_ind = random.randint(0,n-1)
        swap(A,i,rand_ind)
def Bogosort(A):
    n = len(A)
    while(not(is_sorted(A))):
        shuffle_elements(A)
    return A
def bubble_sort(A):
    n = len(A)
    sortB = False
    for i in range(0, n-1):
        sortB = True
        for j in range(0,n-i-1):
            if (A[j] > A[j+1]):
                swap(A, j ,j+1)
                sortB = False
        if (sorB):
            return A
    return A
def Merge(A, B):
    C = []
    i,j = 0,0
    n = len(A)
    m = len(B)
    while((i< n) and (j < m)):
        if (A[i] <= B[j]):
            C.append(A[i])
            i+=1
        else:
            C.append(B[j])
            j += 1
    while(i < n):
        C.append(A[i])
        i+=1
    while(j< m):
        C.append(B[j])
        j+=1
    return C
def merge_sort(A):
    n = len(A)
    if (n <= 1): return A
    else:
        middle = n//2
        left = merge_sort(A[:middle])
        right = merge_sort(A[middle:])
        return Merge(left,right)
def quick_sort(A):
    n = len(A)
    if (n <= 1): return A
    if (n >=2):
        pivot = A[n//2]
        left = [x for x in A if x < pivot]
        middle = [x for x in A if x == pivot]
        right = [x for x in A if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)
def heapify(A, i):
    n = len(A)
    smaller = i
    left = 2*i +1
    right = 2*i + 2
    if (left < n and A[left] < A[smaller]):
        smaller = left
    if (right < n and A[right] < A[smaller]):
        smaller = right
    if ( i != smaller):
        swap(A, i, smaller)
def heap_sort(A):
    n = len(A)
    for i in range(n,-1,-1):
        heapify(A, i)
    return A
def shell_sort(A):
    n = len(A)
    for gap in gaps:
        for i in range(gap, n):
            j = i
            a = A[i]
            while (j >= gap and A[j-gap] > a):
                A[j] = A[j-gap]
                j = j - gap
            A[j] = a
    return A
def gaps_shell(A):
    gaps = []
    n = len(A)
    n //= 2
    while (n >= 1):
        gaps.append(n)
        n //= 2
    return gaps
def gaps_hib(A):
    n = len(A)
    gaps = []
    k = 1
    gaps.append(1)
    while ( 2**k -1 < n):
        gaps.append(2**k - 1)
        k += 1
    return gaps[n:0:-1]
def gaps_pratt(A):
    n = len(A)
    ar1 = [2**i for i in range(0, n)]
    ar2 = [3**j for j in range(0, n)]
    gaps = sorted(c*d for c in ar1 for d in ar2 if c*d <= n)
    return gaps[len(gaps):0:-1]+[1]


A = []
random.seed(21)
n = 1000
A = [random.randint(0, n//2) for i in range(n)]
#print(A)
time1 = time.time()
#insertion_sort(A)

#selection_sort(A)
#Bogosort(A)
#bubble_sort(A)
#A = merge_sort(A)
#A = quick_sort(A)
#heap_sort(A)
#gaps = gaps_shell(A)
#gaps = gaps_hib(A)
#gaps = gaps_pratt(A)
#shell_sort(A)
time2 = time.time()
print(time2-time1)
#print(A)







