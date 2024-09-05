$(function(){
    "use strict";
                
    // chart demo
    
    /**
     *  CHART BAR #1
     *  ======================================================================
     **/
    var hist = [ ['Joe', 1.62], ['Jay', 1.63], ['Jen', 1.71], ['Jane', 1.66], ['John', 1.79], ['Jone', 1.58], ['Jake', 1.55],  ['Jule', 1.62],  ['Jack', 1.72] ],
    plot1 = $.plot("#chart-bar-1", [{
        data : hist,
        label : 'Histogram',
        color: '#1BA1E2'
    }],
    {
        legend: { show: false },
        xaxis: { mode: "categories", tickLength: 0 },
        yaxis: { show: false },
        series: {
            bars: {
                show: true,
                barWidth: 0.6,
                fill: 0.8,
                align: "center"
            }
        },
        grid: {
            hoverable: true,
            clickable: true,
            backgroundColor: 'transparent',
            borderWidth: 0
        }
    });
    
    
    
    /**
     *  CHART BAR #2
     *  ======================================================================
     **/
    var item_1 = [ ['Day 1', 10], ['Day 2', 15], ['Day 3', 12], ['Day 4', 20], ['Day 5', 21], ['Day 6', 17] ],
        item_2 = [ ['Day 1', 5], ['Day 2', 10], ['Day 3', 8], ['Day 4', 12], ['Day 5', 16], ['Day 6', 13] ],
        item_3 = [ ['Day 1', 5], ['Day 2', 8], ['Day 3', 3], ['Day 4', 8], ['Day 5', 11], ['Day 6', 8] ],
    
    plot2 = $.plot("#chart-bar-2", [
        { data : item_1, color : '#1BA1E2', label : 'FirstTime'},
        { data : item_2, color : '#647687', label : 'Return' },
        { data : item_3, color : '#323232', label : 'Purchase' }
    ], 
    {
        legend: { show: false },
        xaxis: { mode: "categories", tickLength: 0},
        yaxis: { show: false },
        series: {
            stack: true,
            bars: {
                show: true,
                barWidth: 0.6,
                fill: 0.9,
                align: "center"
            }
        },
        grid: {
            hoverable: true,
            clickable: true,
            borderWidth: 0
        }
    });
    
    
    
    /**
     *  CHART BAR #3
     *  ======================================================================
     **/
    var d1 = [];
    for (var i = 0; i < 20; ++i) {
        d1.push([i, Math.sin(i)]);
    }
    var data = [{ data: d1, label: "Pressure", color: "#FFFFFF" }],
        markings = [
        { color: "#F3F3F3", yaxis: { from: 1 } },
        { color: "#F3F3F3", yaxis: { to: -1 } },
        { color: "#000", lineWidth: 1, xaxis: { from: 2, to: 2 } },
        { color: "#000", lineWidth: 1, xaxis: { from: 8, to: 8 } }
    ];

    var placeholder = $("#chart-bar-3");

    var plot = $.plot(placeholder, data, {
        legend: { show: false },
        bars: { show: true, barWidth: 0.5, fill: 0.9 },
        xaxis: { show: false },
        yaxis: { min: -2, max: 2, font: {color: '#FFFFFF'} },
        grid: { 
            markings : markings,
            hoverable: true,
            clickable: true,
            borderWidth: 0
        }
    });
    
    var o = plot.pointOffset({ x: 2, y: -1.2});

    // Append it to the placeholder that Flot already uses for positioning
    placeholder.append("<div style='position:absolute;left:" + (o.left + 4) + "px;top:" + o.top + "px;color:#666;font-size:smaller'>Warming up</div>");

    o = plot.pointOffset({ x: 8, y: -1.2});
    placeholder.append("<div style='position:absolute;left:" + (o.left + 4) + "px;top:" + o.top + "px;color:#666;font-size:smaller'>Actual measurements</div>");

    // Draw a little arrow on top of the last label to demonstrate canvas
    // drawing
    var ctx = plot.getCanvas().getContext("2d");
    ctx.beginPath();
    o.left += 4;
    ctx.moveTo(o.left, o.top);
    ctx.lineTo(o.left, o.top - 10);
    ctx.lineTo(o.left + 10, o.top - 5);
    ctx.lineTo(o.left, o.top);
    ctx.fillStyle = "#000";
    ctx.fill();



    
    /**
     *  HELP TOOLTIPS
     *  ======================================================================
     **/
    var showTooltip = function(x, y, contents) {
        $("<div id='tooltip' class='flot-tooltip'>" + contents + "</div>").css({
            top: y + 20,
            left: x - 50
        }).appendTo("body").fadeIn(200);
    }
    $("#chart-bar-1, #chart-bar-2, #chart-bar-3").bind("plothover", function (event, pos, item) {
        var previousPoint = null;
        if(item){
            if (previousPoint != item.dataIndex) {

                previousPoint = item.dataIndex;

                $("#tooltip").remove();
                
                var datapointX = item.datapoint[0], 
                x = item.series.data[datapointX][0],
                y = item.datapoint[1].toFixed(2);
                
                showTooltip(item.pageX, item.pageY,
                    item.series.label + " of " + x + " = " + y);
            }
        } else {
            $("#tooltip").remove();
            previousPoint = null;            
        }
    });
    
    
    
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
        else if(theme == 'magenta'){ colorhex = '#D80073' }
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
        
        plot1.setData([{
            data : hist,
            label : 'Histogram',
            color: colorhex
        }])
        plot1.draw()
        
        plot2.setData([
            { data : item_1, color : colorhex, label : 'FirstTime'},
            { data : item_2, color : '#647687', label : 'Return' },
            { data : item_3, color : '#323232', label : 'Purchase' }
        ])
        plot2.draw()
    })
});