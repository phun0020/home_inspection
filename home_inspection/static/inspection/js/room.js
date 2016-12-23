var room = (function () {
    var xeditableRoomName = function(){
        $('.room-xeditable-text').editable({
            type : "text",
            highlight : '#8e44ad',
            mode : 'inline'
        });
    }
    // call ajax when add new property

    var ajaxAddRoom = function () {
        $.ajax({
            url: $('#hidden-room-form').attr('action'),
            type: 'POST',
            data: $('#hidden-room-form').serialize(),
            success: function (response, textStatus, jqXHR) {
                // debugger;
                $('#room-container').html(response);
                xeditableRoomName();
            }
        });
    };

    var ajaxDeleteRoom = function (url) {
        $.ajax({
            url: url,
            type: 'POST',
            success: function (response, textStatus, jqXHR) {
                // debugger;
                $('#room-container').html(response);
                xeditableRoomName();
            }
        });
    };

    return {
        ajaxAddRoom: ajaxAddRoom,
        ajaxDeleteRoom: ajaxDeleteRoom,
        xeditableRoomName: xeditableRoomName
    };

})();