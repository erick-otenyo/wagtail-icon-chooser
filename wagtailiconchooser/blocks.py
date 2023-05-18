from django import forms
from django.utils.functional import cached_property
from wagtail.blocks import FieldBlock

from wagtailiconchooser.widgets import IconChooserWidget


class IconChooserBlock(FieldBlock):
    def __init__(self, max_length=100, required=True, help_text=None, validators=(), **kwargs):
        self.field_options = {
            "required": required,
            "help_text": help_text,
            "max_length": max_length
        }
        super().__init__(**kwargs)

    @cached_property
    def field(self):
        field_kwargs = {"widget": IconChooserWidget()}
        field_kwargs.update(self.field_options)
        return forms.CharField(**field_kwargs)

    class Meta:
        icon = "radio-full"
