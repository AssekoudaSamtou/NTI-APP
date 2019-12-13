$(document).ready(function () {

});

function supprimerOperation(url) {
    var form = document.getElementById("modifier_form");
    if(confirm('Voulez-vous vraiment supprimer cette opération financière ?')) {
        form.action = url;
        form.method = "POST";
        $(form).submit();
        return false;
    }
    return false;
}