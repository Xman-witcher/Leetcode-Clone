def reverseList(head):

 error_message=None
 try:
  
          if not head:
  
              return
  
          if not head.next:
  
              return head
  
          temp=head.next
  
          head.next=None
  
          nexter=head
  
          while temp:
  
              head=temp
  
              temp=head.next
  
              head.next=nexter
  
              nexter=head
  
          return nexter  
 except Exception as e:
    error_message = str(e)
    return [error_message,"key"]