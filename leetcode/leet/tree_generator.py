import random

class Node:
    def __init__(self, value=None):
        self.val = value
        self.left = None
        self.right = None

def generate_random_binary_tree(length=random.randint(0,100)):
    if length <= 0:
        return None
    node = Node(random.randint(1, 100))
    length -= 1
    if length == 0:
        return node
    if length == 1:
        node.left = generate_random_binary_tree(1)
        return node
    left_length = random.randint(1, length-1)
    node.left = generate_random_binary_tree(left_length)
    node.right = generate_random_binary_tree(length - left_length)
    return node
