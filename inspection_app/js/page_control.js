if(document.URL.indexOf("index.html")>=0){
    $('#includeMain').css({padding:0})
}
$(function() {
    var appBtnWidth = $('.app-btn').width();
    $('.app-btn').height(appBtnWidth);
});