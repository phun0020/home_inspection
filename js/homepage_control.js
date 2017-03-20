function homeSize (){
    var pagewidth = $("body").innerWidth();
    if(pagewidth>=768){
        $('#includeMain').css({padding:0})
    }
    else 
        {
            $('#includeMain').css({padding:100})
        }
};

//change padding on load                 
homeSize()

//change padding on resize
$(window).resize(function(){
   homeSize()
});
