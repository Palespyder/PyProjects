$(function(){
    "use strict";
                
    // chart demo
    
    /**
     *  FLOT REAL TIME
     *  ======================================================================
     **/
    var data = [],
    totalPoints = 300,
    updateInterval = 300; // interval time

    function getRandomData() {
        if (data.length > 0) data = data.slice(1);

        // Do a random walk
        while (data.length < totalPoints) {
            var prev = data.length > 0 ? data[data.length - 1] : 50,
            y = prev + Math.random() * 10 - 5;

            if (y < 0) {
                y = 5;
            } else if (y > 50) {
                y = 50;
            }

            data.push(y);
        }

        // Zip the generated y values with the x values
        var res = [];
        for (var i = 0; i < data.length; ++i) {
            res.push([i, data[i]])
        }
        return res;
    }
    
    var plot_realtime = $.plot("#chart-realtime", 
    [{
            data :getRandomData(),
            color: '#1BA1E2'
    }], {
        legend: { show: false },
        xaxis: { show: false }, 
        yaxis: { show: false },
        series: {
            shadowSize: 0,	// Drawing is faster without shadows
            lines:{fill: 0.8}
        },
        grid: {
            backgroundColor: 'transparent',
            borderWidth: 0
        }
    }),
    update = function() {
        plot_realtime.setData( [{ data: getRandomData(), color: '#1BA1E2' }] );

        // Since the axes don't change, we don't need to call plot.setupGrid()
        plot_realtime.draw();
        setTimeout(update, updateInterval);
    };
    update()
    
    
    
    
    /**
     *  XCHARTS #1
     *  ======================================================================
     **/
    var xdata = [{"xScale":"ordinal","comp":[],"main":[{"className":".main.l1","data":[{"y":15,"x":"2012-11-19T00:00:00"},{"y":11,"x":"2012-11-20T00:00:00"},{"y":8,"x":"2012-11-21T00:00:00"},{"y":10,"x":"2012-11-22T00:00:00"},{"y":1,"x":"2012-11-23T00:00:00"},{"y":6,"x":"2012-11-24T00:00:00"},{"y":8,"x":"2012-11-25T00:00:00"}]},{"className":".main.l2","data":[{"y":29,"x":"2012-11-19T00:00:00"},{"y":33,"x":"2012-11-20T00:00:00"},{"y":13,"x":"2012-11-21T00:00:00"},{"y":16,"x":"2012-11-22T00:00:00"},{"y":7,"x":"2012-11-23T00:00:00"},{"y":18,"x":"2012-11-24T00:00:00"},{"y":8,"x":"2012-11-25T00:00:00"}]}],"type":"line-dotted","yScale":"linear"},{"xScale":"ordinal","comp":[],"main":[{"className":".main.l1","data":[{"y":12,"x":"2012-11-19T00:00:00"},{"y":18,"x":"2012-11-20T00:00:00"},{"y":8,"x":"2012-11-21T00:00:00"},{"y":7,"x":"2012-11-22T00:00:00"},{"y":6,"x":"2012-11-23T00:00:00"},{"y":12,"x":"2012-11-24T00:00:00"},{"y":8,"x":"2012-11-25T00:00:00"}]},{"className":".main.l2","data":[{"y":29,"x":"2012-11-19T00:00:00"},{"y":33,"x":"2012-11-20T00:00:00"},{"y":13,"x":"2012-11-21T00:00:00"},{"y":16,"x":"2012-11-22T00:00:00"},{"y":7,"x":"2012-11-23T00:00:00"},{"y":18,"x":"2012-11-24T00:00:00"},{"y":8,"x":"2012-11-25T00:00:00"}]}],"type":"cumulative","yScale":"linear"},{"xScale":"ordinal","comp":[],"main":[{"className":".main.l1","data":[{"y":12,"x":"2012-11-19T00:00:00"},{"y":18,"x":"2012-11-20T00:00:00"},{"y":8,"x":"2012-11-21T00:00:00"},{"y":7,"x":"2012-11-22T00:00:00"},{"y":6,"x":"2012-11-23T00:00:00"},{"y":12,"x":"2012-11-24T00:00:00"},{"y":8,"x":"2012-11-25T00:00:00"}]},{"className":".main.l2","data":[{"y":29,"x":"2012-11-19T00:00:00"},{"y":33,"x":"2012-11-20T00:00:00"},{"y":13,"x":"2012-11-21T00:00:00"},{"y":16,"x":"2012-11-22T00:00:00"},{"y":7,"x":"2012-11-23T00:00:00"},{"y":18,"x":"2012-11-24T00:00:00"},{"y":8,"x":"2012-11-25T00:00:00"}]}],"type":"bar","yScale":"linear"}],
    order = [0, 1, 0, 2],
    i = 0,
    xFormat = d3.time.format('%A'),
    chart = new xChart('line-dotted', xdata[order[i]], '#xchart', {
        axisPaddingTop: 5,
        dataFormatX: function (x) {
            return new Date(x);
        },
        tickFormatX: function (x) {
            return xFormat(x);
        },
        timing: 1250
    }),
    toggles = d3.selectAll('.multi button'),
    t = 3500,
    updateChart = function (i) {
        var d = xdata[i];
        chart.setData(d);
        toggles.classed('toggled', function () {
            return (d3.select(this).attr('data-type') === d.type);
        });
        return d;
    },
    rotateChart = function () {
        i += 1;
        i = (i >= order.length) ? 0 : i;
        var d = updateChart(order[i]);
        rotateTimer = setTimeout(rotateChart, t);
    },
    rotateTimer = setTimeout(rotateChart, t);
    
    
    
    
    /**
     *  EASY PIE CHART
     *  ======================================================================
     **/
    //create instance
    $('.chart-pie').easyPieChart({
        animate: 2000,
        size: 150
    });
    function randomUpdate(min, max){
        return Math.floor(Math.random() * (max-min+1) + min);
    }
    //update instance after 5 sec
    var updatepie = function() {
        $('.chart-pie').each(function(){
            var updateValue = randomUpdate(30, 95);
            $(this).data('easyPieChart').update(updateValue);
            $(this).find('.easypie-text').text(updateValue+'%')
        })
        setTimeout(updatepie, 7000);
    }
    updatepie()
    
    // custom easy pie
    $('#easypie-custom1').easyPieChart({
        animate: 2000,
        barColor: '#E51400',
        trackColor: '#f3f3f3',
        scaleColor: false,
        lineCap: 'butt',
        lineWidth: 20,
        size: 150
    })
    $('#easypie-custom2').easyPieChart({
        animate: 2000,
        barColor: '#76608A',
        trackColor: '#f3f3f3',
        scaleColor: '#dfe0e0',
        lineCap: 'round',
        lineWidth: 20,
        size: 150
    })
    $('#easypie-custom3').easyPieChart({
        animate: 2000,
        barColor: '#F472D0',
        trackColor: '#f3f3f3',
        scaleColor: false,
        lineCap: 'square',
        lineWidth: 20,
        size: 150
    })
    $('#easypie-custom4').easyPieChart({
        animate: 2000,
        barColor: '#E3C800',
        trackColor: '#f3f3f3',
        scaleColor: '#dfe0e0',
        lineCap: 'round',
        lineWidth: 20,
        size: 150
    })
    
});