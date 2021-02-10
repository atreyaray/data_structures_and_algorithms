# Time Complexity O(n^2)
# Space Complexity O(n)

def quickSort(a) :
    length = len(a)
    # i goes from 0 to length - 1
    for i in range(length-1) :
        # min element and it's index are required
        min = a[i]
        index = i
        # j goes from i+1 to length
        for j in range(i+1, length): 
            if a[j] < min :
                min = a[j]
                index = j
        a[index] = a[i]
        a[i] = min
    return a


def main() :
    ls = [1,2, 2, 3,4,5,6,7,8,9]
    print(quickSort(ls))
    pass

if __name__ == "__main__" :
    main()