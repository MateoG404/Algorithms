def compactify_list(L, F):
    transpose(A[L.head], A[1])
    if F.head == 1:
        F.head = L.head
    L.head = 1
    l = A[L.head].next
    i = 2
    while l != NIL:
        transpose(A[l], A[i])
        if F == i:
            F = l
        l = A[l].next
        i = i + 1

def transpose(a, b):
    swap(a.prev.next, b.prev.next)
    swap(a.prev, b.prev)
    swap(a.next.prev, b.next.prev)
    swap(a.next, b.next)

def swap(x, y):
    temp = x
    x = y
    y = temp
