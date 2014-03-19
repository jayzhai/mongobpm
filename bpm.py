__author__ = 'Jay Zhai'

import json
from workflow import Node, Workflow

def convert_to_builtin_type(obj):
    #print 'default(', repr(obj), ')'
    d = {}
    for (k, v) in obj.__dict__.items():
        if isinstance(v, Node):
            d[k] = convert_to_builtin_type(v)
        else:
            d[k] = v
    return d

def from_node_to_json(node):
    return json.dumps(node, default=convert_to_builtin_type)


def from_workflow_to_json(workflow):
    return json.dumps(workflow, default=convert_to_builtin_type)


def from_json_to_workflow(_str):
    pass


def dict_to_object(_dic):
    pass


def from_json_to_node(_str):
    _d = json.loads(_str)
    n = Node(_d['name'])
    for (k, v) in _d.items():
        setattr(n, k, v)
    return n


