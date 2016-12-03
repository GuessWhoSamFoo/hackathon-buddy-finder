(function($){
  $(function(){

    $('.button-collapse').sideNav();
    $("#detailView").modal({
      ready: function(modal, trigger) { // Callback for Modal open. Modal and trigger parameters available.
        console.log(modal, trigger);
      }
    });
    $("#createView").modal();

  }); // end of document ready
})(jQuery); // end of jQuery name space
