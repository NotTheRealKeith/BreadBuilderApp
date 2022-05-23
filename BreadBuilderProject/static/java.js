console.log('javascript');

window.onload=function(){

  $(document).ready(function(){

    $("#thanks").hide();
    $(".rectanglecart").hide();
    $(".carti").click(function(){
      $(".rectanglecart").toggle();
    });

  });

  $.fn.outerHTML = function(){

    // IE, Chrome & Safari will comply with the non-standard outerHTML, all others (FF) will have a fall-back for cloning
    return (!this.length) ? this : (this[0].outerHTML || (
      function(el){
          var div = document.createElement('div');
          div.appendChild(el.cloneNode(true));
          var contents = div.innerHTML;
          div = null;
          return contents;
    })(this[0]));

  }

  // function createNav(id, content) {
  //       return `<head>
  //           <meta charset="utf-8">
  //           <meta name="viewport" content="width=device-width, initial-scale=1.0">
  //           <link rel="stylesheet" href="Styles/style.css">
  //           <link rel="stylesheet" href="Styles/loginstyle.css">
  //           <link rel="shortcut icon" href="images\logo.ico">
  //           <link href='http://fonts.googleapis.com/css?family=Lato&subset=latin,latin-ext' rel='stylesheet' type='text/css'>
  //           <link href="https://fonts.googleapis.com/css?family=Karla&display=swap" rel="stylesheet" />
  //           <title>BreadBuilder</title>
  //       </head>`;
  //   }
