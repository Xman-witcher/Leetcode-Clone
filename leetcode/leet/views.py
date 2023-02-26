from django.shortcuts import render
from . import check_correct


def home(request):
    return render(request,'leet/home.html',{'yes':'hey'})
    

def question1(request):
    status={'message':'def find_frequency(arr,x):'}
   
    if request.method == 'POST':
        if 's2' in request.POST:
            with open('leet/q1.py', 'r') as file:
                file_contents = file.read()
            status={'message': file_contents}
        else:
            message = request.POST.get('1')
            status['message']=message
            from . import process
            lists=process.process(request)
            if lists[1]==0:
                status['yes']=lists[0]
            else:      
                from . import readme
                ans = check_correct.question_one(readme)
                if type(ans)!=dict:
                    status['yes']=ans
                else: 
                    status['Arr'] = ans['Arr']
                    status['x'] = ans['x']
                    status['ourans'] = ans['ourans']
                    status['ans'] = ans['ans']
    status['heading']='Question 1: Find frequency of a given number'
    status['image']=1
          
            
    return render(request, 'leet/questions.html', status)


def question2(request):
    status={'message':'def twosum(nums, target):'}
   
    if request.method == 'POST':
        if 's2' in request.POST:
            with open('leet/q2.py', 'r') as file:
                file_contents = file.read()
            status={'message': file_contents}
        else:
            message = request.POST.get('1')
            status['message']=message
            from . import process
            lists=process.process(request)
            if lists[1]==0:
                status['yes']=lists[0]
            else:      
                from . import readme
                ans = check_correct.question_two(readme)
                if type(ans)!=dict:
                    status['yes']=ans
                else: 
                    status['Arr'] = ans['Arr']
                    status['x'] = ans['x']
                    status['ourans'] = ans['ourans']
                    status['ans'] = ans['ans']

    status['heading']='Question 2: Two Sum'
    status['image']=2  
    return render(request, 'leet/questions.html', status)



def question3(request):
    status={'message':'def getinorder(root):'}
   
    if request.method == 'POST':
        if 's2' in request.POST:
            with open('leet/q3.py', 'r') as file:
                file_contents = file.read()
            status={'message': file_contents}
        else:
            message = request.POST.get('1')
            status['message']=message
            from . import process
            lists=process.process(request)
            if lists[1]==0:
                status['yes']=lists[0]
            else:
                from . import readme
                ans = check_correct.question_three(readme)
                if type(ans)!=dict:
                    status['yes']=ans
                else: 
                    status['Arr'] = ans['Arr']
                    status['ourans'] = ans['ourans']
                    status['ans'] = ans['ans']

    status['heading']='Question 3: Inorder Traversal of a Binary Tree'
    status['image']=3     
    return render(request, 'leet/questions.html', status)


def question4(request):
    status={'message':'def reverseList(head):'}
   
    if request.method == 'POST':
        if 's2' in request.POST:
            with open('leet/q4.py', 'r') as file:
                file_contents = file.read()
            status={'message': file_contents}
        else:
            message = request.POST.get('1')
            status['message']=message
            from . import process
            lists=process.process(request)
            if lists[1]==0:
                status['yes']=lists[0]
            else:      
                from . import readme
                ans = check_correct.question_four(readme)
                if type(ans)!=dict:
                    status['yes']=ans
                else: 
                    status['Arr'] = ans['Arr']
                    status['ourans'] = ans['ourans']
                    status['ans'] = ans['ans']
                
            
    status['heading']='Question 4: Reverse a LinkedList'
    status['image']=4    
    return render(request, 'leet/questions.html', status)


def question5(request):
    status={'message':'def shortestpath(graph, src):'}
   
    if request.method == 'POST':
        if 's2' in request.POST:
            with open('leet/q5.py', 'r') as file:
                file_contents = file.read()
            status={'message': file_contents}
        else:
            message = request.POST.get('1')
            status['message']=message
            from . import process
            lists=process.process(request)
            if lists[1]==0:
                status['yes']=lists[0]
            else:      
                from . import readme
                ans = check_correct.question_five(readme)
                if type(ans)!=dict:
                    status['yes']=ans
                else: 
                    status['Arr'] = ans['Arr']
                    status['ourans'] = ans['ourans']
                    status['ans'] = ans['ans']
    status['heading']='Question 5: Shortest Path from Source (Graph)'
    status['image']=5
    return render(request, 'leet/questions.html', status)
          

