def quicksort_sort(array,s,e):
    if e-s+1<=1:
        return array
    pivot = array[e]
    left = s
    
    for i in range(s,e):
        if array[i] < pivot:
            array[i], array[left] = array[left], array[i]
            left+=1
    
    array[left],array[e] = array[e],array[left]
    
    quicksort_sort(array,s,left-1)
    quicksort_sort(array,left+1,e)
    
    return array

list = [7,8,11,12,3,16,4,1]

quicksort_sort(list, 0, len(list)-1)
print(list)
