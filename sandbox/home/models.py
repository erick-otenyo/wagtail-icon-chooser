from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField
from wagtail.models import Page

from wagtailiconchooser.blocks import IconChooserBlock
from wagtailiconchooser.widgets import IconChooserWidget


class HomePage(Page):
    icon = models.CharField(max_length=100, null=True, blank=True)
    stream_field_with_icon = StreamField([
        ('icon', IconChooserBlock()),
    ], use_json_field=True, blank=True, null=True)

    content_panels = Page.content_panels + [
        FieldPanel("icon", widget=IconChooserWidget),
        FieldPanel("stream_field_with_icon"),
    ]
