window.onload = function () {

    var cachedEntries;

    $('.button-collapse').sideNav();
    $("#detailView").modal({
      ready: function(modal, trigger) { // Callback for Modal open. Modal and trigger parameters available.
        console.log(modal, trigger);
        var id = $(trigger).find(".idea_id");
        console.log($(id).val());
      }
    });

    $("#createView").modal();

    Materialize.updateTextFields();

    $ideasContainer = $("#ideas");

    $.get( "/ideas", function( data ) {
      cachedEntries = data;
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
                <input class="idea_id" type="hidden" value="` + idea.id + `">
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
      var formData = JSON.stringify(ideaForm.serializeArray());
      console.log(formData);

      var data = {
          creator_name: $('#creator_name').val(),
          creator_role: $('#creator_role').val(),
          project_name: $('#project_name').val(),
          project_desc: $('#project_desc').val(),
          position_one: $('#position_one').val(),
          position_two: $('#position_two').val(),
          spots: 2,
          tags: $('#tags').val()
        }

        console.log(data);

      $.ajax({
          url: '/new',
          type: 'POST',
          data: data,
          success: function(result) {
              console.log(result);
          } //end success function(result)
        });
    });
};
