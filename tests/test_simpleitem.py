import unittest

from simpleitem import SimpleItem


class SimpleItemTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.item1 = SimpleItem()
        self.item1.node1 = 1
        self.item1.node2.node3 = 3

        self.item2 = SimpleItem()
        self.item2['node1'] = 1
        self.item2['node2']['node3'] = 3

        self.item3 = SimpleItem(node1=1, node2={'node3': 3})

        self.item4 = SimpleItem(**{'node1': 1, 'node2': {'node3': 3}})

        self.item5 = SimpleItem()
        self.item5(node1=1, node2={'node3': 3})

        self.item6 = SimpleItem()
        self.item6(**{'node1': 1, 'node2': {'node3': 3}})

        self.item7 = SimpleItem()
        self.item7.from_yaml('test_files/test.yaml')

    def test_getitem(self):
        self.assertEqual(self.item1['node1'], 1)
        self.assertEqual(self.item1['node2']['node3'], 3)
        self.assertIsInstance(self.item1['node2'], SimpleItem)

        self.assertEqual(self.item2['node1'], 1)
        self.assertEqual(self.item2['node2']['node3'], 3)
        self.assertIsInstance(self.item2['node2'], SimpleItem)

        self.assertEqual(self.item3['node1'], 1)
        self.assertEqual(self.item3['node2']['node3'], 3)
        self.assertIsInstance(self.item3['node2'], SimpleItem)

        self.assertEqual(self.item4['node1'], 1)
        self.assertEqual(self.item4['node2']['node3'], 3)
        self.assertIsInstance(self.item4['node2'], SimpleItem)

        self.assertEqual(self.item5['node1'], 1)
        self.assertEqual(self.item5['node2']['node3'], 3)
        self.assertIsInstance(self.item5['node2'], SimpleItem)

        self.assertEqual(self.item6['node1'], 1)
        self.assertEqual(self.item6['node2']['node3'], 3)
        self.assertIsInstance(self.item6['node2'], SimpleItem)

    def test_getattr(self):
        self.assertEqual(self.item1.node1, 1)
        self.assertEqual(self.item1.node2.node3, 3)
        self.assertIsInstance(self.item1.node2, SimpleItem)

        self.assertEqual(self.item2.node1, 1)
        self.assertEqual(self.item2.node2.node3, 3)
        self.assertIsInstance(self.item2.node2, SimpleItem)

        self.assertEqual(self.item3.node1, 1)
        self.assertEqual(self.item3.node2.node3, 3)
        self.assertIsInstance(self.item3.node2, SimpleItem)

        self.assertEqual(self.item4.node1, 1)
        self.assertEqual(self.item4.node2.node3, 3)
        self.assertIsInstance(self.item4.node2, SimpleItem)

        self.assertEqual(self.item5.node1, 1)
        self.assertEqual(self.item5.node2.node3, 3)
        self.assertIsInstance(self.item5.node2, SimpleItem)

        self.assertEqual(self.item6.node1, 1)
        self.assertEqual(self.item6.node2.node3, 3)
        self.assertIsInstance(self.item6.node2, SimpleItem)

    def test_setattr(self):
        self.assertIsInstance(self.item1.test_setattr_node1, SimpleItem)

    def test_setitem(self):
        self.assertIsInstance(self.item1['test_setitem1_node1'], SimpleItem)

    def test_keys(self):
        self.assertEqual(self.item1.keys, ('node1', 'node2'))
        self.assertEqual(self.item2.keys, ('node1', 'node2'))
        self.assertEqual(self.item3.keys, ('node1', 'node2'))
        self.assertEqual(self.item4.keys, ('node1', 'node2'))
        self.assertEqual(self.item5.keys, ('node1', 'node2'))
        self.assertEqual(self.item6.keys, ('node1', 'node2'))

    def test_from_yalm(self):
        self.assertEqual(self.item7.settings.username, 'admin')
        self.assertEqual(self.item7.settings.host, '0.0.0.0')


if __name__ == '__main__':
    unittest.main()
