(function($){
  $(function(){

    function getInitialPosts() {

      return [
        {
          author: "Bogdan P",
          project_name: "Uber For Fish",
          project_desc: "Fish need to go places too!",
          tags: [
            "PHP",
            "SQL"
          ],
          stops_left: 4
        }
      ];
    }

    var posts = getInitialPosts;

    $('.button-collapse').sideNav();
    $("#detailView").modal({
      ready: function(modal, trigger) { // Callback for Modal open. Modal and trigger parameters available.
        console.log(modal, trigger);
      }
    });

    $("#createView").modal();

  }); // end of document ready
})(jQuery); // end of jQuery name space

$(document).ready(function () {
    Materialize.updateTextFields();

    var ideaForm = $("#ideaForm");

    $("#addIdea").on('click', function () {
      var formData = ideaForm.serialize();
      console.log(formData);
    });
});
