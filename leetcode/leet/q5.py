def shortestpath(graph, src):
       
        def insert(heap,tup):
            heap.append(tup)
            current=len(heap)-1
            parent=(current-1)//2
            while current!=0 and heap[parent][0]>heap[current][0]:
                heap[current],heap[parent]=heap[parent],heap[current]
                current=parent
                parent=(current-1)//2
        
        def heapify(heap):
            parent=0
            left=1
            right=2
            while left<len(heap):
                if right<len(heap):
                    left=left if heap[left][0]<=heap[right][0] else right
                if heap[left]>=heap[parent]:
                    return
                heap[left],heap[parent]=heap[parent],heap[left]
                parent=left
                left=(parent*2)+1
                right=(parent*2)+2
                      
        def extract(heap):
            if len(heap)==1:
                return heap.pop()
            node=heap[0]
            heap[0]=heap.pop()
            heapify(heap)
            return node
           
        
        V=len(graph)
        distance=[float('inf')]*V
        distance[src]=0
        heap=[]
        insert(heap,(0,src))
        while heap!=[]:
            node=extract(heap)
            if node[0]==distance[node[1]]:
                for i in graph[node[1]]:
                    if (distance[node[1]]+i[1])<distance[i[0]]:
                        distance[i[0]]=(distance[node[1]]+i[1])
                        insert(heap,(distance[i[0]],i[0]))
        return distance