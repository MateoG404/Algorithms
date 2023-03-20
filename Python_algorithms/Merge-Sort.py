import array as arr

n_list = [5,2,4,7,1,3,2,6]

p = 0

r = len(n_list) - 1


def merge(n_list, p, q, r):
    n_1 = q - p + 1
    n_2 = r - q 
    L = [None] * (n_1 + 1)
    R = [None] * (n_2 + 1)
    
    for i in range(0, n_1):
        L[i] = n_list[p + i - 1]
        
    for j in range(0, n_2):
        R[j] = n_list[q + j]
        
    L[n_1] = float("inf")
    R[n_2] = float("inf")
    i = 0
    j = 0
    
    for k in range(p, r + 1):
        if L[i] <= R[j]:
            n_list[k] = L[i]
            i = i + 1
        elif n_list[k] == R[j]:
            j = j + 1

    

def merge_sort(n_list, p, r):
    if p < r:
        q = int((p+1 + r) / 2) - 1
        merge_sort(n_list, p, q)
        merge_sort(n_list, q + 1, r)
        merge(n_list, p, q, r)
    
    
merge_sort(n_list, p, r)

for i in n_list:
    print(i)
