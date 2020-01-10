$(document).ready(function () {

    $("#btn_avatar").click(function () {
        $("#id_avatar").trigger('click');
    });

    $("#id_avatar").change(function () {
        var files = this.files;
        if (files.length === 0) {
            console.log('No file is selected');
            return;
        }

        var reader = new FileReader();
        reader.onload = function(event) {
            console.log('File content:', event.target.result);
            $("#img_avatar").attr('src', event.target.result)
        };
        reader.readAsDataURL(files[0]);
    });

});

function supprimerTradeur(url) {
    var form = document.getElementById("modifier_form");
    if(confirm('Voulez-vous vraiment supprimer cet tradeur ?')) {
        form.action = url;
        form.method = "POST";
        $(form).submit();
        return false;
    }
    return false;
}