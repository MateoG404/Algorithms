def cycle_sort(array):
    n = len(array)
    for i in range(0, n-1):
        item = array[i]
        pos = i
        
        # Find the position to put the item in its correct position
        for j in range(i+1, n):
            if array[j] < item:
                pos += 1
        
        # If the item is already in its correct position, continue to the next item
        if pos == i:
            continue
        
        # Place the item in its correct position
        while item == array[pos]:
            pos += 1
            
        array[pos], item = item, array[pos]
        
        # Rotate the elements in the cycle

        while pos != i:
            pos = i
            for j in range(i+1, n):
                if array[j] < item:
                    pos += 1
            while item == array[pos]:
                pos += 1
            array[pos], item = item, array[pos]
    return array