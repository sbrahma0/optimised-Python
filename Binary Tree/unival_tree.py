class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

node_right_left1 = Node(1, Node(1), Node(1))
node_right1 = Node(0, node_right_left1, Node(0))
tree1 = Node(0, Node(1), node_right1)
# tree1 looks like:
#         0
#        / \
#       1   0
#          / \
#         1   0
#        / \
#       1   1

# To print th4 tree in order
def in_order(root):
    if root.left:
        in_order(root.left)
    print(str(root.value) + ', ', end='')
    if root.right:
        in_order(root.right)

in_order(tree1)

def count_univals2(root):
    total_count, is_unival = helper(root)
    return total_count

# This function is the recursive function which does all the comparisons
def helper(root):
    if root is None:
        return 0, True

    left_count, is_left_unival = helper(root.left)
    right_count, is_right_unival = helper(root.right)

    is_unival = True
    if not is_left_unival or not is_right_unival:
        is_unival = False
    if root.left is not None and root.left.value != root.value:
        is_unival = False
    if root.right is not None and root.right.value != root.value:
        is_unival = False
    if is_unival:
        return left_count + right_count + 1, True
    else:
        return left_count + right_count, False

print(count_univals(tree1)) #should be 5
