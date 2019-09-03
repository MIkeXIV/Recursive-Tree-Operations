

class Node():

    def __init__(self, value, left, right):

        self.value = value
        self.left = left
        self.right = right
        


def recursive_add_sub_nodes(node):
    if node == None:
        print('i ran')
        return 0
    print(node.value)
    return node.value + recursive_add_sub_nodes(node.left) + recursive_add_sub_nodes(node.right)


one = Node(1, None, None)
four = Node(4, None, None)
two = Node(2, one, four)
eleven = Node(11, None, None)
nine = Node(9, None, eleven)
five = Node(5, two, nine)

x = recursive_add_sub_nodes(five)
print(x)


'''

                        5
                       / \
                      2   9
                     /  \   \
                    1    4   11

'''
