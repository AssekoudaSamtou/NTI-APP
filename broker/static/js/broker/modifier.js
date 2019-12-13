$(document).ready(function () {

});

function supprimerBoker(url) {
    var form = document.getElementById("modifier_form");
    if(confirm('Voulez-vous vraiment supprimer cet broker ?')) {
        form.action = url;
        form.method = "POST";
        $(form).submit();
        return false;
    }
    return false;
}