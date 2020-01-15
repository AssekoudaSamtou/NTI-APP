$(document).ready(function () {

    function buildUsername() {
        var nom = $("#id_first_name").val(),
            prenom = $("#id_last_name").val();

        $("#id_username").val(nom.trim() + '_' + prenom.trim());
    }

    $(".names").change(function () {
        buildUsername();
    }).keyup(function () {
        buildUsername();
    });


});