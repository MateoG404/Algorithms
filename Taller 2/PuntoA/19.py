def list_insert(L, x):
    x.next = L.head
    L.head = x