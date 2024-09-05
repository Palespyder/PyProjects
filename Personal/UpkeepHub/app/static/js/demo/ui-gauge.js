$(function () {
    "use strict";


    // justgage demo
    var g1 = new JustGage({
        id: "gauge1",
        relativeGaugeSize: true, // responsive option set
        value: 648,
        min: 0,
        max: 1000,
        title: "Visitors",
        titleFontColor: '#f3f3f3',
        label: "per minute",
        labelFontColor: '#f3f3f3',
        valueFontColor: '#f3f3f3',
        levelColors: ['#00ABA9'],
        levelColorsGradient: false
    });
    var g2 = new JustGage({
        id: "gauge2",
        relativeGaugeSize: true, // responsive option set
        value: 38,
        min: 0,
        max: 100,
        gaugeWidthScale: 0.5,
        title: "Errors",
        titleFontColor: '#f3f3f3',
        label: "average",
        labelFontColor: '#f3f3f3',
        valueFontColor: '#f3f3f3',
        levelColors: ['#E51400'],
        levelColorsGradient: false
    });
    var g3 = new JustGage({
        id: "gauge3",
        relativeGaugeSize: true, // responsive option set
        value: 30,
        min: 0,
        max: 60,
        gaugeWidthScale: 0.7,
        title: "Timers",
        titleFontColor: '#f3f3f3',
        labelFontColor: '#f3f3f3',
        valueFontColor: '#f3f3f3',
        levelColors: ['#F0A30A'],
        levelColorsGradient: false,
        gaugeColor: '#999999'
    });
    var g4 = new JustGage({
        id: "gauge4",
        relativeGaugeSize: true, // responsive option set
        value: randomUpdate(10, 100),
        min: 10,
        max: 100,
        gaugeWidthScale: 0.2,
        title: "Events",
        titleFontColor: '#f3f3f3',
        labelFontColor: '#f3f3f3',
        valueFontColor: '#f3f3f3',
        levelColors: ['#323232'],
        levelColorsGradient: false
    });

    function randomUpdate(min, max) {
        return Math.floor(Math.random() * (max - min + 1) + min);
    }
    setInterval(function () {
        g1.refresh(randomUpdate(100, 1000));
        g2.refresh(randomUpdate(20, 100));
        g3.refresh(randomUpdate(10, 60));
        g4.refresh(randomUpdate(20, 100));
    }, 5000)


    // knob demo
    $('[data-chart="knob"]').knob({
        "inputColor ": "inherit ",
        "skin ": "tron ",
        'width' : '150',
        'height' : '150',
        draw: function () {
            
            // "tron"  case
            if(this.$.data('skin') == 'tron') {

                var a = this.angle(this.cv)  // Angle
                    , sa = this.startAngle          // Previous start angle
                    , sat = this.startAngle         // Start angle
                    , ea                            // Previous end angle
                    , eat = sat + a                 // End angle
                    , r = 1;

                this.g.lineWidth = this.lineWidth;

                this.o.cursor
                    && (sat = eat - 0.3)
                    && (eat = eat + 0.3);

                if (this.o.displayPrevious) {
                    ea = this.startAngle + this.angle(this.v);
                    this.o.cursor
                        && (sa = ea - 0.3)
                        && (ea = ea + 0.3);
                    this.g.beginPath();
                    this.g.strokeStyle = this.pColor;
                    this.g.arc(this.xy, this.xy, this.radius - this.lineWidth, sa, ea, false);
                    this.g.stroke();
                }

                this.g.beginPath();
                this.g.strokeStyle = r ? this.o.fgColor : this.fgColor ;
                this.g.arc(this.xy, this.xy, this.radius - this.lineWidth, sat, eat, false);
                this.g.stroke();

                this.g.lineWidth = 2;
                this.g.beginPath();
                this.g.strokeStyle = this.o.fgColor;
                this.g.arc( this.xy, this.xy, this.radius - this.lineWidth + 1 + this.lineWidth * 2 / 3, 0, 2 * Math.PI, false);
                this.g.stroke();

                return false;
            }
        }
    })
});