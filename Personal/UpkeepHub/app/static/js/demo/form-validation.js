$.validator.setDefaults({
    submitHandler: function() {
        alert("submitted!");
    }
})

// handle for dynamic form
$.validator.messages.max = jQuery.validator.format("Your totals mustn't exceed {0}!");
$.validator.addMethod("quantity", function(value, element) {
    return !this.optional(element) && !this.optional($(element).prev("select")[0]); // find the select element
}, "Please select both the item and its amount.")

$(function(){
    "use strict";
                
    // form validate demo 
    // validate the comment form when it is submitted
    $("#commentForm").validate({
        errorElement: "small",
        errorPlacement: function(error, element){
            error.appendTo( element.parent() )
            error.addClass('help-block')
        }
    })
                
    // validate fileupload, required additional-methods.js
    $("#fileForm").validate({
        errorElement: "small",
        errorPlacement: function(error, element){
            var parent = element.parent();
                        
            if(parent.is('.controls')){
                error.appendTo( parent )
            }
            else if(parent.parent().is('.controls')){
                error.appendTo( parent.parent() )
            }
            else if(parent.parent().parent().is('.controls')){
                error.appendTo( parent.parent().parent() )
            }
            else{
                error.appendTo( parent.parent().parent().parent() )
            }
            error.addClass('help-block')
        }
    });
    
    // validate signup form on keyup and submit
    $("#signupForm").validate({
        errorElement: "small",
        errorPlacement: function(error, element){
            var parent = element.parent();
                        
            if(parent.is('.controls')){
                error.appendTo( parent )
            }
            else{
                error.appendTo( parent.parent() )
            }
                        
            error.addClass('help-inline')
        },
        rules: {
            firstname: "required",
            lastname: "required",
            username: {
                required: true,
                minlength: 2
            },
            password: {
                required: true,
                minlength: 5
            },
            confirm_password: {
                required: true,
                minlength: 5,
                equalTo: "#password"
            },
            email: {
                required: true,
                email: true
            },
            topic: {
                required: "#newsletter:checked",
                minlength: 2
            },
            agree: "required"
        },
        messages: {
            firstname: "Please enter your firstname",
            lastname: "Please enter your lastname",
            username: {
                required: "Please enter a username",
                minlength: "Your username must consist of at least 2 characters"
            },
            password: {
                required: "Please provide a password",
                minlength: "Your password must be at least 5 characters long"
            },
            confirm_password: {
                required: "Please provide a password",
                minlength: "Your password must be at least 5 characters long",
                equalTo: "Please enter the same password as above"
            },
            email: "Please enter a valid email address",
            agree: "Please accept our policy"
        }
    })
    // propose username by combining first- and lastname
    $("#username").focus(function() {
        var firstname = $("#firstname").val();
        var lastname = $("#lastname").val();
        if(firstname && lastname && !this.value) {
            this.value = firstname + "." + lastname;
        }
    })
    //code to hide topic selection, disable for demo
    var newsletter = $("#newsletter");
    // newsletter topics are optional, hide at first
    var inital = newsletter.is(":checked");
    var topics = $("#newsletter_topics")[inital ? "removeClass" : "addClass"]("color-silver");
    var topicInputs = topics.find("input").attr("disabled", !inital);
    // show when newsletter is checked
    newsletter.click(function() {
        topics[this.checked ? "removeClass" : "addClass"]("color-silver");
        topicInputs.attr("disabled", !this.checked);
    })
    
    // validate dynamic form
    $("#orderform").validate({
        errorClass: 'border-red',
        validClass: '',
        focusCleanup: true,
        errorPlacement: function(error, element) {
            error.appendTo( element.parent() );
        },
        highlight: function(element, errorClass) {
            // find the select element
            $(element).addClass(errorClass).prev("select").addClass(errorClass);
        }
    });

    var template = jQuery.validator.format($.trim($("#template").val()));
    function addItem() {
        $("#orderitems-totals").before(template(i++));
        $('[data-fx="select2"]').select2()
    }

    var i = 1;
    // start with one row
    addItem();
    // add more rows on click
    $("#add").click(addItem);

    // check keyup on quantity inputs to update totals field
    $("#orderform").validateDelegate("input.quantity", "keyup", function(event) {
        var totals = 0;
        $("#orderform input.quantity").each(function() {
            totals += +this.value;
        });
        $("#totals").attr("value", totals).valid();
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
});