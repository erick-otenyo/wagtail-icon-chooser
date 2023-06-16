import itertools
from xml.dom import minidom

from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from wagtail import hooks

_svg_icons = {}


def get_svg_icons():
    global _svg_icons
    if not _svg_icons:
        icon_hooks = hooks.get_hooks("register_icons")
        all_icons = sorted(
            itertools.chain.from_iterable(hook([]) for hook in icon_hooks)
        )
        for icon in all_icons:
            svg_str = render_to_string(icon)
            doc = minidom.parseString(svg_str)
            svg = doc.getElementsByTagName("svg")
            if svg:
                svg = svg[0]
                icon_id = svg.getAttribute("id")
                if icon_id:
                    if icon_id.startswith("icon-"):
                        icon_id = icon_id.replace("icon-", "")
                    _svg_icons[icon_id] = svg_str
            else:
                symbol = doc.getElementsByTagName("symbol")
                if symbol:
                    symbol = symbol[0]
                    icon_id = symbol.getAttribute("id")
                    if icon_id:
                        if icon_id.startswith("icon-"):
                            icon_id = icon_id.replace("icon-", "")
                            svg_str = symbol.toxml().replace("symbol", "svg")
                            doc = minidom.parseString(svg_str)
                            svg = doc.getElementsByTagName("svg")
                            if svg:
                                svg = svg[0]
                                svg.setAttribute('xmlns', 'http://www.w3.org/2000/svg')
                                svg.setAttribute("id", icon_id)
                                _svg_icons[icon_id] = mark_safe(svg.toxml())
    return _svg_icons
