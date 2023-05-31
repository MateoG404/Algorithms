def list_insert(L, x):
    x.next = L.nil.next
    L.nil.next = x

def list_delete(L, x):
    prev = L.nil
    while prev.next != x:
        if prev.next == L.nil:
            raise ValueError("Element does not exist")
        prev = prev.next
    prev.next = x.next

def list_search(L, k):
    x = L.nil.next
    while x != L.nil and x.key != k:
        x = x.next
    return x

