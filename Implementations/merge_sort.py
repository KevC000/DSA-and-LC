def merge(array, start, mid, end):
    left = array[start:mid+1]
    right = array[mid+1:end+1]
    
    a,l,r = start, 0, 0,
    
    while l<len(left) and r<len(right):
        if left[l]<=right[r]:
            array[a] = left[l]
            l+=1
        else:
            array[a] = right[r]
            r+=1
        a+=1
            
    while l < len(left):
        array[a] = left[l]
        l+=1
        a+=1
    while r < len(right):
        array[a] = right[r]
        r+=1
        a+=1

def merge_sort(array, start , end):
    if end-start+1 <= 1:
        return array
    
    merge_sort(array, start, (start+end)//2)
    merge_sort(array, (start+end)//2+1, end)
    
    merge(array, start, (start+end)//2, end)
    return array
    
list = [9, 12, 3, 11, 5, 9, 2, 26, 1, 7]

merge_sort(list, 0, len(list))
print(list)

    
