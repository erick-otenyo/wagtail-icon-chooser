import json

from django.forms import widgets
from wagtail.telepath import register
from wagtail.utils.widgets import WidgetWithScript
from wagtail.widget_adapters import WidgetAdapter


class IconChooserWidget(WidgetWithScript, widgets.TextInput):
    template_name = "wagtailiconchooser/widgets/icon-chooser-widget.html"

    def __init__(self, attrs=None):
        default_attrs = {
            "class": "icon-chooser-widget__icon-input",
        }
        attrs = attrs or {}
        attrs = {**default_attrs, **attrs}
        super().__init__(attrs=attrs)

    def render_js_init(self, id_, name, value):
        return "$(document).ready(() => new IconChooserWidget({0}));".format(json.dumps(id_))

    class Media:
        css = {
            "all": [
                "wagtailiconchooser/css/icon-chooser-widget.css",
            ]
        }
        js = [
            "wagtailiconchooser/js/icon-chooser-widget.js",
        ]


class IconChooserWidgetAdapter(WidgetAdapter):
    js_constructor = "wagtailiconchooser.widgets.IconChooser"

    class Media:
        js = [
            "wagtailiconchooser/js/icon-chooser-widget-telepath.js",
        ]


register(IconChooserWidgetAdapter(), IconChooserWidget)
