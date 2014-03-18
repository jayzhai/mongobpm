__author__ = 'Jay Zhai'


class Workflow:
    'A workflow definition'

    def __init__(self, name, instanceid='0', version=0):
        self.instanceid = instanceid
        self.name = name
        self.version = version
        self.root_node = Node('_ROOTNODE')
        self.node_dict = {'_ROOTNDE': self.root_node}
        self.pointer = '_ROOTNODE'

    def find_node(self, name):
        return self.node_dict[name]

    def add_node(self, node):
        self.node_dict[node.name] = node

    def delete_node(self, node_name):
        return self.node_dict.pop(node_name)

    def flow_to(self, node_name):
        #TODO
        pass



class Node:
    'Node in a process'

    def __init__(self, name):
        self.name = name
        self.transit_dict = {}


    def transit(self,  target_node, transit_tag='DEFAULT'):
        self.transit_dict[transit_tag] = target_node