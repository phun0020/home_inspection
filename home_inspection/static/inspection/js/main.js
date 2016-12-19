//get crsf token from cookies
var csrftoken = crsftoken.getCookie('csrftoken');

var csrfSafeMethod = function (method) {
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

// inject this csrf token to every ajax call
$.ajaxSetup({
    beforeSend: function (xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

//------------------------index.js------------------------

// toggle add-form-property button
// hide/show the form
$('#toggle-add-new').bootstrapToggle({
      on: 'Show',
      off: 'Hide',
      onstyle: 'primary',
      offstyle: 'default',
      style: 'ios'
});


$('#toggle-add-new').on('change', function(){
    $('#prop-form-container').slideToggle( 400, 'linear' );
});

// add new property button
// call AJAX and update the property-container
$('#newPropBtn').on('click', function(){
    index.ajaxAdd();
})

// del selected property button
$('#property-container').on('click', 'button.delProp', function(){
    index.ajaxDelete($(this).attr('data-id'));
});

//------------------------room.js------------------------

$('.room-type-btn').on('click', function(e){
    e.preventDefault();
    // both roomType and roomName are radio buttons
    // propertyId is seperate input
    $(this).siblings("input[type='radio']").prop("checked", true);
    
    room.ajaxAddRoom();
});

$('#room-container').on('click', 'button.deleteRoom', function(){
    room.ajaxDeleteRoom($(this).attr('data-url'));
});

room.xeditableRoomName();