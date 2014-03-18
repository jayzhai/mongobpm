__author__ = 'Jay Zhai'


class WorkflowDef:
    'A workflow definition'

    def __init__(self, name, version=0):
        self.name = name
        self.version = version





class Node:
    'Node in a process'

    def __init__(self, name):
        self.name = name