window.onload = function () {


    $('.button-collapse').sideNav();
    $("#detailView").modal({
      ready: function(modal, trigger) { // Callback for Modal open. Modal and trigger parameters available.
        console.log(modal, trigger);
      }
    });

    $("#createView").modal();

    Materialize.updateTextFields();

    $ideasContainer = $("#ideas");

    $.get( "/ideas", function( data ) {
      data.entries.forEach(function (idea) {
        var ideaHTML = generateIdeaRow(idea);
        $ideasContainer.append(ideaHTML);
      });
    });

    var ideaForm = $("#ideaForm");

    function generateIdeaRow(idea) {

        var tags = idea.tags.split(", ");

        var tagsHTML = "";

        tags.forEach(function (tag) {
            tagsHTML += '<div class="chip">' + tag + '</div>';
        });

        return `<div class="row">
                  <div class="col s12">
                    <div class="card blue-grey">
                      <a href="#detailView">

                        <div class="card-content white-text">
                          <span class="card-title">` + idea.project_name +`</span>
                          <p>` + idea.project_desc + `</p>
                        </div>

                        <div class="card-action">
                            ` + tagsHTML + `
                              <div class="chip orange white-text pull-right">` + idea.spots + ` Spots Remaining</div>
                        </div>
                      </a>
                    </div>
                  </div>
              </div>`;
    }

    $("#addIdea").on('click', function () {
      var formData = ideaForm.serialize();
      console.log(formData);
    });
};
