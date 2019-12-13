$(document).ready(function () {

});

function supprimerCommercial(url) {
    var form = document.getElementById("modifier_form");
    if(confirm('Voulez-vous vraiment supprimer cet commercial ?')) {
        form.action = url;
        form.method = "POST";
        $(form).submit();
        return false;
    }
    return false;
}