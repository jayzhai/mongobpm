__author__ = 'Jay Zhai'

import json
from workflow import Node, Workflow

def convert_to_repr_type(obj):
    #print 'default(', repr(obj), ')'
    d = {}
    for (k, v) in obj.__dict__.items():
        if isinstance(v, Node):
            d[k] = convert_to_repr_type(v)
        else:
            d[k] = v
    return d

def from_node_to_json(node):
    return json.dumps(node, default=convert_to_repr_type)


def from_workflow_to_json(workflow):
    return json.dumps(workflow, default=convert_to_repr_type)


def from_json_to_workflow(_str):
    _d = json.loads(_str)
    wf = Workflow(_d['name'], _d['instanceid'], _d['version'])
    for (k, v) in _d.items():
        if k == 'node_dict':
            nd = {}
            for (a, b) in v.items():
                n = Node(b['name'])
                n.__dict__.update(b)
                nd[a] = n
            setattr(wf, k, nd)
        else:
            setattr(wf, k, v)
    return wf

# def dict_to_node(d):
#     top = type('new', (object,), d)
#     seqs = tuple, list, set, frozenset
#     for i, j in d.items():
#         if isinstance(j, dict):
#             setattr(top, i, dict_to_node(j))
#         elif isinstance(j, seqs):
#             setattr(top, i,
#                 type(j)(dict_to_node(sj) if isinstance(sj, dict) else sj for sj in j))
#         else:
#             setattr(top, i, j)
#     return top


def from_json_to_node(_str):
    _d = json.loads(_str)
    n = Node(_d['name'])
    for (k, v) in _d.items():
        if k == 'transit_dict':
            td = {}
            for (a, b) in v.items():
                td[a] = b;
            setattr(n, k, td)
        else:
            setattr(n, k, v)
    return n


if __name__ == '__main__':
    n1 = Node('n1')
    n2 = Node('n2')
    n1.transit(n2)
    wf = Workflow('test')
    wf.add_node(n1, True)
    wf.add_node(n2)
    js1  = from_workflow_to_json(wf)
    print js1
    w2 = from_json_to_workflow(js1)
    print repr(w2)
    js2 =  from_workflow_to_json(w2)
    print js2