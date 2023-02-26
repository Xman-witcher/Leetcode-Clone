def process(request):

        message = request.POST.get('1')
        with open('leet/readme.py', 'w') as f:
            f.write(message)
        
        def check_file_syntax(filename):
            try:
                exec(open(filename).read(), {'__file__': filename})
                return True
            except SyntaxError:
                return 0
    
            except Exception:
                return 5
        yes=1
        for i in message:
            if i!=' ':
                yes=0
                break
                
        if check_file_syntax('leet/readme.py') in [0,5] or yes==1:
            if yes==1:
                ans='Am I supposed to check your blank code? Write some code'
            else:
                ans= 'SyntaxError. Please check your code'
                
            return [ans,0]


        with open('leet/readme.py', 'r') as file:
            lines = file.readlines()

        with open('leet/readme.py', 'w') as file:
            count=0
            for line in lines:
                
                if count==0:
                    file.write(line+'\n')
                    file.write(' error_message=None\n')
                    file.write(' try:\n')
                    count+=1
                else:
                    file.write('  '+line)
 
            file.write('\n')
            file.write(' except Exception as e:\n')
            file.write('    error_message = str(e)\n')
            file.write('    return [error_message,"key"]')     
            
        return [1,1]
        

                