arr = [10, 3, 5, 20, 7, 4];
print("Original ", arr)

def heapify(arr): 
    n = len(arr) 
    last = getParent(n - 1)
    print ("Starting at index ", last, " with value ", arr[last])
    for i in range(last, -1, -1):  
        print ("Calling SiftDown on {} with value {}".format(i, arr[i]))
        siftDown(arr, i, n)
        print ("Returned array {}".format(arr))

def siftDown(arr, i, n): 
    left = getLeft(i)
    right = getRight(i)
    if(left < n): #make sure left is in the array
        max_index = left
        if(right < n) and arr[right] > arr[left]: 
           max_index = right
        if(arr[max_index] > arr[i]): 
            swap(arr, max_index, i)
            siftDown(arr, max_index, n)

def swap(arr, i, n): 
    temp = arr[i]
    arr[i] = arr[n]
    arr[n] = temp

def getParent(n): 
  return int((n-1)/2)

def getLeft(n): 
    return (2*n) + 1

def getRight(n): 
    return(2*n) + 2

heapify(arr)
print("Heapified array ", arr)
