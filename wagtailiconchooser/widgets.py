import json

from django.forms import widgets, Media
from wagtail.telepath import register
from wagtail.widget_adapters import WidgetAdapter


class IconChooserWidget(widgets.TextInput):
    template_name = "wagtailiconchooser/widgets/icon-chooser-widget.html"
    
    def __init__(self, attrs=None):
        default_attrs = {
            "class": "icon-chooser-widget__icon-input",
        }
        attrs = attrs or {}
        attrs = {**default_attrs, **attrs}
        super().__init__(attrs=attrs)
    
    def build_attrs(self, *args, **kwargs):
        attrs = super().build_attrs(*args, **kwargs)
        attrs['data-controller'] = 'icon-chooser-widget'
        
        return attrs
    
    @property
    def media(self):
        css = {
            "all": [
                "wagtailiconchooser/css/icon-chooser-widget.css",
            ]
        }
        
        js = [
            "wagtailiconchooser/js/icon-chooser-widget.js",
            "wagtailiconchooser/js/icon-chooser-widget-controller.js",
        ]
        
        return Media(js=js, css=css)


class IconChooserWidgetAdapter(WidgetAdapter):
    js_constructor = "wagtailiconchooser.widgets.IconChooser"
    
    class Media:
        js = [
            "wagtailiconchooser/js/icon-chooser-widget-telepath.js",
        ]


register(IconChooserWidgetAdapter(), IconChooserWidget)
