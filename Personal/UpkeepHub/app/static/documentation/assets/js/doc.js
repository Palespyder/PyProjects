$(function(){
    'use strict';
    
    
    // animate scroll
    $(".scroll").click(function(e){
        e.preventDefault();
        $("html,body").animate({scrollTop: $(this.hash).offset().top-60}, 'slow');
    });
    
    
    $('body').append('<a href="#" class="scroll-top bg-cyan" data-toggle="tooltip" title="back to top"><i class="icomo-arrow-up-2 text-3x"></i></a>')
    // scrolling event
    $(window).scroll(function() {
        if($(this).scrollTop() > 100) {
            $('.scroll-top').fadeIn('slow')
        }
        else{
            $('.scroll-top').fadeOut('slow')
        }
    })
    
    $('.scroll-top').click(function(e){
        e.preventDefault();
        $("html,body").animate({scrollTop: 0}, 'slow');
    })
    
    // tooltips
    $('[data-toggle=tooltip]').tooltip()
})