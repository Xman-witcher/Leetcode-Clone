
from . import q1, q2, q3, q4, q5
from . import tree_generator
from . import getlinkedlist
from . import linkedlist_generator
from . import generate_graph

def question_one(message):
    try:
        namespace = {}
        exec(message,namespace)
        a = eval('find_frequency',namespace)
        arr=[1,2,2,3,3,4,3,5,6,3,0,3,3,3,3,3]
        x=3
        a(arr,x)           
             
    except Exception as e:
            
        if str(e)=="name 'find_frequency' is not defined":
                  e='Did you just Nuke the given Function "Find Frequency()"?'
        else:             
            message2='def find_frequency(arr,x):' 
            
            if len(message)>=len(message2):
                 if message[0:26]==message2:
                        
                        message = "".join(message.split())
                        message2 =  'deffind_frequency(arr,x):' 
                        if message==message2:              
                            e='Am I supposed to check your blank code? Write some code'
                             
        return [e]

    testcases=[ ([1,2,2,3,4,5,3,2],2),
            ([32,11,14,21,15,11,41,11,11,11,11,11],11),
            ([1,2,3,3,4,6,7],5),
            ([1,2,3,4,5,6,7,8,9],4),
            ([1,2,3,4,4,5,7,7,7,7,8,7,9,10],7)]
    
    for i in testcases:
        arr,x = i
        ans=a(arr,x) 
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


def question_two(message):

    try:
        namespace = {}
        exec(message,namespace)
        a = eval('twosum',namespace)
        arr=[2,7,11,15]
        x=9
        a(arr,x)           
             
    except Exception as e:
 
        if str(e)=="name 'twosum' is not defined":       
            e='Did you just Nuke the given Function "twosum()"?'
                
        else:             
            message2='def twosum(nums, target):' 
            
            if len(message)>=len(message2):
                 if message[0:25]==message2:                     
                        message = "".join(message.split())
                        message2 =  'deftwosum(nums,target):' 
                        if message==message2:              
                            e='Am I supposed to check your blank code? Write some code'
                             
        return [e]

    testcases=[ ([2,5,3,44,7,1,33],9), 
                ([3,3],6),
                ([3,5,1,45,3,7,-27,-18,4],18),
                ([11,4,55,12,-7,18,39,4],32),
                ([14,25,42,76,24,50],100),
                ([-14,22,91,64,32,63,1,41],63) ]

    for i in testcases:
        nums,target = i
        ans=a(nums,target)    
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

def question_three(message):


    try:
        namespace = {}
        exec(message,namespace)
        a = eval('getinorder',namespace)
        tree=tree_generator.generate_random_binary_tree(4)
        a(tree)           
            
    except Exception as e:
        
        if str(e)=="name 'getinorder' is not defined":         
            e='Did you just Nuke the given Function "getinorder()"?'
                
        else:             
            message2='def getinorder(root):' 
            new='def getinorder(root,result=None):'
            
            if len(message)>=len(message2): 
                if message[0:21]==message2  or message[0:33]==new:                           
                        message = "".join(message.split())
                        message2 =  'defgetinorder(root):' 
                        if message==message2:              
                            e='Am I supposed to check your blank code? Write some code'
                        else:
                            message2='defgetinorder(root,result=None):'          
                            if message==message2:              
                                e='Am I supposed to check your blank code? Write some code'                          
        return [e]

    testcases=[]
    for i in range(50):
        testcases.append(tree_generator.generate_random_binary_tree())
    for i in testcases:
        ourans= q3.getinorder(i)   
        ans=  a(i)
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


def question_four(message):
    try:
        namespace = {}
        exec(message,namespace)
        a = eval('reverseList',namespace)
        ll=linkedlist_generator.generate_random_linked_list(4)
        a(ll)           
             
    except Exception as e:
            
        if str(e)=="name 'reverseList' is not defined":
            e='Did you just Nuke the given Function "reverseList()"?'
                
        else:             
            message2='def reverseList(head):' 
            
            if len(message)>=len(message2):
                 if message[0:22]==message2:                     
                        message = "".join(message.split())
                        message2 =  'defreverseList(head):' 
                        if message==message2:              
                            e='Am I supposed to check your blank code? Write some code'
                             
        return [e]

    testcases=[]
    
    for i in range(50):
        testcases.append(linkedlist_generator.generate_random_linked_list())
    for i in testcases:
        result= getlinkedlist.get(i)
        ourans = q4.reverseList(i)
        i=q4.reverseList(ourans)

        ans = a(i)       
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

def question_five(message):
    try:
        namespace = {}
        exec(message,namespace)
        a = eval('shortestpath',namespace)
        graph =  generate_graph.Graph(4)
        graph.generate_random_graph()   
        a(graph.graph,0)           
             
    except Exception as e:
            
        if str(e)=="name 'shortestpath' is not defined":
            e='Did you just Nuke the given Function "shortestpath()"?'
                
        else:             
            message2='def shortestpath(graph, src):' 
            
            if len(message)>=len(message2):
                 if message[0:29]==message2:                     
                        message = "".join(message.split())
                        message2 =  'defshortestpath(graph,src):' 
                        if message==message2:              
                            e='Am I supposed to check your blank code? Write some code'
                             
        return [e]

    testcases=[]
    
    import random
    
    for i in range(50):
        graph =  generate_graph.Graph(random.randint(1,9))
        graph.generate_random_graph()
        testcases.append(graph)
    for i in testcases:
        src= random.randint(0,len(i.graph)-1)  
        ourans = q5.shortestpath(i.graph,src)

        ans=a(i.graph,src)
       
        if ourans!=ans:
            arr='Input: ' + str(i.graph)
            ourans = 'Expected output: '+ str(ourans)
            ans = 'Your output: '+ str(ans)
            dicts= {'Arr':arr, 'ourans': ourans, 'ans': ans}
            return dicts
    return 'Accepted'




    


