from dcim import forms
from django.test import SimpleTestCase

from netbox_metatype_importer.utils import related_object_forms


class RelatedObjectFormsTest(SimpleTestCase):
    def test_netbox_46_port_mappings_are_imported(self):
        self.assertIs(related_object_forms()['port-mappings'], forms.PortTemplateMappingImportForm)

    def test_netbox_47_cooling_templates_are_imported(self):
        mapping = related_object_forms()
        self.assertIs(mapping['cooling-intakes'], forms.CoolingIntakeTemplateImportForm)
        self.assertIs(mapping['cooling-outflows'], forms.CoolingOutflowTemplateImportForm)

    def test_cooling_intakes_precede_outflows(self):
        keys = list(related_object_forms())
        self.assertLess(keys.index('cooling-intakes'), keys.index('cooling-outflows'))
