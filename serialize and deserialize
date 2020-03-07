# Serializing and deserializing a given string.
def serialize(root):
    if root is None:
        return '#'
    return '{} {} {}'.format(root.val, serialize(root.left), serialize(root.right)) # .format is like a place holder which prints the value at that location.

def deserialize(data):
    def helper():
        val = next(vals) # next function takes an iterator as its arguement and gets the next value of the iterator
        if val == '#':
            return None
        node = Node(int(val))
        node.left = helper()
        node.right = helper()
        return node
    vals = iter(data.split()) # helps to create an iterator which iterates for each individual values. split function splits the long string with space or comma.
    return helper()
