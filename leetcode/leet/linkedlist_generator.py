import random

class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

def generate_random_linked_list(size=random.randint(1,100)):
    head = Node(random.randint(1, 100))
    current = head
    for _ in range(1, size):
        current.next = Node(random.randint(1, 100))
        current = current.next
    return head