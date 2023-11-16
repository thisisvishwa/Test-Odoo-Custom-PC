```python
from odoo.tests import common

class TestBuild(common.TransactionCase):

    def setUp(self):
        super(TestBuild, self).setUp()
        self.Build = self.env['build']

    def test_component_selection(self):
        build = self.Build.create({'name': 'Test Build'})
        self.assertEqual(build.name, 'Test Build')

    def test_component_configuration(self):
        build = self.Build.create({'configuration': 'Test Configuration'})
        self.assertEqual(build.configuration, 'Test Configuration')

    def test_component_customization(self):
        build = self.Build.create({'customization': 'Test Customization'})
        self.assertEqual(build.customization, 'Test Customization')

    def test_component_pricing(self):
        build = self.Build.create({'price': 1000})
        self.assertEqual(build.price, 1000)

    def test_build_history(self):
        build = self.Build.create({'name': 'Test Build'})
        self.assertIn(build, self.Build.search([]))

    def test_build_recommendations(self):
        build = self.Build.create({'recommendations': 'Test Recommendations'})
        self.assertEqual(build.recommendations, 'Test Recommendations')

    def test_build_sharing(self):
        build = self.Build.create({'sharing': 'Test Sharing'})
        self.assertEqual(build.sharing, 'Test Sharing')

    def test_build_import_export(self):
        build = self.Build.create({'import_export': 'Test Import/Export'})
        self.assertEqual(build.import_export, 'Test Import/Export')

    def test_build_analytics(self):
        build = self.Build.create({'analytics': 'Test Analytics'})
        self.assertEqual(build.analytics, 'Test Analytics')

    def test_build_support(self):
        build = self.Build.create({'support': 'Test Support'})
        self.assertEqual(build.support, 'Test Support')
```