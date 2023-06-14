from xml.dom import minidom

from django import template
from django.utils.safestring import mark_safe

from wagtailiconchooser.utils import get_svg_icons

register = template.Library()


@register.simple_tag
def svg_icon(name=None, classname=None):
    """
    Load svg icon.

    Usage:
        {% load wagtailiconchooser_tags %}
        ...
        {% svg_icon name="cogs" classname="your-custom-class" %}

    :param name: the icon name/id, required (string)
    :param classname: css classname to add to svg (string)
    """

    if not name:
        raise ValueError("You must supply an icon name")

    svg_icons = get_svg_icons()

    if svg_icons.get(name):
        svg_str = svg_icons.get(name)

        if classname:
            doc = minidom.parseString(svg_str)
            svg = doc.getElementsByTagName("svg")[0]
            svg.setAttribute("class", classname)
            return mark_safe(svg.toxml())
        else:
            return svg_str

    return None
