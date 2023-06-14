import itertools
from xml.dom import minidom

from django.template.loader import render_to_string
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
                svg_id = svg.getAttribute("id")
                if svg_id:
                    if svg_id.startswith("icon-"):
                        svg_id = svg_id.replace("icon-", "")
                    _svg_icons[svg_id] = svg_str

    return _svg_icons
