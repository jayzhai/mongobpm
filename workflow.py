__author__ = 'Jay Zhai'


class Workflow:
    'A workflow definition'

    def __init__(self, name, instanceid='0', version=0):
        self.instanceid = instanceid
        self.name = name
        self.version = version
        self.root_node = ''
        self.pointer = ''
        self.node_dict = {}

    def find_node(self, name):
        return self.node_dict[name]

    def add_node(self, node, root_node=False):
        self.node_dict[node.name] = node
        if root_node:
            self.root_node = node.name

    def delete_node(self, node_name):
        return self.node_dict.pop(node_name)

    def jump_to(self, node_name):
        #TODO
        pass



class Node:
    'Node in a process'

    def __init__(self, name):
        self.name = name
        self.transit_dict = {}


    def transit(self,  target_node, transit_tag='DEFAULT'):
        self.transit_dict[transit_tag] = target_node.name


class Traveler:
    'Like signal in other bpm system'

    def __init__(self, id):
        self.id = id
        self.parent = ''
        self.workflow_name = ''
        self.workflow_version = 0
        self.node = ''

