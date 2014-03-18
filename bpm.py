__author__ = 'Jay Zhai'

import json
from workflow import Node, Workflow

def convert_to_builtin_type(obj):
    #print 'default(', repr(obj), ')'
    d = {}
    d.update(obj.__dict__)
    return d

def from_node_to_json(node):
    return json.dumps(node, default=convert_to_builtin_type)

def from_workflow_to_json(workflow):
    return json.dumps(workflow, default=convert_to_builtin_type)



def from_json_to_node(_str):
    _d = json.loads(_str)
    n = Node(_d['name'])
    for (k,v) in _d.items():
        setattr(n, k, v)
    return n


