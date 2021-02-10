'''
Time Complexity - 
    1. Best Case : O(nlogn)
    2. Worst Case : O(n^2)
    (Depends on the selection of the pivot, good pivot when array divided into two sub
    array of roughly the size)

Unstable (Order is not maintained)
In-place, no extra memory required
'''
import random
 
def swap(a, i, j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp
    return a

def partition(a, start, end) :
    
    index = random.randint(start, end)
    swap(a, index, end)
    p = a[end]

    i, j = start, start
    while j < end :
        if a[j] < p :
            swap(a, i, j)
            i += 1
        j += 1 

    swap(a, end, i)
    return i 

def quick_sort(a):

    def helper(a, start, end) :
        p = partition(a, start, end)
        if start+1 < p :
            helper(a, start, p)
        if p+1 < end :
            helper(a, p+1, end)
        return a

    return helper(a, 0, len(a)-1)

def main() :
    # ls = [9, 6, 1, 4, 8, 3]
    ls = [17, 21, 1, 19, 21, 7, 2, 20]
    print(quick_sort(ls))

if __name__ == "__main__" :
    main()
