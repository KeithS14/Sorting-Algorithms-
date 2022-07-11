from random import *

def quickSort(mylist):
    start = 0
    n = len(mylist) -1
    shuffle (mylist)
    #print(mylist)
    return(_quickSort(mylist, start, n))

def _quickSort(mylist, start, end):
    pivot = start 
    l = pivot 
    r = end
    if  l >= r :
        return mylist
    while l < r:
        while mylist[l] < mylist[pivot]:
           l +=1
        while mylist[r] > mylist[pivot]:
            r -=1
        if l < r :
            mylist[l], mylist[r] = mylist[r], mylist[l]
            r -=1
    mylist[pivot], mylist[r] = mylist[r], mylist[pivot]
    _quickSort(mylist, pivot, r)
    _quickSort(mylist, pivot+1, end)  
    return mylist



if __name__ == "__main__":
   
    list_ = []
    for i in range(10):
        list_.append(randint(0, 1000))
    #list_ = [17, 15,31,12,467,69421,14.5,-69,44000000,3400.6]
    print("Original list: ", list_)
    mylist = quickSort(list_) 
    if sorted(mylist) == mylist:
        print ("list is sorted")
    else:
        print("list not sorted")
    print(mylist)