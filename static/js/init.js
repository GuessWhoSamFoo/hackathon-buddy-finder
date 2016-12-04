window.onload = function () {


    $('.button-collapse').sideNav();
    $("#detailView").modal({
      ready: function(modal, trigger) { // Callback for Modal open. Modal and trigger parameters available.
        console.log(modal, trigger);
      }
    });

    $("#createView").modal();

    Materialize.updateTextFields();

    $.get( "/ideas", function( data ) {
      data.entries.forEach(function (idea) {
        console.log(idea); // array of values
      });
    });

    var ideaForm = $("#ideaForm");

    $("#addIdea").on('click', function () {
      var formData = ideaForm.serialize();
      console.log(formData);
    });
};
