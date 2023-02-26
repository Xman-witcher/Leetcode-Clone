
from . import q1, q2, q3, q4, q5

def question_one(file):
    testcases=[ ([1,2,2,3,4,5,3,2],2),
            ([32,11,14,21,15,11,41,11,11,11,11,11],11),
            ([1,2,3,3,4,6,7],5),
            ([1,2,3,4,5,6,7,8,9],4),
            ([1,2,3,4,4,5,7,7,7,7,8,7,9,10],7)]
    
    for i in testcases:
        arr,x = i

        try:
            ans=file.find_frequency(arr,x)
        except Exception as e:
            error_message = str(e)
            return error_message

        if type(ans)==list and ans[-1]=='key':
            return ans[0]
        
        ourans= q1.find_frequency(arr,x)
        if ourans!=ans:
            arr='Arr: ' + str(arr)
            x=  'x: '+ str(x)
            ourans = 'Expected output: '+ str(ourans)
            ans = 'Your output: '+ str(ans)
            dicts= {'Arr':arr, 'x':x, 'ourans': ourans, 'ans': ans}
            return dicts
    return 'Accepted'


    
###################################################################

def question_two(file):
    testcases=[ ([2,5,3,44,7,1,33],9), 
                ([3,3],6),
                ([3,5,1,45,3,7,-27,-18,4],18),
                ([11,4,55,12,-7,18,39,4],32),
                ([14,25,42,76,24,50],100),
                ([-14,22,91,64,32,63,1,41],63) ]

    for i in testcases:
        nums,target = i
        try:
            ans=file.twosum(nums,target)
        except Exception as e:
            error_message = str(e)
            return error_message

    
        if type(ans)==list and ans[-1]=='key':
            return ans[0]
        
        ourans= q2.twosum(nums,target)
        another=[ourans[1],ourans[0]]
        if ourans!=ans and another!=ans:
            arr='Nums: ' + str(nums)
            x=  'target: '+ str(target)
            ourans = 'Expected output: '+ str(ourans)
            ans = 'Your output: '+ str(ans)


            dicts= {'Arr':arr, 'x':x, 'ourans': ourans, 'ans': ans}
            return dicts
    return 'Accepted'

############################################################

def question_three(file):
    testcases=[]
    from . import tree_generator
    for i in range(50):
        testcases.append(tree_generator.generate_random_binary_tree())
    for i in testcases:
        ourans= q3.getinorder(i)


        try:
            ans=  file.getinorder(i)
        except Exception as e:
            error_message = str(e)
            return error_message

        if type(ans)==list and ans[-1]=='key':
            return ans[0]
        
        if ourans!=ans:
            from . import getlevelorder
            result=getlevelorder.get(i)
            arr='Input: root = ' + str(result) + '  (level-order)'
            ourans = 'Expected output: '+ str(ourans)
            ans = 'Your output: '+ str(ans)
            dicts= {'Arr':arr, 'ourans': ourans, 'ans': ans}
            return dicts
    return 'Accepted'


###################################################################################



def question_four(file):
    testcases=[]
    from . import linkedlist_generator
    for i in range(50):
        testcases.append(linkedlist_generator.generate_random_linked_list())
    for i in testcases:
        from . import getlinkedlist
        result= getlinkedlist.get(i)
        ourans = q4.reverseList(i)
        i=q4.reverseList(ourans)

        try:
            ans = file.reverseList(i)
        except Exception as e:
            error_message = str(e)
            return error_message

        if type(ans)==list and ans[-1]=='key':
            return ans[0]
        
        stat=True
        while ourans!=None and ans!=None:
            if type(ourans)!=type(ans) or ourans.value!=ans.value:
                stat=False
                break
            ourans=ourans.next
            ans= ans.next
        if stat==False or ourans or ans:
            arr='Input: Head = ' + str(result)
            if type(ourans)==type(ans):
                ans= getlinkedlist.get(ans)
                
            ourans= getlinkedlist.get(ourans)
            ourans = 'Expected output: '+ str(ourans)
            ans = 'Your output: '+ str(ans)
              
            dicts= {'Arr':arr, 'ourans': ourans, 'ans': ans}
            return dicts
    return 'Accepted'

##########################################################################################

def question_five(file):
    testcases=[]
    from . import generate_graph
    import random
    
    for i in range(50):
        graph =  generate_graph.Graph(random.randint(1,9))
        graph.generate_random_graph()
        testcases.append(graph)
    for i in testcases:
        src= random.randint(0,len(i.graph)-1)  
        ourans = q5.shortestpath(i.graph,src)

        try:
            ans=file.shortestpath(i.graph,src)
        except Exception as e:
            error_message = str(e)
            return error_message

        if type(ans)==list and ans[-1]=='key':
            return ans[0]
        
        if ourans!=ans:
            arr='Input: ' + str(i.graph)
            ourans = 'Expected output: '+ str(ourans)
            ans = 'Your output: '+ str(ans)
            dicts= {'Arr':arr, 'ourans': ourans, 'ans': ans}
            return dicts
    return 'Accepted'




    


