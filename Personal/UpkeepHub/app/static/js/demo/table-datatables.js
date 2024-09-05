$(function(){
    'use strict';
    
    
    /* Table #1 initialisation */
    $('#datatables1').dataTable({
        "bProcessing": true,
        "sAjaxSource": 'js/datatables/objects.txt',
        "aoColumns": [
            { "mData": "engine" },
            { "mData": "browser" },
            { "mData": "platform" },
            { "mData": "version" },
            { "mData": "grade" }
        ]
    });
    
    
    /* Table #2 initialisation */
    $('#datatables2').dataTable({
        "sDom": "<'row-fluid'<'span6'T><'span6'f>r>t<'row-fluid'<'span6'i><'span6'p>>",
        "bProcessing": true,
        "sAjaxSource": 'js/datatables/objects.txt',
        "aoColumns": [
            { "mData": "engine" },
            { "mData": "browser" },
            { "mData": "platform" },
            { "mData": "version" },
            { "mData": "grade" }
        ],
        "oTableTools": {
            "aButtons": [
                "copy",
                "print",
                "pdf",
                "csv"
            ],
            "sSwfPath": "js/datatables/tabletools/swf/copy_csv_xls_pdf.swf"
        }
    });
    
    
    /* Table #3 initialisation */
    $('#datatables3').dataTable({
        "bProcessing": true,
        "sAjaxSource": 'js/datatables/objects.txt',
        "aoColumns": [
            { "mData": "engine" },
            { "mData": "browser" },
            { "mData": "platform" },
            { "mData": "version" },
            { "mData": "grade" }
        ],
        // include colReorder (R) and filter collumn (C)
        "sDom": "RC<'clearfix'>'<'row-fluid'<'span6'l><'span6'f>r>t<'row-fluid'<'span6'i><'span6'p>>",
        // hide column index[2] by default
        "aoColumnDefs": [
            { "bVisible": false, "aTargets": [ 2 ] }
        ],
        "oLanguage": {
            "sSearch": "Search:"
        },
        "bSortCellsTop": true
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
    })
})