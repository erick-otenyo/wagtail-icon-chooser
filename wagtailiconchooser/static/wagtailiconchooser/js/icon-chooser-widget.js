function IconChooserWidget(id) {
    /*
    id = the ID of the HTML element where icon input should be attached
    */
    this.iconInput = $('#' + id);
    this.iconContainer = $("#" + id + "-icon-container")
    this.initialRender = true

    this.modalTrigger = $("#" + id + "-modal-trigger")
    this.modalTrigger.on("click", () => {
        this.createIconOptions()
        if (this.modalContainer) {
            this.modalContainer.modal("show")
        }
    })

    this.iconClear = $("#" + id + "-icon-choice-clear")
    this.iconClear.on("click", this.handleSelectedIconClear.bind(this))
}


IconChooserWidget.prototype.setState = function (newState) {
    this.iconInput.val(newState);
    // show initially selected
    if (this.initialRender) {
        this.initialRender = false
        if (newState) {
            const svg = this.createIconSvgEl(newState)
            this.iconContainer.html(svg)
            this.iconClear.show()

        }
    }
};

IconChooserWidget.prototype.getState = function () {
    return this.iconInput.val();
};

IconChooserWidget.prototype.getValue = function () {
    return this.iconInput.val();
};

IconChooserWidget.prototype.focus = function () {
    this.iconInput.focus();
}

IconChooserWidget.prototype.createIconOptions = function () {
    const that = this
    $('body > .modal').remove();
    this.modalContainer = $(`<div class="modal fade" tabindex="-1" role="dialog" aria-hidden="true">
                                <div class="modal-dialog"><div class="modal-content">
                                    <button type="button" class="button close button--icon text-replace" data-dismiss="modal">
                                    <svg class="icon icon-cross" aria-hidden="true"><use href="#icon-cross"></use></svg>
                                        Close
                                    </button>
                                    <div class="modal-body">
                                        <header class="w-header w-header--hasform">
                                            <div class="row">
                                                <div class="left">
                                                    <div class="col">
                                                        <h1 class="w-header__title" id="header-title">
                                                            <svg class="icon icon-doc-empty-inverse w-header__glyph" aria-hidden="true">
                                                                <use href="#icon-doc-empty-inverse"></use>
                                                            </svg>
                                                            Choose icon
                                                        </h1>
                                                    </div>
                                                        <div class="w-field__wrapper w-mb-0 -w-mt-2.5" data-field-wrapper="">
                                                            <label class="w-field__label w-sr-only" htmlFor="id_icon_modal_filter" id="id_q-label">
                                                                Search
                                                            </label>
                                                            <div class="w-field w-field--char_field w-field--text_input">
                                                                <div class="w-field__input" data-field-input="">
                                                                    <svg class="icon icon-search w-field__icon" aria-hidden="true">
                                                                        <use href="#icon-search"></use>
                                                                    </svg>
                                                                    <input type="text" name="q" placeholder="Search" id="id_icon_modal_filter">
                                                                </div>
                                                            </div>
                                                        </div>
                                                </div>
                                            </div>
                                        </header>
                                        <div class="modal-icons-content"></div>
                                    </div>
                                </div>
                            </div>
                        </div>`);

    $('body').append(this.modalContainer);
    this.modalContainer.modal('hide');


    this.modalContainer.on('hidden.bs.modal', function () {
        that.modalContainer.remove();
    });

    this.modalIconsContent = this.modalContainer.find('.modal-icons-content');

    const $svgDefs = $('div[data-sprite] svg defs symbol')
    $svgDefs.each(function () {
            let iconId = $(this).attr("id")
            const parts = iconId.split("-")
            if (parts[0] === "icon") {
                iconId = parts.slice(1).join("-")
            }
            const $container = $("<div class='svg-container'>")
            $container.on("click", () => that.onIconSelect(iconId))
            $(`<svg class="icon icon-option" aria-hidden="true"><use href="#icon-${iconId}"></use></svg>`).appendTo($container)
            $(`<div class="icon-label">${iconId}</div>`).appendTo($container)
            $container.appendTo(that.modalIconsContent)
        }
    )


    this.iconModalFilter = $("#id_icon_modal_filter")
    this.iconModalFilter.on('keyup', this.handleIconListFilter.bind(this));
}

IconChooserWidget.prototype.onIconSelect = function (iconId) {
    const svg = this.createIconSvgEl(iconId)
    this.iconContainer.html(svg)
    this.setState(iconId)

    if (this.modalContainer) {
        // close modal
        this.modalContainer.modal("hide")
    }
    // show clear button
    this.iconClear.show()
}

IconChooserWidget.prototype.createIconSvgEl = function (iconId) {
    return $(`<svg class="icon selected-icon" aria-hidden="true"><use href="#icon-${iconId}"></use></svg>`)
}


IconChooserWidget.prototype.handleIconListFilter = function (e) {
    const value = e.target.value
    this.modalIconsContent.find("div").filter(function () {
        $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
    });
}


IconChooserWidget.prototype.handleSelectedIconClear = function () {
    // clear input value
    this.setState("")
    // clear displayed icon
    this.iconContainer.html("")
    // hide clear button
    this.iconClear.hide()
}







