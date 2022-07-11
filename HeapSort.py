from random import *


class PQBinaryHeap:
    """ Maintain an collection of items, popping by lowest key.

        This implementation maintains the collection using a binary heap.
    """
    class Element:
        """ An element with a key and value. """
        
        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __eq__(self, other):
            """ Return True if this key equals the other key. """
            return self._key == other._key

        def __lt__(self, other):
            """ Return True if this key is less than the other key. """
            return self._key < other._key

        def __gt__(self, other):
            """ Return True if this key is greater than the other key. """
            return self._key > other._key
        
        def __le__(self, other):
            """ Return True if this key is less than or equal to the other key. """
            return self._key >= other._key

        def __ge__(self, other):
            """ Return True if this key is greater than or equal to the other key. """
            return self._key >= other._key

        

    ########## End of element class #########
    
    def __init__(self):
        """ Create a PQ with no elements. """
        self._heap = []
        self._size = 0
        
    def __str__(self):
        """ Return a breadth-first string of the values. """

        # method body goes here
        rtn_str = ""
        for elt in self._heap:
            rtn_str += "(%s, %s) "% (elt._key,elt._value)
        return rtn_str

    

    def max(self):
        """ Return the max priority key,value. """
        if self._size > 0:
            return "Key: %s, Value: %s" %(self._heap[0]._key, self._heap[0]._value ) 

    def add(self, key, value):
        """ Add Element(key,value) to the heap. """
       
        self._heap.append(self.Element(key, value))
        if self._size > 0:
            self._upheap(self._size)
        self._size +=1 
        
    def remove_max(self):
        """ Remove and return the max priority key,value. """
        max = self.max()
        if self._size > 0:
            self._heap[0] = self._heap[-1]
            #self._heap[-1]._wipe
            #print(self._printstructure())
            self._heap.pop(-1)
            self._downheap(0,self._size)
        self._size -= 1
        return max

    def length(self):
        """ Return the number of items in the heap. """
        # method body goes here
        return self._size

   

    def _upheap(self, posn):
        """ Bubble the item in posn in the heap up to its correct place. """
       
        if posn != 0:  
            parent = self._parent(posn)
            if self._heap[posn] > self._heap[parent]:
                self._swap(posn, parent)
                self._upheap(parent)

    def _downheap(self, posn, end):
        """ Bubble the item in posn in the heap down to its correct place. """
        left = self._left(posn)
        right = self._right(posn)
        if left is not None or right is not None:
            if left == None:
                child = right
            elif right == None:
                child = left
            else:
                if self._heap[left] >= self._heap[right]:
                    child = left
                else:
                    child = right
            if self._heap[posn] < self._heap[child] and child <= end :
                self._swap(posn, child)
                self._downheap(child, end)

    def _parent(self, posn):
        """ Return the index of the parent of elt at index posn. """
        index = (posn-1)//2
        if posn > 0:
            return index
        

    def _left(self, posn):
        """ Return the index of the left child of elt at index posn. """
        index = posn *2 +1
        if self._size-1 > index:
            #if self._heap[index] is not None:
            return index 
        else:
            return None

    def _right(self, posn):
        """ Return the index of the right child of elt at index posn. """
        index = posn *2 + 2
        if self._size-1 > index:
            #if self._heap[index] is not None:
            return index 
        else:
            return None

    def _swap(self, posn1, posn2):
        """ Swaps posn1 and posn2 """
        temp = self._heap[posn1]
        self._heap[posn1] = self._heap[posn2]
        self._heap[posn2] = temp
        #print("~~~~~~~~~~~~~~~~~")
       #print(self._heap[posn2]._key," swaps with ",self._heap[posn1]._key)



    def _inPlaceHeapSort(self):
        last = len(self._heap) -1
        while last > 0:
            # remove max from heap 
            max = self._heap[0]
            #self._heap[0] = None
            # copy last item up and bubble down
            self._heap[0] = self._heap[last]
            self._downheap(0,last)
            # reinsert max into free place 
            self._heap[last] = max
            last -=1
            print(self._printstructure())

        return self._heap


    def _printstructure(self):
        """ Print out the elements one to a line. """
        rtn_str = ""
        for elt in self._heap:
            rtn_str += "(%s, %s) "% (elt._key,elt._value)
        return rtn_str



    def _myTestAdd():
        pq = PQBinaryHeap()
        alpha = ["F","E","D","C","B","A"]
        size = len(alpha)
        for i in range(size):
            integer = int(input("Enter integer: "))
            pq.add(integer, alpha[-1])
            alpha.pop(-1)
        #pq._printstructure()
        print("Remove max:")
        pq.remove_max()
        #pq._printstructure()
        print(pq)

    
    def _testHeapSortInput():
        pq = PQBinaryHeap()
        alpha = ["F","E","D","C","B","A"]
         
        for i in range(len(alpha)):
            integer = int(input("Enter integer: "))
            pq.add(integer, alpha[-1])
            alpha.pop(-1)
        print("After max heap:")
        print(pq)
        #pq._inPlaceHeapSort()
        pq._inPlaceHeapSort()

        print("After heap sort:")
        print(pq)


    
def heapSort(inList):
    pq = PQBinaryHeap()
    for i in inList:
        pq.add(i,"value")
    #return
    print("After max heap:")
    print(pq)
    inList = pq._inPlaceHeapSort()
    print("After heap sort:")
    print(pq)
    return inList




if __name__ == "__main__":
    mylist = []
    for i in range(4):
        mylist.append(randint(0, 9))
    heapSort(mylist)  


    heapSort([2,56,27,8,1,56,23,86,97,12,0,11,556,23,1])
    #heapSort([1,5,9,2,5,0,6])  

    
    
