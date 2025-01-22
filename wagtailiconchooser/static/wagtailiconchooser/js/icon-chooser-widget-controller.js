class IconChooserWidgetController extends window.StimulusModule.Controller {
    connect() {
        new IconChooserWidget(this.element.id);
    }
}

window.wagtail.app.register('icon-chooser-widget', IconChooserWidgetController);