class Search:
    
    def __init__(self,array,number):
        self.lst = sorted(array)
        self.number = number
    def binary_search(self,lst,n,start = 0,end = -1):
        mid = lst[end] // 2
        if start - end == 0:
            return 'Element not in the list'
        if mid == n:
            return f'Position : {mid-1}'
        elif mid > n:
            binary_search(lst,n,start = start,end = end - 1)
        elif mid < n:
            binary_search(lst,n,start = start + 1, end = end)
            
    
    def linear_search(self,lst,n):
        for i in range(len(lst)):
            if lst[i] == n:
                return f'Position :{i}'
        return -1
    
    def run_search(self):
        while True:
            print('Select the searching algorithm:')
            print('1. Linear Search.')
            print('2. Binary Search.')
            print('3. quit.')
            opt = int(input('Option: '))
            if opt == 2:
                print(search.binary_search(self.lst,self.number))
            elif opt == 1:
                print(search.linear_search(self.lst,self.number))
            elif opt == 3:
            	break
        

lst = [1,2,3,4,5,6,7,8]
number = 4
search = Search(lst,number)
search.run_search()    
