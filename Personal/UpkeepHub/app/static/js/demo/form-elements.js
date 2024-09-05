$(function(){
    "use strict";
                
                
    // select2 demo 
    $('[data-fx="select2"]').each(function(){
        var $this = $(this),
        min_in = ($this.attr('data-min-input') == undefined) ? 0 : parseInt($this.attr('data-min-input'));
                    
        $this.select2({
            minimumInputLength : min_in
        })
    })
    // select2 tags mode demo
    $('[data-fx="select2-tags"]').select2({
        tags: ['@bent', '@Iin', 'stilearning']
    })
    // select2 dragdrop support demo
    $("#select2-dragdrop").select2({
        tags: ["red", "green", "blue", "orange", "white", "black", "purple", "cyan", "teal"]
    }).on("change", function() {
        $("#select2-dragdrop-val").html($("#select2-dragdrop").val());
    });
                
    $('#select2-dragdrop').select2("container").find("ul.select2-choices").sortable({
        containment: 'parent',
        start: function() {
            $("#select2-dragdrop").select2("onSortStart");
        },
        update: function() {
            $("#select2-dragdrop").select2("onSortEnd");
        }
    });
                
                
    // masked input demo
    $('[data-fx="masked"]').inputmask();
                
    // datepicker demo
    $('[data-fx="datepicker"]').datepicker();
                
    // timepicker demo
    $('[data-fx="timepicker"]').timepicker();
                
    // datetimepicker demo
    $('[data-fx="datetimepicker"]').datetimepicker({
        autoclose: true,
        todayBtn: true
    });
                
    // daterangepicker demo
    $('#daterangepicker').daterangepicker();
    $('#reportrange').daterangepicker({
        ranges: {
            'Today': [new Date(), new Date()],
            'Yesterday': [moment().subtract('days', 1), moment().subtract('days', 1)],
            'Last 7 Days': [moment().subtract('days', 6), new Date()],
            'Last 30 Days': [moment().subtract('days', 29), new Date()],
            'This Month': [moment().startOf('month'), moment().endOf('month')],
            'Last Month': [moment().subtract('month', 1).startOf('month'), moment().subtract('month', 1).endOf('month')]
        },
        opens: 'left',
        format: 'MM/DD/YYYY',
        separator: ' to ',
        startDate: moment().subtract('days', 29),
        endDate: new Date(),
        minDate: '01/01/2012',
        maxDate: '12/31/2013',
        locale: {
            applyLabel: 'Submit',
            fromLabel: 'From',
            toLabel: 'To',
            customRangeLabel: 'Custom Range',
            daysOfWeek: ['Su', 'Mo', 'Tu', 'We', 'Th', 'Fr','Sa'],
            monthNames: ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
            firstDay: 1
        },
        showWeekNumbers: true,
        buttonClasses: ['btn-danger'],
        dateLimit: false
    },
    function(start, end) {
        $('#reportrange .btn span').html(start.format('MMMM D, YYYY') + ' - ' + end.format('MMMM D, YYYY'));
    });
    //Set the initial state of the picker label
    $('#reportrange .btn span').html(moment().subtract('days', 29).format('MMMM D, YYYY') + ' - ' + moment().format('MMMM D, YYYY'));
                
    $('#daterangepicker2').daterangepicker({
        minDate: '01/01/2010',
        maxDate: '12/31/2015',
        showDropdowns: true
    });
    $('#daterangepicker3').daterangepicker({
        dateLimit: {
            days: 3
        }
    });
                
    
    // colorpicker demo
    $('[data-fx="colorpicker"]').colorpicker();
    
    
    
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
    })
});