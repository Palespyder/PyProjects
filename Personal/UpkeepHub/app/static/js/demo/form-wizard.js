$(function(){
    "use strict";
                
    // wizards demo
    // Example 1: Basic wizard with validation
    $('#with-progress1').click(function(){
        if($('#with-progress1:checked').is(':checked')){
            $("#wizard1").find('.progress').fadeIn();
        }
        else{
            $("#wizard1").find('.progress').fadeOut();
        }
    })
    $("#wizard1").wizard({
        animations: {
            show: {
                options: {
                    duration: 500
                },
                properties: {
                    opacity: "show"
                }
            }
        },
        stepsWrapper: "#wrapped1",
        submit: ".submit",
        beforeSelect: function( event, state ) {
            var inputs = $(this).wizard('state').step.find(':input');
            return !inputs.length || !!inputs.valid();
        },
        afterSelect: function( event, state ) {
            // progress
            // manual percentComplete value (sometime its have some bugs)
            if(state.percentComplete == Infinity || isNaN(state.percentComplete) == true){
                var total_steps = state.branchStepCount - 1,
                current_step = state.stepsActivated.length - 1;
                state.percentComplete = (current_step / total_steps) * 100;
            }
            $(this).find('.progress .bar').css("width", state.percentComplete + '%');
            
            // result
            if(state.isLastStep == true){
                var fields = $('#wrapped1').serializeArray();
                            
                $('#fname').text(fields[0].value)
                $('#lname').text(fields[1].value)
                $('#sgender').text(fields[2].value)
            }
        }
    }).wizard('form').submit(function( event ) {
        event.preventDefault();
        alert('Form submitted!');
    }).validate({
        errorPlacement: function(error, element) { 
            if ( element.is(':radio') || element.is(':checkbox') ) {
                error.insertAfter( element.parent().next() );
            } else { 
                error.insertAfter( element );
            }
        }
    });
    
    
    // wizard2
    // Example 1: Basic wizard with validation
    $('#with-progress2').click(function(){
        if($('#with-progress2:checked').is(':checked')){
            $("#wizard2").find('.progress').fadeIn();
        }
        else{
            $("#wizard2").find('.progress').fadeOut();
        }
    })
    $("#wizard2").wizard({
        animations: {
            show: {
                options: {
                    duration: 500
                },
                properties: {
                    opacity: "show"
                }
            }
        },
        stepsWrapper: "#wrapped2",
        submit: ".submit",
        beforeSelect: function( event, state ) {
            var inputs = $(this).wizard('state').step.find(':input');
            return !inputs.length || !!inputs.valid();
        },
        afterSelect: function( event, state ) {
            // progress
            // manual percentComplete value (sometime its have some bugs)
            if(state.percentComplete == Infinity || isNaN(state.percentComplete) == true){
                var total_steps = state.branchStepCount - 1,
                current_step = state.stepsActivated.length - 1;
                state.percentComplete = (current_step / total_steps) * 100;
            }
            $(this).find('.progress .bar').css("width", state.percentComplete + '%');
            
            // result
            if(state.isLastStep == true){
                var fields = $('#wrapped2').serializeArray();
                            
                $('#fname2').text(fields[0].value)
                $('#lname2').text(fields[1].value)
                $('#sgender2').text(fields[2].value)
            }
        }
    }).wizard('form').submit(function( event ) {
        event.preventDefault();
        alert('Form submitted!');
    }).validate({
        errorPlacement: function(error, element) { 
            if ( element.is(':radio') || element.is(':checkbox') ) {
                error.insertAfter( element.parent().next() );
            } else { 
                error.insertAfter( element );
            }
        }
    });
    
    
    
                
    
    // Example 2: Wizard style #1 with validation
    $('#wizard3').wizard({
        animations: {
            show: {
                options: {
                    duration: 500
                },
                properties: {
                    opacity: "show"
                }
            }
        },
        forward: ".next",
        backward: ".prev",
        stepsWrapper: "#wrapped3",
        submit: ".submit",
        beforeSelect: function( event, state ) {
            var inputs = $(this).wizard('state').step.find(':input');
            return !inputs.length || !!inputs.valid();
        },
        afterSelect: function( event, state ) {
            var current_step = state.stepsActivated.length - 1,
            wizard_steps = $(this).find('.wizard-steps li');
            
            if(state.isLastStep == true){
                wizard_steps.removeClass('active complete').find('.badge').removeClass('badge-info')
                wizard_steps.eq(current_step).addClass('complete').find('.badge').addClass('badge-info')
            }
            else{
                wizard_steps.removeClass('active complete').find('.badge').removeClass('badge-info')
                wizard_steps.eq(current_step).addClass('active').find('.badge').addClass('badge-info')
            }
        }
    }).wizard('form').submit(function( event ) {
        event.preventDefault();
        alert('Form submitted!');
    }).validate({
        errorElement: "small",
        errorPlacement: function(error, element){
            var controls = element.parent();
            if(controls.is('.controls')){
                error.appendTo( controls )
            }
            else{
                error.appendTo( controls.parent() )
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
            }
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
            email: "Please enter a valid email address"
        }
    });
    
    
    // wizard4
    $('#wizard4').wizard({
        animations: {
            show: {
                options: {
                    duration: 500
                },
                properties: {
                    opacity: "show"
                }
            }
        },
        forward: ".next",
        backward: ".prev",
        stepsWrapper: "#wrapped4",
        submit: ".submit",
        beforeSelect: function( event, state ) {
            var inputs = $(this).wizard('state').step.find(':input');
            return !inputs.length || !!inputs.valid();
        },
        afterSelect: function( event, state ) {
            var current_step = state.stepsActivated.length - 1,
            wizard_steps = $(this).find('.wizard-steps li');
            
            if(state.isLastStep == true){
                wizard_steps.removeClass('active complete').find('.badge').removeClass('badge-info')
                wizard_steps.eq(current_step).addClass('complete').find('.badge').addClass('badge-info')
            }
            else{
                wizard_steps.removeClass('active complete').find('.badge').removeClass('badge-info')
                wizard_steps.eq(current_step).addClass('active').find('.badge').addClass('badge-info')
            }
        }
    }).wizard('form').submit(function( event ) {
        event.preventDefault();
        alert('Form submitted!');
    }).validate({
        errorElement: "small",
        errorPlacement: function(error, element){
            var controls = element.parent();
            if(controls.is('.controls')){
                error.appendTo( controls )
            }
            else{
                error.appendTo( controls.parent() )
            }
            error.addClass('help-inline')
        },
        rules: {
            firstname2: "required",
            lastname2: "required",
            username2: {
                required: true,
                minlength: 2
            },
            password2: {
                required: true,
                minlength: 5
            },
            confirm_password2: {
                required: true,
                minlength: 5,
                equalTo: "#password2"
            },
            email2: {
                required: true,
                email: true
            }
        },
        messages2: {
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
            email: "Please enter a valid email address"
        }
    });
    
    
    
    
    // Example 3: Wizard style #2
    $('#nav-wizard1 li a').click(function(e){
        e.preventDefault();
    })
    $('#wizard5').wizard({
        animations: {
            show: {
                options: {
                    duration: 500
                },
                properties: {
                    opacity: "show"
                }
            }
        },
        afterSelect: function( event, state ) {
            var current_step = state.stepsActivated.length - 1,
            wizard_steps = $('#nav-wizard1 li');
            
            wizard_steps.removeClass('active')
            wizard_steps.eq(current_step).addClass('active')
        }
    }).wizard('form').submit(function( event ) {
        event.preventDefault();
        alert('Form submitted!');
    });
    
    
    // wizard6
    $('#nav-wizard2 li a').click(function(e){
        e.preventDefault();
    })
    $('#wizard6').wizard({
        animations: {
            show: {
                options: {
                    duration: 500
                },
                properties: {
                    opacity: "show"
                }
            }
        },
        afterSelect: function( event, state ) {
            var current_step = state.stepsActivated.length - 1,
            wizard_steps = $('#nav-wizard2 li');
            
            wizard_steps.removeClass('active')
            wizard_steps.eq(current_step).addClass('active')
        }
    }).wizard('form').submit(function( event ) {
        event.preventDefault();
        alert('Form submitted!');
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