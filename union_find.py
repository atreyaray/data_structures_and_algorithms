class unionFind :

    def __init__(self) :
        self.no_of_sets = 0
        self.parents = {}
        self.rank = {}

    def make_set(self,x) :
        if x not in self.parents :
            self.parents[x] = x
            self.no_of_sets += 1
            self.rank[x] = 0

    def find_set(self,x) :
        y = x
        while self.parents[y] != y :
            y = self.parents[y]
        return y

    def path_comp_find_set(self, x) :
        def find_and_compress(y) :
            if self.parents[y] == y :
                return y 
            else :
                r = find_and_compress(self.parents[y])
                self.parents[y] = r
                return r
        return find_and_compress(x)
    
    def union(self, x,y) :
        r_x = self.find_set(x)
        r_y = self.find_set(y)
        if r_x != r_y :
            self.parents[r_y] = r_x

    def balanced_union(self, x, y) :
        r_x = self.path_comp_find_set(x)
        r_y = self.path_comp_find_set(y)
        if r_x != r_y :
            if self.rank[r_x] > self.rank[r_y] :
                self.parents[r_y] = r_x
            else :
                self.parents[r_x] = r_y
                if self.rank[r_x] == self.rank[r_y] :
                    self.rank[r_y] += 1


def main() :
    u = unionFind()
    u.make_set(1)
    u.make_set(2)
    u.make_set(3)
    u.make_set(4)
    print('Input')
    # x = 1
    # print("root of ", x, 'is ', u.path_comp_find_set(x))
    # x = 2
    # print("root of ", x, 'is ', u.path_comp_find_set(x))
    # x = 3
    # print("root of ", x, 'is ', u.path_comp_find_set(x))
    # x = 4
    # print("root of ", x, 'is ', u.path_comp_find_set(x))
    x, y = 1, 2 
    u.balanced_union(x,y)
    x, y = 3, 4 
    u.balanced_union(x,y)
    print("Union 1")
    x = 1
    print("root of ", x, 'is ', u.path_comp_find_set(x))
    x = 2
    print("root of ", x, 'is ', u.path_comp_find_set(x))
    x = 3
    print("root of ", x, 'is ', u.path_comp_find_set(x))
    x = 4
    print("root of ", x, 'is ', u.path_comp_find_set(x))
    x, y = 2, 3
    u.balanced_union(x,y)
    print("Union 2")
    x = 1
    print("root of ", x, 'is ', u.path_comp_find_set(x))
    x = 2
    print("root of ", x, 'is ', u.path_comp_find_set(x))
    x = 3
    print("root of ", x, 'is ', u.path_comp_find_set(x))
    x = 4
    print("root of ", x, 'is ', u.path_comp_find_set(x))

    u.make_set(5)
    u.balanced_union(4,5)
    print("root of ", 5, 'is ', u.path_comp_find_set(x))
    

    print("hello")

if __name__ == "__main__":
    main()
