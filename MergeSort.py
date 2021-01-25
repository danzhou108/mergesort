class MergeSort:
    def __init__(self):
        pass
    def merge(self,par1,par2,a): #merge two partitions in chronological order into parent node
        i = 0 #initialize counter of left child node
        j = 0 #initialize counter of right child node
        for k in range(len(a)): #loop through length of parent node
            if par1[i]<=par2[j]: #check if value of left child node is smaller than that of right child node
                a[k] = par1[i] #replace value in parent node with the value of left child node for current loop iteration
                if i<len(par1)-1: #if last element in left child node not reached, add one to counter
                    i += 1
                else:
                    par1[i] = float('inf') #if last element of left child node reached, replace value of last element with inf
            else:
                a[k] = par2[j] #replace value in parent node with the value of right child node for current loop iteration
                if j<len(par2)-1: #if last element in right child node not reached, add one to counter
                    j += 1
                else:
                    par2[j] = float('inf') #if last element of right child node reached, replace value of last element with inf
    def mergesort(self,a): #break main problem into subproblems; split an unsorted array into two partitions (child nodes) for sorting or further splitting
        if len(a)>1: #base condition; if array size of one element returned, stop recursing
            mid = len(a)//2 #take floor function for left child node
            par1 = a[0:mid] #fill left child node from 0 to floor function of parent node
            par2 = a[mid:] #fill right child node from floor function to last element of parent node
            self.mergesort(par1) #perform recursive function call on left child node splits until array size=1
            self.mergesort(par2) #perform recursive function call on right child node split
            self.merge(par1,par2,a) #pass left, right child nodes and parent node into merge function to sort elements in parent node in chronological order
        return a #return sorted array