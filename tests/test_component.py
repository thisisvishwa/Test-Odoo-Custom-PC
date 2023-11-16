```python
from odoo.tests import common

class TestComponent(common.TransactionCase):

    def setUp(self):
        super(TestComponent, self).setUp()
        self.Component = self.env['component']

    def test_component_selection(self):
        component = self.Component.create({'name': 'Test CPU', 'category': 'CPU', 'price': 200.00})
        self.assertEqual(component.name, 'Test CPU')

    def test_component_configuration(self):
        component = self.Component.create({'name': 'Test CPU', 'category': 'CPU', 'configuration': '4 cores', 'price': 200.00})
        self.assertEqual(component.configuration, '4 cores')

    def test_component_customization(self):
        component = self.Component.create({'name': 'Test CPU', 'category': 'CPU', 'customization': 'Black', 'price': 200.00})
        self.assertEqual(component.customization, 'Black')

    def test_component_pricing(self):
        component = self.Component.create({'name': 'Test CPU', 'category': 'CPU', 'price': 200.00})
        self.assertEqual(component.price, 200.00)
```