//homepage square (mobile) button height 
//$(function() {
//    var appBtnWidth = $('.app-btn').width();
//    $('.app-btn').height(appBtnWidth);
//});

// ######################################## ERRORS ########################################
// #                       should resize on both expand and shrink                        #
// #                          no longer functions in framework                            #
// ########################################################################################
$(window).resize(function() {
    var pagewidth = $("body").innerWidth();
        if(document.URL.indexOf("")>=0){
            if(pagewidth>=768){
            $('#includeMain').css({padding:0})
            }
        }
});
