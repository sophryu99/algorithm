
class Tree:
    # initialize a list to append nodes
    def __init__(self):
        self.lst = [0]

   # sort nodes
    def sort(self, num):
        # while list has more than 2 elements
        if num >= 2:
            # if the parent node is larger than the child node
            if self.lst[num] < self.lst[num//2]:
                # swap places
                self.lst[num], self.lst[num//2] = self.lst[num//2], self.lst[num]
                # continue swapping
                self.sort(num//2)
    
    # append nodes to array and sort them
    def append(self, data):
        num = len(self.lst)
        self.lst.append(data)
        self.sort(num)

    def totalsum(self, node):
        if node <= 1 :
            return self.lst[node]
        else:
            return self.lst[node] + self.totalsum(node // 2)

    def result(self):
        last = len(self.lst) - 1
        # final result for the sum of parent node
        self.sum = 0
        # if there are parent nodes
        if last >= 2:
            return self.totalsum(last//2)
        else:
            return 0
        
T = int(input())

for tc in range(T):
    N = int(input())
    vals = list(map(int, input().split()))
    tree = Tree()
    for i in range(N):
        tree.append(vals[i])
    print("#{} {}".format(tc + 1, tree.result()))

    

