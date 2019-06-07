from __future__ import absolute_import

import unittest

import dynetx as dn


class DynDiGraphTestCase(unittest.TestCase):

    def test_nodes_with_data(self):
        g = dn.DynDiGraph()
        g.add_interaction(0, 1, 5)
        g.add_interaction(0, 2, 5)
        g.add_interaction(0, 3, 5)
        g.add_interaction(0, 4, 5)
        g._node[0]['key'] = 'val0'
        g._node[1]['key'] = 'val1'
        g._node[2]['key'] = 'val2'
        g._node[3]['key'] = 'val3'
        g._node[4]['key'] = 'val4'

        data = g.nodes(data=True)
        self.assertEqual(data,
                         [(0, {'key': 'val0'}),
                          (1, {'key': 'val1'}),
                          (2, {'key': 'val2'}),
                          (3, {'key': 'val3'}),
                          (4, {'key': 'val4'})
                          ])

    def test_time_slice_with_data(self):
        g = dn.DynDiGraph()
        g.add_interaction(0, 1, 5)
        g.add_interaction(0, 2, 5)
        g.add_interaction(0, 3, 5)
        g.add_interaction(0, 4, 5)
        g.add_interaction(4, 5, 6)
        g.add_interaction(4, 6, 6)
        g.add_interaction(4, 7, 6)
        g.add_interaction(4, 8, 6)
        g._node[0]['key'] = 'val0'
        g._node[1]['key'] = 'val1'
        g._node[2]['key'] = 'val2'
        g._node[3]['key'] = 'val3'
        g._node[4]['key'] = 'val4'
        g._node[5]['key'] = 'val5'

        h = g.time_slice(5)
        self.assertDictEqual(h._node,
                             {0: {'key': 'val0'},
                              1: {'key': 'val1'},
                              2: {'key': 'val2'},
                              3: {'key': 'val3'},
                              4: {'key': 'val4'}}
                             )

        h = g.time_slice(5, 6)
        self.assertDictEqual(h._node,
                             {0: {'key': 'val0'},
                              1: {'key': 'val1'},
                              2: {'key': 'val2'},
                              3: {'key': 'val3'},
                              4: {'key': 'val4'},
                              5: {'key': 'val5'},
                              6: {},
                              7: {},
                              8: {}}
                             )


if __name__ == '__main__':
    unittest.main()
