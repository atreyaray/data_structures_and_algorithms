class priorityQueue :
    # constructor
    def __init__(self,l) :
        self.lst = [l]
        self.size = len(self.lst)

    def is_empty(self) :
        '''
        checks whether queue is empty or not
        '''
        return self.size == 0

    #upheap
    def upheap(self, i) :
        if i-1 >= 0 and self.lst[i] > self.lst[(i-1)//2] :
            temp = self.lst[i]
            self.lst[i] = self.lst[(i-1)//2]
            self.lst[(i-1)//2] = temp
            self.upheap((i-1)//2)
        else :
            return

    #downheap
    def downheap(self, i) :
        # children exist?
        children = False if (2*i + 1 > self.size -1)  else True
        if(not children) :
            return
        # left child exists?
        lc = 2*i+2 <= self.size-1
        child = 2*i + 1
        if(lc) :
            if(self.lst[2*i+1] < self.lst[2*i+2]) :
                child = 2*i + 2
        # return if parent is greater than child
        if(self.lst[child] <= self.lst[i]) :
            return
        # swap
        temp = self.lst[child]
        self.lst[child] = self.lst[i]
        self.lst[i] = temp
        self.downheap(child)


    #insert
    def insert(self, n) :
        '''
        Insert a new element n in the queue
        '''
        self.lst.append(n)  
        self.size += 1
        self.upheap(self.size-1)
        print('New list', self.lst)

    #max
    def max(self) :
        '''
        Returns the largest element of the queue
        '''
        return self.lst[0]

    #remove max
    def remove_max(self):
        '''
        Removes the largest element of the queue
        '''
        temp = self.lst[self.size-1]
        self.lst[0] = temp
        del self.lst[-1]
        self.size-= 1
        self.downheap(0)
        print('New list', self.lst)
    
    def increase_key(self, i, n) :
        '''
        Increases the key of the element at index i
        '''
        if i >= self.size :
            print("Index out of range")
        elif n <= self.lst[i]:
            print("Use decrease_key instead")
        else :
            self.lst[i] = n
            self.upheap(i)
            print('New list', self.lst)

    def decrease_key(self, i, n) :
        '''
        Decreases the key of the element at index i
        '''
        if i >= self.size:
            print("Index out of range")
        elif n >= self.lst[i] :
            print("Use increase_key instead")
        else : 
            self.lst[i] = n
            self.downheap(i)
            print('New list', self.lst)
        


def main() :
    l = 1
    p = priorityQueue(l)
    p.max()




if __name__ == "__main__":
    main()
