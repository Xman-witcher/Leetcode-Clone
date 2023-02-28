def reverseList(head):
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