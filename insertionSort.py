def insertionSort(arr):
    """
        Sort elements in an array using via Insertion
    
        Input: 
            - arr: An array
        Output:
            - sorted: An array that is sorted 
    """
    sorted = []
    for j in range(1,len(arr)):
        key = arr[j]
        i = j-1
        
        while(i > 0 and arr[i] > key):
            arr[i+1] = arr[i]
            i = i-1
        arr[i+1] = key
        sorted.append(arr[i+1])
    return sorted

if __name__ == "__main__":

    arr = [10,1,4,5,12,32]
    print ("Sorted array is:", insertionSort(arr))
