$(document).ready(function () {

    $("#id_comptes").bsMultiSelect();

    $("#id_balance_initialisation").keyup(function () {

        var objectif = parseFloat(this.value) * 2.5;
        $("#id_objectif").val(Math.round(objectif));
    });

});
