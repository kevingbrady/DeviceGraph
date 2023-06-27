

class Node:

    def __init__(self, name, value):
        self.name = name
        self.value = value
        self.children = []

    def addChild(self, node):
        self.children.append(node)

    def node_string_repr(self):

        if not self.children:
         nodeString = f'{self.name}: {self.value}'

        else:
            nodeString = f'{self.name}: ['
            for i, child in enumerate(self.children):
                nodeString += repr(child)
                if i < len(self.children) - 1:
                    nodeString += ', '

            nodeString += ']'

        return nodeString

    def __repr__(self):

        return f'{self.name}:{self.value}'
