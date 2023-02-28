from django.shortcuts import render
from . import check_correct
import os


def home(request):
    return render(request,'leet/home.html',{'yes':'hey'})
    

def question1(request):
    status={'message':'def find_frequency(arr,x):'}
   
    if request.method == 'POST':
        if 's2' in request.POST:
            script_path = os.path.abspath(__file__)
            file_path = os.path.join(os.path.dirname(script_path), 'q1.py')
            with open(file_path, 'r') as file:        
                file_contents = file.read()
            status={'message': file_contents}
        else:
            message = request.POST.get('1')
            status['message']=message
            
            ans=check_correct.question_one(message)
            if type(ans)==list:
                status['yes']=ans[0]

            else:            
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
            script_path = os.path.abspath(__file__)
            file_path = os.path.join(os.path.dirname(script_path), 'q2.py')
            with open(file_path, 'r') as file:
                file_contents = file.read()
            status={'message': file_contents}
        else:
            message = request.POST.get('1')
            status['message']=message

            ans=check_correct.question_two(message)
            if type(ans)==list:
                status['yes']=ans[0]
            else:      
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
            script_path = os.path.abspath(__file__)
            file_path = os.path.join(os.path.dirname(script_path), 'q3.py')
            with open(file_path, 'r') as file:
                file_contents = file.read()
            status={'message': file_contents}
        else:
            message = request.POST.get('1')
            status['message']=message
            
            ans=check_correct.question_three(message)
            if type(ans)==list:
                status['yes']=ans[0]
            else:
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
            script_path = os.path.abspath(__file__)
            file_path = os.path.join(os.path.dirname(script_path), 'q4.py')
            with open(file_path, 'r') as file:
                file_contents = file.read()
            status={'message': file_contents}
        else:
            message = request.POST.get('1')
            status['message']=message

            ans=check_correct.question_four(message)
            if type(ans)==list:
                status['yes']=ans[0]
            else:      
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
            script_path = os.path.abspath(__file__)
            file_path = os.path.join(os.path.dirname(script_path), 'q5.py')
            with open(file_path, 'r') as file:
                file_contents = file.read()
            status={'message': file_contents}
        else:
            message = request.POST.get('1')
            status['message']=message

            ans=check_correct.question_five(message)
            if type(ans)==list:
                status['yes']=ans[0]
            else:      
                if type(ans)!=dict:
                    status['yes']=ans
                else: 
                    status['Arr'] = ans['Arr']
                    status['ourans'] = ans['ourans']
                    status['ans'] = ans['ans']
    status['heading']='Question 5: Shortest Path from Source (Graph)'
    status['image']=5
    return render(request, 'leet/questions.html', status)
          

