"""TO-DO: Write a description of what this XBlock is."""

import pkg_resources

from django.utils import translation
from xblock.core import XBlock
from xblock.fields import Scope, Integer
from xblock.fragment import Fragment
from xblockutils.resources import ResourceLoader


class {{cookiecutter.class_name}}(XBlock):
    """
    TO-DO: document what your XBlock does.
    """

    # Fields are defined on the class.  You can access them in your code as
    # self.<fieldname>.

    # TO-DO: delete count, and define your own fields.
    count = Integer(
        default=0, scope=Scope.user_state,
        help="A simple counter, to show something happening",
    )

    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    # TO-DO: change this view to display your data your own way.
    def student_view(self, context=None):
        """
        The primary view of the {{cookiecutter.class_name}}, shown to students
        when viewing courses.
        """
        html = self.resource_string("static/html/{{cookiecutter.package_name}}.html")
        frag = Fragment(html.format(self=self))
        frag.add_css(self.resource_string("static/css/{{cookiecutter.package_name}}.css"))

        # Add i18n js
        statici18n_js_url = self._get_statici18n_js_url()
        if statici18n_js_url:
            frag.add_javascript_url(self.runtime.local_resource_url(self, statici18n_js_url))

        frag.add_javascript(self.resource_string("static/js/src/{{cookiecutter.package_name}}.js"))
        frag.initialize_js('{{cookiecutter.class_name}}')
        return frag

    # TO-DO: change this handler to perform your own actions.  You may need more
    # than one handler, or you may not need any handlers at all.
    @XBlock.json_handler
    def increment_count(self, data, suffix=''):
        """
        An example handler, which increments the data.
        """
        # Just to show data coming in...
        assert data['hello'] == 'world'

        self.count += 1
        return {"count": self.count}

    # TO-DO: change this to create the scenarios you'd like to see in the
    # workbench while developing your XBlock.
    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("{{cookiecutter.class_name}}",
             """<{{cookiecutter.tag_name|lower}}/>
             """),
            ("Multiple {{cookiecutter.class_name}}",
             """<vertical_demo>
                <{{cookiecutter.tag_name|lower}}/>
                <{{cookiecutter.tag_name|lower}}/>
                <{{cookiecutter.tag_name|lower}}/>
                </vertical_demo>
             """),
        ]

    @staticmethod
    def _get_statici18n_js_url():
        """
        Returns the Javascript translation file for the currently selected language, if any.
        Defaults to English if available.
        """
        lang_code = translation.get_language()
        if not lang_code:
            return
        text_js = 'public/js/translations/{lang_code}/text.js'
        country_code = lang_code.split('-')[0]
        for code in (lang_code, country_code, 'en'):
            loader = ResourceLoader(__name__)
            if pkg_resources.resource_exists(loader.module_name, text_js.format(lang_code=code)):
                return text_js.format(lang_code=code)
