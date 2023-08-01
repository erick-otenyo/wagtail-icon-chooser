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

            try:
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
                        symbol_icon_id = symbol.getAttribute("id")
                        if symbol_icon_id:
                            if symbol_icon_id.startswith("icon-"):
                                icon_id = symbol_icon_id.replace("icon-", "")
                                svg_str = symbol.toxml().replace("symbol", "svg")
                                doc = minidom.parseString(svg_str)
                                svg = doc.getElementsByTagName("svg")
                                if svg:
                                    svg = svg[0]
                                    svg.setAttribute('xmlns', 'http://www.w3.org/2000/svg')
                                    svg.setAttribute("id", symbol_icon_id)
                                    _svg_icons[icon_id] = mark_safe(svg.toxml())
            except Exception:
                pass

    return _svg_icons


def get_svg_sprite_for_icons(icons_list):
    svg_icons = get_svg_icons()
    combined_icon_markup = ""
    for icon in icons_list:
        svg_str = svg_icons.get(icon)
        if svg_str:
            combined_icon_markup += (
                svg_str.replace('xmlns="http://www.w3.org/2000/svg"', "").replace("svg", "symbol")
            )
    _icons_html = render_to_string(
        "wagtailadmin/shared/icons.html", {"icons": combined_icon_markup}
    )

    return _icons_html
