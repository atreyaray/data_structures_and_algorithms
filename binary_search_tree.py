class ListNode :
    def __init__ (self, value = 0, left = None, right = None) :
        self.val = value
        self.right = right
        self.left = left

class bst :
    def __init__ (self) :
        self.root = ListNode()
        self.length = 0
    
    def search (self, val) :
        def _search(node) :
            if val == node.val :
                return True
            elif node.val > val :
                # go left
                if node.left != None :
                    return True and _search(node.left)  
                else :
                    return False
            else : 
                # go right
                if node.right != None :
                    return True and _search(node.right)  
                else :
                    return False
        return _search(self.root)

    
    def insert(self,val) :
        if self.root.val == 0 :
            self.root = ListNode(val)
        else :
            def _search_and_insert(node):
                if val == node.val :
                    return 
                elif node.val > val :
                    # go left
                    if node.left != None :
                        _search_and_insert(node.left) 
                    else :
                        node.left = ListNode(val)
                else : 
                    # go right
                    if node.right != None :
                        _search_and_insert(node.right)  
                    else :
                        node.right = ListNode(val)
            _search_and_insert(self.root)
    
    def min(self) :
        temp = self.root
        while(temp.left != None) :
            temp = temp.left
        return temp.val

    def max(self) :
        temp = self.root
        while (temp.right != None) :
            temp = temp.right
        return temp.val

    def predecessor(self, val) :
        def _pred(n, best) :
            if n.val >= val :
                if n.left != None :
                    return _pred(n.left, best)
                else :
                    return best
            else :
                best = n.val
                if n .right != None :
                    return _pred(n.right, best)
                else :
                    return best
        return _pred(self.root, None)

    def successor(self, val) :
        def _succ(n, best):
            if n.val > val:
                best = n.val
                if n.left != None:
                    return _succ(n.left, best)
                else:
                    return best
            else:
                if n .right != None:
                    return _succ(n.right, best)
                else:
                    return best
        return _succ(self.root, None)

    def printInOrder(self) :
        temp = self.root
        def traverse(n) :
            if n.left != None :
                traverse(n.left)
            print(n.val, end=' ')
            if n.right != None :
                traverse(n.right)
        traverse(temp)
        
    
    
def main() :
    b = bst()
    b.insert(1)
    b.insert(7)
    b.insert(8)
    b.insert(3)
    b.insert(9)
    b.insert(2)

    print('The element {n} does exist in the tree : {cond}'.format(n = 3, cond = b.search(3)))
    print('The element {n} does exist in the tree : {cond}'.format(n = 2, cond = b.search(2)))
    print('Predecessor of {n} is {ans}'.format(n = 3, ans = b.predecessor(3)))
    print('Successor of {n} is {ans}'.format(n = 3, ans = b.successor(3)))
    print('Smallest element is {n}'.format(n = b.min()))
    print('Largest element is {n}'.format(n = b.max()))

    b.printInOrder()
    pass

if __name__ == "__main__":
    main()
