def insertion_sort(a) :
    length = len(a)
    for i in range(1,length):
        j = i 
        while j > 0 and a[j] < a[j-1] :
            temp = a[j]
            a[j] = a[j-1]
            a[j-1] = temp
            j -= 1
    return a


def main() :
    ls = [9, 8, 7, 6, 5, 4, 3, 2]
    print(insertion_sort(ls))
    pass

if __name__ == "__main__" :
    main()
