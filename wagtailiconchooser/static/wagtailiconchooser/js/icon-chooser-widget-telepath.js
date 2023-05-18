(function () {
    function IconChooser(html) {
        this.html = html;
    }

    IconChooser.prototype.render = function (placeholder, name, id, initialState) {
        const html = this.html.replace(/__NAME__/g, name).replace(/__ID__/g, id);
        placeholder.outerHTML = html;

        const iconChooser = new IconChooserWidget(id);
        iconChooser.setState(initialState);
        return iconChooser;
    };

    window.telepath.register('wagtailiconchooser.widgets.IconChooser', IconChooser);
})();