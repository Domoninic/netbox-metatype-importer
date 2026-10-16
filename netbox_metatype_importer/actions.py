from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from netbox.object_actions import ObjectAction

__all__ = ('DeviceTypeActions', 'ModuleTypeActions', 'RackTypeActions')


class MetaTypeBulkAction(ObjectAction):
    """
    Base for the Import/Delete Selected buttons. Rendering them as ObjectActions (rather than by overriding the
    `bulk_buttons` template block) is required as of NetBox v4.7.3, which skips the block entirely when a view
    defines no actions.
    """

    multi = True
    template_name = 'netbox_metatype_importer/buttons/bulk_action.html'
    url_name = None
    button_class = None
    icon = None

    @classmethod
    def get_url(cls, obj):
        return reverse(f'plugins:netbox_metatype_importer:{cls.url_name}')

    @classmethod
    def get_context(cls, context, obj):
        return {'button_class': cls.button_class, 'icon': cls.icon}


def _make_actions(prefix):
    class ImportSelected(MetaTypeBulkAction):
        name = 'import'
        label = _('Import Selected')
        permissions_required = {'add'}
        url_name = f'meta{prefix}type_import'
        button_class = 'btn-warning'
        icon = 'mdi-upload'

    class DeleteSelected(MetaTypeBulkAction):
        name = 'bulk_delete'
        label = _('Delete Selected')
        permissions_required = {'delete'}
        url_name = f'bulk_meta{prefix}type_delete'
        button_class = 'btn-danger'
        icon = 'mdi-trash-can-outline'

    return (ImportSelected, DeleteSelected)


DeviceTypeActions = _make_actions('device')
ModuleTypeActions = _make_actions('module')
RackTypeActions = _make_actions('rack')
