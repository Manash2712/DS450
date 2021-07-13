def kthSmallest(self,arr, l, r, k):
        '''
        arr : given array
        l : starting index of the array i.e 0
        r : ending index of the array i.e size-1
        k : find kth smallest element and return using this function
        '''
        heapq.heapify(arr)
        a = heapq.nsmallest(k,arr)
        return(a[-1])
        '''for i in range(k-1):
            arr.remove(min(arr))
        return (min(arr))'''
