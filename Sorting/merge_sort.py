# Time complexity O(n^2)
# Space complexity O(n)
# 
# Divide and Conquer used
# Subroutine ''merge'' merges sorted subarrays [a0, a1] [a2, a3] => [a0, a1, a2, a3]
# Main procedure splits array recursively and then calls the merge method


def merge(a, start, mid, end):
    aux = []
    i, j, dest = start, mid, start
    while i < mid and j <= end :
        if a[i] <= a[j] :
            aux.append(a[i])
            i += 1
        else: 
            aux.append(a[j])
            j += 1 

    while i < mid : 
        aux.append(a[i])
        i += 1

    while j <= end :
        aux.append(a[j])
        j += 1


    for i in range(len(aux)) :
        a[dest] = aux[i]
        dest += 1
    
    return a
    


def merge_sort(a) :
    length = len(a)

    if length < 1 : 
        return a

    def helper(a, start, end) :
        if start >= end :
            return 
        mid = start + (end-start)//2
        helper(a, start, mid)
        helper(a, mid+1, end)
        merge(a, start, mid+1, end)
        return a


    return helper(a, 0, length-1)


def main() :
    ls = [17,21,1,19,21,7,2,20]
    print(merge_sort(ls))
    pass

if __name__ == "__main__" :
    main()