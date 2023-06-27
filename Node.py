

class Node:

    name = ''
    value = None

    def __init__(self, name, value):
        self.name = name
        self.value = value
        self.children = []

    def addChild(self, node):
        self.children.append(node)


