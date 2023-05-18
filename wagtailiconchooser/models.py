from wagtail.admin.views import home
from wagtail.models import Page


class CustomIconPage(Page):
    class Meta:
        abstract = True

    def get_context(self, request, *args, **kwargs):
        context = super(CustomIconPage, self).get_context(request, *args, **kwargs)
        # add icons
        context.update({"icons_svg_sprite": home.icons()})

        return context
