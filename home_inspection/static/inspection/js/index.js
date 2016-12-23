var index = (function () {
    var xeditableProperty = function () {
        var url = $('.index-xeditable').closest('div.index-info-container').attr('data-url');
        var pk = function () { return $(this).closest('div.index-update-container').attr('data-pk'); }

        // for text only
        $('.index-xeditable').editable({
            url: url,
            pk: pk,
            type: "text",
            highlight: '#8e44ad',
            mode: 'inline',
            params: function (params) {
                // add class to seperate Owner and Property section
                params.class = $(this).attr('data-class');
                return params;
            },
            success: function (response, newValue){
                var dataName = $(this).attr('data-name');
                var nonUpdateContainer = $(this).closest('.updatable-prop').siblings('.non-updatable-prop');

                if(dataName === 'firstname'){
                    nonUpdateContainer.find('.propOwnerFname').text(newValue);
                } 
                if(dataName === 'lastname'){
                    nonUpdateContainer.find('.propOwnerLname').text(newValue);
                }
                if(dataName === 'address'){
                    nonUpdateContainer.find('.propAddress').text(newValue);
                }
                
            }
        });

        // specify for each select list
        // Property Type xeditable
        $('.index-xeditable-select.propertyType').editable({
            url: url,
            pk: pk,
            value: function(){ 
                return $(this).attr('data-value');
            },
            type: 'select',
            mode: 'inline',
            source: function(){ 
                // parse whole list to xeditable
                return $(this).attr('data-obj');
            },
            params: function (params) {
                // add class to seperate Owner and Property section
                params.class = $(this).attr('data-class');
                return params;
            }
        });

        // Building Type xeditable
        $('.index-xeditable-select.buildingType').editable({
            url: url,
            pk: pk,
            value: function() { return $(this).attr('data-current'); },
            type: 'select',
            mode: 'inline',
            source: function(){ 
                return $(this).attr('data-obj');
            },
            params: function (params) {
                params.class = $(this).attr('data-class');
                return params;
            }
        });

        
    }

    // call ajax when add new property
    var ajaxAdd = function () {
        $.ajax({
            url: '/inspection/',
            type: 'POST',
            data: $('#newPropForm').serialize(),
            success: function (response, textStatus, jqXHR) {
                // debugger;
                $('#property-container').html(response);
                $(':input', '#newPropForm')
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
        ajaxDelete: ajaxDelete,
        xeditableProperty: xeditableProperty
    };

})();