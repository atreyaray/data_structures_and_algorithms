'''
Select the k-th largest element of an array
'''
import random
def swap(a, i, j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp
    return a


def partition(a, start, end):

    index = random.randint(start, end)
    swap(a, index, end)
    p = a[end]

    i, j = start, start
    while j < end:
        if a[j] < p:
            swap(a, i, j)
            i += 1
        j += 1

    swap(a, end, i)
    return i

def quick_select(a, k) :
    def helper(a, k, start, end):
        p = partition(a, start, end)
        length = len(a)
        if p == length-k:
            return a[p]
        if p > length-k:
            return helper(a, k, start, p-1)
        elif p < length-k:
            return helper(a, k, p+1, end)

    return helper(a, k, 0, len(a)-1)


def main() :
    ls = [17, 21, 1, 19, 21, 7, 2, 20]
    print(quick_select(ls,4))

    pass

if __name__ == "__main__" :
    main()
