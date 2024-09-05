$(function(){
    "use strict";
                
    // code editor demo 
    // select2
    $('[data-form=select2]').select2();
                
    // mode name list
    var modesByName = {
        asciidoc:   ["AsciiDoc"     , "asciidoc"],
        c9search:   ["C9Search"     , "c9search_results"],
        coffee:     ["CoffeeScript" , "coffee|^Cakefile"],
        coldfusion: ["ColdFusion"   , "cfm"],
        csharp:     ["C#"           , "cs"],
        css:        ["CSS"          , "css"],
        diff:       ["Diff"         , "diff|patch"],
        glsl:       ["Glsl"         , "glsl|frag|vert"],
        golang:     ["Go"           , "go"],
        groovy:     ["Groovy"       , "groovy"],
        haxe:       ["haXe"         , "hx"],
        html:       ["HTML"         , "htm|html|xhtml"],
        c_cpp:      ["C/C++"        , "c|cc|cpp|cxx|h|hh|hpp"],
        clojure:    ["Clojure"      , "clj"],
        jade:       ["Jade"         , "jade"],
        java:       ["Java"         , "java"],
        jsp:        ["JSP"                , "jsp"],
        javascript: ["JavaScript"   , "js"],
        json:       ["JSON"         , "json"],
        jsx:        ["JSX"          , "jsx"],
        latex:      ["LaTeX"        , "latex|tex|ltx|bib"],
        less:       ["LESS"         , "less"],
        liquid:     ["Liquid"       , "liquid"],
        lua:        ["Lua"          , "lua"],
        luapage:    ["LuaPage"      , "lp"], // http://keplerproject.github.com/cgilua/manual.html#templates
        markdown:   ["Markdown"     , "md|markdown"],
        ocaml:      ["OCaml"        , "ml|mli"],
        perl:       ["Perl"         , "pl|pm"],
        pgsql:      ["pgSQL"        , "pgsql"],
        php:        ["PHP"          , "php|phtml"],
        powershell: ["Powershell"   , "ps1"],
        python:     ["Python"       , "py"],
        ruby:       ["Ruby"         , "ru|gemspec|rake|rb"],
        scad:       ["OpenSCAD"     , "scad"],
        scala:      ["Scala"        , "scala"],
        scss:       ["SCSS"         , "scss|sass"],
        sh:         ["SH"           , "sh|bash|bat"],
        sql:        ["SQL"          , "sql"],
        svg:        ["SVG"          , "svg"],
        tcl:        ["Tcl"          , "tcl"],
        text:       ["Text"         , "txt"],
        textile:    ["Textile"      , "textile"],
        typescript: ["Typescript"   , "typescript|ts|str"],
        xml:        ["XML"          , "xml|rdf|rss|wsdl|xslt|atom|mathml|mml|xul|xbl"],
        xquery:     ["XQuery"       , "xq"],
        yaml:       ["YAML"         , "yaml"]
    };
                
    // define editor
    var editor = ace.edit("editor");
    editor.getSession().setMode("ace/mode/javascript");
                
    // append mode
    $.each(modesByName, function(k, v){
        $('#mode').append('<option value="'+k+'">'+v[0]+'</option>'); // if you use chosen you need update list .trigger("liszt:updated");
    })
                
    $('#data-files').change(function(){
        var url = 'js/ace-editor/file-changer.php',
        value = $(this).val();
        $.post(url, {
            data:value
        }, function(o){
            if(o == '0'){
                alert('file not found, may be broken.')
            }
            else{
                editor.setValue(o, 0);
            }
        })
                    
    })
    $('#mode').change(function(){
        var mode = $(this).val();
        editor.getSession().setMode("ace/mode/"+mode+"");
    })
    $('#theme').change(function(){
        var theme = $(this).val();
        editor.setTheme(theme);
    })
    $('#update').click(function(){
        alert('action update here... :)')
        return false;
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
        
    })
});