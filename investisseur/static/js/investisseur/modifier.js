$(document).ready(function () {

});

function supprimerInvestisseur(url) {
    var form = document.getElementById("modifier_form");
    if(confirm('Voulez-vous vraiment supprimer cet investisseur ?')) {
        form.action = url;
        form.method = "POST";
        $(form).submit();
        return false;
    }
    return false;
}