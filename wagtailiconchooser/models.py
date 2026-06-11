from wagtail.models import Page

try:
    from wagtail.admin.icons import get_icons
except ImportError:
    from wagtail.admin.views.home import icons as get_icons


class CustomIconPage(Page):
    class Meta:
        abstract = True

    def get_context(self, request, *args, **kwargs):
        context = super(CustomIconPage, self).get_context(request, *args, **kwargs)
        context.update({"icons_svg_sprite": get_icons()})

        return context
