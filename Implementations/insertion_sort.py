def insertion_sort(array):
    for i in range(len(array)):
        curr = array[i]
        j = i
        while j>0 and curr<array[j-1]:
            array[j],array[j-1]=array[j-1],array[j]
            j-=1
            
arr = [5,6,1,10,2,8]            
insertion_sort(arr)
print(arr)