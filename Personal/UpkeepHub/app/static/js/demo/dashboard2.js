$(function () {
    "use strict";
    
//    $('#row2 .widget').equalHeight()
    
    /**
     *  STATS
     *  ======================================================================
     **/
    function randomInt(min, max) {
       return Math.floor(Math.random() * (max - min + 1)) + min;
    }
    var today = [];
    var yesterday = [];
    
    for(var i=0; i<24; i++){
        var at = 'AM';
        var clock = i;
        if(i > 12){
           at = 'PM' ;
           clock = i - 12;
        }
        
        var date = moment.utc();
        
        today.push( [ date.hour(i), randomInt(300, 600) ] );
        yesterday.push( [ date.hour(i), randomInt(200, 500) ] );
    }
    
    // render chart lines
    $.plot("#stats-chart", [{
        data: today, 
        color: '#1BA1E2',
        label: "Today"
    },{
        data: yesterday, 
        color: '#D80073',
        label: "Yesterday",
        yaxis: 2
    }], {
        legend: { show: false },
        xaxis: { show: false }, 
        grid: {
            hoverable: true,
            backgroundColor: 'transparent',
            borderWidth: 0
        }
    });
    /**
     *  HELP TOOLTIPS FLOT CHART
     *  ======================================================================
     **/
    var showTooltip = function(color, x, y, contents) {
        $("<div id='tooltip' class='flot-tooltip'>" + contents + "</div>").css({
            top: y + 20,
            left: x - 50,
            borderColor: color,
            color: color
        }).appendTo("body").fadeIn(200);
    }
    $("#stats-chart").bind("plothover", function (event, pos, item) {
        var previousPoint = null;
        if(item){
            if (previousPoint != item.dataIndex) {
                
                previousPoint = item.dataIndex;
                
                $("#tooltip").remove();
                var x = moment.utc(item.datapoint[0]).format('hA'),
                y = item.datapoint[1],
                color = item.series.color;
                
                showTooltip(color ,item.pageX, item.pageY, item.series.label + " at " + x + " = " + y);
            }
        } else {
            $("#tooltip").remove();
            previousPoint = null;            
        }
    });
    
    
    
    /**
     *  CONTENT MANAGER
     *  ======================================================================
     **/
    // simple table sorter
    $('table[data-sorter="true"]').tablesorter();
    

    // chat setting, scrollbar and more
    $('#chat').mCustomScrollbar("scrollTo","bottom");
    $('[data-toggle="add-others"]').click(function(){
        $('.add-to-chat').slideToggle('fast', 'easeOutBack')
    })
    $('[name="addtochat"]').select2({
        placeholder: "Select user to add"
    })
    // chat action
    $('#form-chat').submit(function(){
        var message = $('input[name="chat-text"]').val(),
        template = '<li class="self">'
                    +'<div class="avatar">'
                    +'    <img src="img/demo/1.jpg" alt="" title="me" />'
                    +'</div>'
                    +'<div class="messages">'
                    +'    <p>'+ message +'</p>'
                    +'    <time datetime="2013-06-05T20:14">just now</time>' // just sample time, replace with your own value
                    +'</div>'
                    +'</li>';
        
        if(message != '' && message != ' '){
            $('ol.chats').append(template);
            $('#chat').mCustomScrollbar('update')
            $('#chat').mCustomScrollbar("scrollTo","bottom")

            // other replay scenario
            setTimeout(function() {
                template = '<li class="other">'
                        +'<div class="avatar">'
                        +'    <img src="img/demo/2.jpg" alt="" title="john doe" />'
                        +'</div>'
                        +'<div class="messages">'
                        +'    <p>Demo : just simple replay from other.</p>'
                        +'    <time datetime="2013-06-05T20:14">john doe | just now</time>' // just sample time, replace with your own value
                        +'</div>'
                        +'</li>';

                $('ol.chats').append(template);
                $('#chat').mCustomScrollbar('update')
                $('#chat').mCustomScrollbar("scrollTo","bottom")
            }, 3000);

            $('input[name="chat-text"]').val('') // remove chat-text value
        }
        
        return false;
    })
    // add some user
    $('#form-addtochat').submit(function(){
        var data = $('[name="addtochat"]').select2('val')
        if(data.length > 0){
            $.each(data, function(i, v){
                var template = '<li class="moderator">'
                        +'<div class="messages"><p>'+ v +' now join to chat</p></div>'
                        +'</li>';

                $('[name="addtochat"] option[value="'+v+'"]').remove()
                $('[name="addtochat"]').select2({
                    placeholder: "Select user to add"
                })
                $('ol.chats').append(template);
                $('#chat').mCustomScrollbar('update')
                $('#chat').mCustomScrollbar("scrollTo","bottom")
            })
        }
        
        $('.add-to-chat').slideToggle('fast', 'easeOutBack')
        return false;
    })
    
    
    
    /**
     *  QUICK POST
     *  ======================================================================
     **/
    // bootstrap wysihtml5
    $('#post-content').wysihtml5();
    $('[data-form="select2"]').select2();
    $('#post-tags').select2({
        tags: ["print", "webs", "icons", "graphics", "vectors", "bussiness", "others"]
    })
    
    
    
    // themes demo, just for page dashboard, you can remove or modified this part
    $('.syncronize .themes-choice > a, .unsyncronize .themes-navbar > a').on('click', function(e){
        e.preventDefault();
        var theme = $(this).attr('data-theme');
        
        $('.widget:first').attr('class', 'widget border-'+theme) // widget
        $('.widget:first .widget-header').attr('class', 'widget-header bg-'+theme) // widget header
        $('.widget:first .widget-action').attr('class', 'widget-action color-'+theme) // widget action
    })
});