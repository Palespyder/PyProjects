$(function () {
    "use strict";
    
    $('#row2 .widget').equalHeight()
    $('#row3 .widget').equalHeight()
    $('#row4 .widget').equalHeight()
    
    /**
     *  TILES
     *  ======================================================================
     **/
    var looper = $('.looper')
    looper.each(function(){
        var $this = $(this),
            interval = ($this.attr('data-interval') == undefined)  ? 5000 : $this.attr('data-interval'),
            pause = ($this.attr('data-pause') == undefined)  ? 'hover' : $this.attr('data-pause'),
            speed = ($this.attr('data-speed') == undefined)  ? 500 : $this.attr('data-speed');

        $this.looper({
            interval : interval,
            pause :  '"' + pause + '"',
            speed : speed
        });
    })
    
    
    
    /**
     *  Charts
     *  ======================================================================
     **/
    // morris.js chart
    var sales_performce = function(){
        Morris.Area({
            element: 'sales-performance',
            data: [
                {period: '2012-07', targets: 2.5, achievement: 2},
                {period: '2012-08', targets: 3, achievement: 2.5},
                {period: '2012-09', targets: 4, achievement: 3},
                {period: '2012-10', targets: 6, achievement: 5.5},
                {period: '2012-11', targets: 6.5, achievement: 4},
                {period: '2012-12', targets: 5.5, achievement: 4.5},
                {period: '2013-01', targets: 4.5, achievement: 1.5},
                {period: '2013-02', targets: 15, achievement: 13},
                {period: '2013-03', targets: 10, achievement: 8},
                {period: '2013-04', targets: 10.5, achievement: 8},
                {period: '2013-05', targets: 12, achievement: 11},
                {period: '2013-06', targets: 8, achievement: 9}
            ],
            xkey: 'period',
            xLabels: 'month',
            ykeys: ['targets', 'achievement'],
            labels: ['Targets', 'Achievement'],
            pointSize: 2,
            hideHover: 'auto',
            gridTextColor: '#F3F3F3',
            yLabelFormat: function(y){
                return y.toString() + ' M'
            }
        });
    },
    sales_area = function(){
        Morris.Bar({
            element: 'sales-byarea',
            data: [
                {period: '2012-07', achievement: 830},
                {period: '2012-08', achievement: 745},
                {period: '2012-09', achievement: 973},
                {period: '2012-10', achievement: 548},
                {period: '2012-11', achievement: 998},
                {period: '2012-12', achievement: 840},
                {period: '2013-01', achievement: 639},
                {period: '2013-02', achievement: 658},
                {period: '2013-03', achievement: 890},
                {period: '2013-04', achievement: 857},
                {period: '2013-05', achievement: 975},
                {period: '2013-06', achievement: 648}
            ],
            xkey: 'period',
            ykeys: ['achievement'],
            labels: ['Achievement'],
            barRatio: 0.4,
            barColors: ['#647687'],
            gridTextColor: '#F3F3F3',
            hideHover: 'auto',
            yLabelFormat: function(y){
                return y.toString() + ' K'
            }
        });
    },
    employee_resume = function(){
        Morris.Donut({
            element: 'employee-resume',
            data: [
                {label: 'Achievement', value: 78 },
                {label: 'Target', value: 22 }
            ],
            formatter: function(y){
                return y + "%"
            },
            colors: ['#76608A', '#F0A30A'] // #D80073
        });
    },
    employee_progress = function(){
        Morris.Area({
            element: 'employee-progress',
            data: [
                {period: '2012-07', targets: 500, achievement: 658},
                {period: '2012-08', targets: 800, achievement: 745},
                {period: '2012-09', targets: 850, achievement: 973},
                {period: '2012-10', targets: 850, achievement: 548},
                {period: '2012-11', targets: 650, achievement: 998},
                {period: '2012-12', targets: 750, achievement: 840},
                {period: '2013-01', targets: 750, achievement: 639},
                {period: '2013-02', targets: 700, achievement: 658},
                {period: '2013-03', targets: 825, achievement: 890},
                {period: '2013-04', targets: 850, achievement: 857},
                {period: '2013-05', targets: 900, achievement: 975},
                {period: '2013-06', targets: 875, achievement: 680}
            ],
            xkey: 'period',
            ykeys: ['targets', 'achievement'],
            lineColors: ['#F0A30A', '#76608A'],
            labels: ['Targets', 'Achievement'],
            pointSize: 2,
            hideHover: 'auto',
            yLabelFormat: function(y){
                return y.toString() + ' K'
            }
        });
    };
    
    // call chart function
    sales_performce();
    sales_area();
    employee_resume();
    
    
    $('[data-toggle="tab"]').on('shown', function (e) {
        var active_tab = e.target.attributes.href.value;
        $('#employee-resume, #employee-progress').empty() // destroy charts
        
        if($(active_tab).is('#resumeStat')){
            employee_resume();
        }
        else if($(active_tab).is('#progressStat')){
            employee_progress();
        }
    })
    
    // control for responsive morris chart
    var redraw_charts = function(){
        $('#sales-performance, #sales-byarea, #employee-resume, #employee-progress').empty() // destroy charts
        sales_performce();
        sales_area();
        employee_resume();
        employee_progress();
    }
    $(window).resize(function(){
        redraw_charts()
    })
    // layout chage
    $('[name="layout-mode"]').on('change', function(){
        redraw_charts()
    })
    
    
    
    
    /* Sales employee datatable
    ----------------------------------------------------------------- */
    var oTable = $('#sale-employee').dataTable({
        "sDom": "<'row-fluid'<'span12'f>r>t<'row-fluid'<'span6'i><'span6'p>>",
        "iDisplayLength": 8
    })
    /* Add a click handler to the rows - this could be used as a callback */
    $("#sale-employee tbody tr").click( function( e ) {
        if ( $(this).hasClass('row_selected') ) {
            $(this).removeClass('row_selected');
        }
        else {
            oTable.$('tr.row_selected').removeClass('row_selected');
            $(this).addClass('row_selected');
        }
        
        // update chart
        var empl_name = $(this).find('td').eq(1).text()
        $('.employee-name').text(empl_name)
        
        // your other action, like updating chart via ajax or something else
        
    });
    
    
    /* Chat settings, scrollbar and more
    ----------------------------------------------------------------- */
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
                    +'<div class="messages bg-transparent">'
                    +'    <p class="color-white">'+ message +'</p>'
                    +'    <time class="color-white" datetime="2013-06-05T20:14">just now</time>' // just sample time, replace with your own value
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
                        +'<div class="messages bg-transparent">'
                        +'    <p class="color-white">Demo : just simple replay from other.</p>'
                        +'    <time class="color-white" datetime="2013-06-05T20:14">john doe | just now</time>' // just sample time, replace with your own value
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
    
    
    /* just initialize the calendar
    -----------------------------------------------------------------*/
    var date = new Date(),
    d = date.getDate(),
    m = date.getMonth(),
    y = date.getFullYear();
    
    $('#calendar').fullCalendar({
        header: {
            left: 'prev,next',
            center: 'title',
            right: 'today,month,agendaWeek,agendaDay'
        },
        editable: true,
        events: [
            {
                title: 'All Day Event',
                start: new Date(y, m, 1)
            },
            {
                title: 'Long Event',
                start: new Date(y, m, d-5),
                end: new Date(y, m, d-2)
            },
            {
                id: 999,
                title: 'Repeating Event',
                start: new Date(y, m, d-3, 16, 0),
                allDay: false
            },
            {
                id: 999,
                title: 'Repeating Event',
                start: new Date(y, m, d+4, 16, 0),
                allDay: false
            },
            {
                title: 'Meeting',
                start: new Date(y, m, d, 10, 30),
                allDay: false
            },
            {
                title: 'Lunch',
                start: new Date(y, m, d, 12, 0),
                end: new Date(y, m, d, 14, 0),
                allDay: false
            },
            {
                title: 'Birthday Party',
                start: new Date(y, m, d+1, 19, 0),
                end: new Date(y, m, d+1, 22, 30),
                allDay: false
            },
            {
                title: 'Click for stilearning',
                start: new Date(y, m, 28),
                end: new Date(y, m, 29),
                url: 'http://stilearning.com/'
            }
        ]
    })
    $('.fc-button-agendaWeek, .fc-button-agendaDay').on('click', function(){
        var selector = $('.fc-agenda-divider').next();
        $(selector).mCustomScrollbar("destroy");
        $(selector).mCustomScrollbar({
            autoHideScrollbar: true,    // boolean
            scrollButtons:{ enable: true, scrollSpeed: 60 },
            theme: 'light-thick'
        });
    })
    
    
    
});