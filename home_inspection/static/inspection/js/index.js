var index = (function () {
    // call ajax when add new property
    var ajaxAdd = function () {
        $.ajax({
            url: '/inspection/',
            type: 'POST',
            data: $('#newPropForm').serialize(),
            success: function (response, textStatus, jqXHR) {
                // debugger;
                $('#property-container').html(response);
                $(':input','#newPropForm')
                .not(':button, :submit, :reset, :hidden')
                .val('')
                .removeAttr('checked')
                .removeAttr('selected');
            }
        });
    };

    var ajaxDelete = function (id) {
        $.ajax({
            url: '/inspection/' + id + '/delete',
            type: 'POST',
            success: function (response, textStatus, jqXHR) {
                $('#property-container').html(response);
            }
        });
    };

    return {
        ajaxAdd: ajaxAdd,
        ajaxDelete : ajaxDelete
    };

})();