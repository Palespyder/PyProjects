$(function () {
    "use strict";
    
//    $('#row2 .widget').equalHeight()
    
    /**
     *  STATS
     *  ======================================================================
     **/
    // morris.js chart
    var d = new Date(),
    today = d.getFullYear() + '-' + d.getMonth() + '-' + d.getDate();
    var stats = function(colors){
        Morris.Area({
            element: 'stats-chart',
            data: [
                {period: today + ' 01:00', today: 3, yesterday: 2.5},
                {period: today + ' 02:00', today: 4, yesterday: 3},
                {period: today + ' 03:00', today: 6, yesterday: 5.5},
                {period: today + ' 04:00', today: 6.5, yesterday: 4},
                {period: today + ' 05:00', today: 5.5, yesterday: 4.5},
                {period: today + ' 06:00', today: 4.5, yesterday: 1.5},
                {period: today + ' 07:00', today: 15, yesterday: 13},
                {period: today + ' 08:00', today: 10, yesterday: 8},
                {period: today + ' 09:00', today: 10.5, yesterday: 8},
                {period: today + ' 10:00', today: 12, yesterday: 11},
                {period: today + ' 11:00', today: 8, yesterday: 9},
                {period: today + ' 12:00', today: 2.5, yesterday: 2},
                {period: today + ' 13:00', today: 3, yesterday: 2.5},
                {period: today + ' 14:00', today: 4, yesterday: 3},
                {period: today + ' 15:00', today: 6, yesterday: 5.5},
                {period: today + ' 16:00', today: 6.5, yesterday: 4},
                {period: today + ' 17:00', today: 5.5, yesterday: 4.5},
                {period: today + ' 18:00', today: 4.5, yesterday: 1.5},
                {period: today + ' 19:00', today: 15, yesterday: 13},
                {period: today + ' 20:00', today: 10, yesterday: 8},
                {period: today + ' 21:00', today: 10.5, yesterday: 8},
                {period: today + ' 22:00', today: 12, yesterday: 11},
                {period: today + ' 23:00', today: 8, yesterday: 9},
                {period: today + ' 24:00', today: 2.5, yesterday: 2}
            ],
            xkey: 'period',
            xLabels: 'hour',
            ykeys: ['today', 'yesterday'],
            labels: ['Today', 'Yesterday'],
            pointSize: 2,
            hideHover: 'auto',
            lineColors: [colors, '#D80073'],
            yLabelFormat: function(y){
                return y.toString() + ' K'
            }
        });
    }
    stats('#1BA1E2');
    $(window).resize(function(){
        $('#stats-chart').empty()
        stats('#1BA1E2')
    })
    
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

        $.each($('.widget'), function(){
            var widget = $(this),
            widget_header = widget.find('.widget-header'),
            widget_action = widget.find('.widget-action');

            if(widget.is('[class*="border-"]')){
                widget.attr('class', 'widget border-'+theme) // widget border
            }
            if(widget.is('[class*="bg-"]')){
                widget.attr('class', 'widget bg-'+theme) // widget theme bgcolor
            }
            if(widget_header.is('[class*="bg-"]')){
                widget_header.attr('class', 'widget-header bg-'+theme) // widget header
            }
            if(widget_action.is('[class*="color-"]')){
                widget_action.attr('class', 'widget-action color-'+theme) // widget action
            }
        })

        $('.chat-action form').find('.btn').attr('class', 'btn bg-'+theme) // chat button
        $('.overview-today .overview-count').attr('class', 'overview-count color-'+theme)
        
        var colorhex = null;
        if(theme == 'lime'){ colorhex = '#A4C400' }
        else if(theme == 'green'){ colorhex = '#60A917' }
        else if(theme == 'emerald'){ colorhex = '#008A00' }
        else if(theme == 'teal'){ colorhex = '#00ABA9' }
        else if(theme == 'cyan'){ colorhex = '#1BA1E2' }
        else if(theme == 'cobalt'){ colorhex = '#0050EF' }
        else if(theme == 'indigo'){ colorhex = '#6A00FF' }
        else if(theme == 'violet'){ colorhex = '#AA00FF' }
        else if(theme == 'pink'){ colorhex = '#F472D0' }
        else if(theme == 'crimson'){ colorhex = '#A20025' }
        else if(theme == 'red'){ colorhex = '#E51400' }
        else if(theme == 'orange'){ colorhex = '#FA6800' }
        else if(theme == 'amber'){ colorhex = '#F0A30A' }
        else if(theme == 'yellow'){ colorhex = '#E3C800' }
        else if(theme == 'brown'){ colorhex = '#825A2C' }
        else if(theme == 'olive'){ colorhex = '#6D8764' }
        else if(theme == 'steel'){ colorhex = '#647687' }
        else if(theme == 'mauve'){ colorhex = '#76608A' }
        else if(theme == 'taupe'){ colorhex = '#87794E' }
        else{ colorhex = '#323232' }
        
        $('#stats-chart').empty()
        stats(colorhex)
        
        $(window).resize(function(){
            $('#stats-chart').empty()
            stats(colorhex)
        })
    })
});