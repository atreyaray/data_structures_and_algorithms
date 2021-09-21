def partition(low, hi, pivot, arr) :
    
    temp = arr[low]
    arr[low] = arr[pivot]
    arr[pivot] = temp
    
    i = low+1
    j = hi
    while i <= j :
        if arr[i] >= arr[low] :
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            j -= 1
        else :
            i +=1
        
    i -= 1
    temp = arr[i] 
    arr[i] = arr[low]
    arr[low] = temp
    return i

def quickselect(low, hi, arr, k) :
    if low == hi:
        return arr[low]
    mid = low + (hi-low)//2
    partitionIndex = partition(low, hi, mid, arr)
    if k-1 > partitionIndex: 
        return quickselect(partitionIndex+1, hi, arr, k)
    elif partitionIndex > k-1 :
        return quickselect(low, partitionIndex-1, arr, k)
    else :
        return arr[partitionIndex]

def main() :
    # a = [4,1,5,3,2,7]
    a = [i for i in range(100, 0, -1)]
    # a = [i for i in range(1, 101, 1)]
    # print('pivot: ', a[49])
    # print(partition(0, len(a)-1, 49, a))
    ans = quickselect(0, len(a)-1, a, 63)
    print('ans', ans)


if __name__ == "__main__":
    main()
