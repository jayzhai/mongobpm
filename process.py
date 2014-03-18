__author__ = 'Jay Zhai'

import json
from workflow import Node

def convert_to_builtin_type(obj):
    #print 'default(', repr(obj), ')' # 把MyObj对象转换成dict类型的对象
    d = {}
    d.update(obj.__dict__)
    return d

def from_node_to_json(node):
    return json.dumps(node, default=convert_to_builtin_type)


def from_json_to_node(_str):
    _d = json.loads(_str)
    n = Node(_d['name'])
    for (k,v) in _d.items():
        setattr(n, k, v)
    return n


