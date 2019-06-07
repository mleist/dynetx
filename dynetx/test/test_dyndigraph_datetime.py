from __future__ import absolute_import

import unittest
import uuid
from datetime import datetime

import dynetx as dn

def from_iso(inp_string):
    return datetime.strptime(inp_string,
                             "%Y-%m-%dT%H:%M:%S")

class DynDiGraphTestCase(unittest.TestCase):
    maxDiff = None

    node0uuid = str(uuid.uuid5(uuid.NAMESPACE_OID, 'node0'))
    node1uuid = str(uuid.uuid5(uuid.NAMESPACE_OID, 'node1'))
    node2uuid = str(uuid.uuid5(uuid.NAMESPACE_OID, 'node2'))
    node3uuid = str(uuid.uuid5(uuid.NAMESPACE_OID, 'node3'))
    node4uuid = str(uuid.uuid5(uuid.NAMESPACE_OID, 'node4'))
    node5uuid = str(uuid.uuid5(uuid.NAMESPACE_OID, 'node5'))
    t0 = from_iso("2019-06-05T10:10:00")
    t1 = from_iso("2019-06-05T11:10:00")
    t2 = from_iso("2019-06-05T12:10:00")
    t3 = from_iso("2019-06-05T13:10:00")
    t4 = from_iso("2019-06-05T14:10:00")
    t5 = from_iso("2019-06-05T15:10:00")
    t0ts = int(t0.timestamp())
    t1ts = int(t1.timestamp())
    t2ts = int(t2.timestamp())
    t3ts = int(t3.timestamp())
    t4ts = int(t4.timestamp())
    t5ts = int(t5.timestamp())

    def test_nodes_with_data(self):
        g = dn.DynDiGraph()
        g.add_node(self.node4uuid, test_param='test_val_4')
        g.add_node(self.node1uuid, test_param='test_val_1')
        g.add_node(self.node3uuid, test_param='test_val_3')
        g.add_node(self.node5uuid, test_param='test_val_5')
        g.add_node(self.node2uuid, test_param='test_val_2')
        g.add_interaction(u=self.node0uuid, v=self.node1uuid, t=self.t5ts)
        g.add_interaction(u=self.node0uuid, v=self.node2uuid, t=self.t5ts)
        g.add_interaction(u=self.node0uuid, v=self.node3uuid, t=self.t5ts)
        g.add_interaction(u=self.node0uuid, v=self.node4uuid, t=self.t5ts)
        data = g.nodes(data=True)
        self.assertEqual(data,
                         [(self.node4uuid, {'test_param': 'test_val_4'}),
                          (self.node1uuid, {'test_param': 'test_val_1'}),
                          (self.node3uuid, {'test_param': 'test_val_3'}),
                          (self.node5uuid, {'test_param': 'test_val_5'}),
                          (self.node2uuid, {'test_param': 'test_val_2'}),
                          (self.node0uuid, {})
                          ]
                         )


if __name__ == '__main__':
    unittest.main()
