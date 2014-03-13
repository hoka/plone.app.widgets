from zope.interface import Interface
from Products.CMFCore.utils import getToolByName
from zope.component.hooks import getSite

class IRichTextEditor(Interface):

    def is_selected(self, editor):
        """
            Check if a special editor is selected by the user
            or set by default.
        """


class Adapter:

    def __init__(self, context):
        self.context = context

    def is_selected(self, editor):
        context = self.context
        portal=getSite()
        pm = getToolByName(portal, 'portal_membership')
        auth = pm.getAuthenticatedMember()

        selected_editor = auth.getProperty('wysiwyg_editor')
        if not selected_editor:
            sp = getToolByName(portal, 'portal_properties').site_properties
            selected_editor = sp.getProperty('default_editor')

        if selected_editor == editor:
            return True
