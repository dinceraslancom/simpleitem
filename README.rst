SimpleItem
---------------------------

Python SimpleItem Library.

Installing
----------

Install and update using `pip3`_:

.. code-block:: text

    $ pip3 install simpleitem

Python 3 and newer.

.. _pip3: https://pip.pypa.io/en/stable/quickstart/


SimpleItem Example
------------------

Easy to define and use features.

.. code-block:: python

    >> from simpleitem import SimpleItem

    >> item1 = SimpleItem()

    >> item1.node1 = 1

    >> item1['node2']node3 = 3

    >> item1['node1']
    1

    >> item1.node2.node3
    3

    >> item1['node2'].node3
    3

    >> item1.node2['node3']
    3

    >> item1['node2']['node3']
    3

Other Usage Examples

.. code-block:: python

    >> item2 = SimpleItem()
    >> item2['node1'] = 1
    >> item2['node2']['node3'] = 3

    >> item3 = SimpleItem(node1=1, node2={'node3': 3})

    >> item4 = SimpleItem(**{'node1': 1, 'node2': {'node3': 3}})

    >> item5 = SimpleItem()
    >> item5(node1=1, node2={'node3': 3})

    >> item6 = SimpleItem()
    >> item6(**{'node1': 1, 'node2': {'node3': 3}})

path; test.yaml

    settings:
        username: admin

        host: 0.0.0.0

.. code-block:: python

    >> item = SimpleItem()
    >> item.from_yaml(path)

    >> item.setting.username
    admin

    >> setting = item.setting
    >> setting.host
    0.0.0.0


MemoryStorage Example
-----------------------

MemoryStorage designed as singleton pattern, define somewhere use everywhere.

.. code-block:: python

    >> from simpleitem import MemoryStorage

    >> storage = MemoryStorage()

    >> settings = storage.settings
    >> settings.sleep = 1
    >> settings.sleep
     1

    >> settings(debug=True)
    >> storage.settings.debug
     True

Support
-------

*   Python 3.x
*   Supports all operating systems

Links
-----

*   License: `MIT License <https://github.com/dinceraslancom/simpleitem/blob/master/LICENSE>`_
*   Code: https://github.com/dinceraslancom/simpleitem
