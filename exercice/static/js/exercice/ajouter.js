$(document).ready(function () {

    $("#id_balance_initialisation").keyup(function () {
        // console.log(this.value);
        var objectif = parseFloat(this.value) * 2.5;
        $("#id_objectif").val(objectif);
    });

});