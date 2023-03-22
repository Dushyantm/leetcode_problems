class Deque():
    
    def __init__(self):
        self.left = []
        self.right = []
        self.l = 0 #pointer
        self.n = 0 #number of elements
    
    def is_empty(self):
        n= len(self)
        if(n == 0):
          return True
        return False
    
    def appendleft(self, value):
        self[-1] = value
        self.l = self.l-1
        self.n = self.n + 1
    
    def append(self, value):
        self[self.n] = value
        self.n = self.n + 1 
    
    def popleft(self):
        x = self.first()
        self.l += 1
        self.n -= 1
        return x 
    
    def pop(self):
        x = self.last()
        self.l = 0 if len(self) == 1 else self.l
        self.n -= 1
        return x      
    
    def first(self):
        return self[0]
    
    def last(self):
        return self[self.n-1]
    
    def __str__(self):
        return f"Deque([{', '.join(str(self[i]) for i in range(len(self)))}])" 
    
    def __len__(self):
        return self.n
    
    def __getitem__(self, index):
        true_index = self.l + index
        if true_index < 0:
            true_index = -(true_index + 1)
            assert true_index < len(self.left)
            return self.left[true_index]
        else:
            if true_index < len(self.right):
                return self.right[true_index]
            else:
                assert False


    def __setitem__(self,index, value):
        assert (-1 <= index <= self.n)
        true_index = self.l + index
        target = self.left if true_index < 0 else self.right
        true_index = -(true_index + 1) if true_index < 0 else true_index
        if true_index < len(target):
            target[true_index] = value
        else:
            assert true_index == len(target)
            target.append(value)
            
            
class MyCircularQueue:

    def __init__(self,k): 
        #k is useless for our Deque. 
        # ONLY DATA STRUCTURE YOU CAN USE HERE IS ONLY Deque you WROTE
        #NOTHING CAN BE CHANJED HERE
        self._maxSize = k
        self._s = Deque()
        
    #############################
    # WRITE All public functions and private funcions BELOW
    #############################
    def enQueue(self, item):
        if self.isFull():
            return False
        self._s.append(item)
        return True 
    
    def deQueue(self):
        if(self.isEmpty()):
            return False
        self._s.popleft()
        return True

    def Front(self):
        if self.isEmpty():
            return -1
        return self._s.first()

    def Rear(self):
        if self.isEmpty():
            return -1
        return self._s.last()

    def isEmpty(self):
        return self._s.is_empty()

    def isFull(self):
        length = len(self)
        if(length >= self._maxSize):
            return True
        return False

    def __len__(self):
        return len(self._s)

   

    #############################
    # Overload print
    # NOTHING CAN BE CHANGED BELOW
    #############################
    def __str__(self)->'String':
        return ''+str(self._s)
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()