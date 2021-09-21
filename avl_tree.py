class ListNode:
    def __init__(self, value=0, height=0, parent = None, left=None, right=None):
        self.val = value
        self.parent = parent
        self.right = right
        self.left = left
        self.height = height
    

class bst:
    def __init__(self):
        self.root = ListNode()
        self.length = 0

    """ 
    Inserting node x with key k :
        a. If current node k' == k then stop
        b. If current node k' > k then go left
        c. If current node k' < k then go right
        d. If either left or right child don't exist, 
           make a new child with given key
    
    After inserting :
        a. Update height of parent
    
    Apply balancing (including height update) on grandparent node (if it exists)
    """
    def insert(self, val):
        if self.root.val == 0:
            self.root = ListNode(val)
        else:
            temp = self.root
            found = False
            new = ListNode(val)
            while not found :
                if temp.val == val :
                    found = True
                elif temp.val > val :
                    if temp.left != None :
                        temp = temp.left
                    else :
                        temp.left = new
                        temp.left.parent = temp
                        temp.height += 1
                        found = True
                else :
                    if temp.right != None :
                        temp = temp.right
                    else :
                        temp.right = new
                        temp.right.parent = temp
                        temp.height += 1
                        found = True

            if temp.parent != None :
                balance(temp.parent)
                # while temp != None :
                #     h1 = temp.left.height if temp.left != None else -1
                #     h2 = temp.right.height if temp.right != None else -1
                #     temp.height = 1 + max(h1, h2)
                #     temp = temp.parent

    def balance(self, n) :
        temp = n 
        while n != None :
            h1 = temp.left.height if temp.left != None else -1
            h2 = temp.right.height if temp.right != None else -1
            if abs(h1 - h2) >= 2 :

                pass
            else :
                temp.height = 1 + max(h1, h2)
            temp = temp.parent
    
    def rotateRight(self, n) :
        pass

    def rotateLeft(self, n) :
        x = ListNode(n.val, parent = n, right = n.right.left, left = n.left)
        n.left = x 
        n.val = n.right.val
        n.right = n.right.right
        n.right.parent = n
    
    def printInOrder(self):
        temp = self.root
        def traverse(n):
            if n.left != None:
                traverse(n.left)
            print(n.val, end=' ')
            if n.right != None:
                traverse(n.right)
        traverse(temp)


def main() :
    print('hello')
    b = bst()
    l = [1,7,8,3,9,2]
    for i in l :
        print('Insert', i) 
        b.insert(i)
    b.printInOrder()

if __name__ == "__main__":
    main()
