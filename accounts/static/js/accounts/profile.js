function hidePassword() {
    var pass = $("#hidden_password").text(), res = "";
    for (char in pass) {
        res += "*";
    }
    console.log("xxxxxx");
    $("#toggle-possword-icon").removeClass("fa-eye-slash");
    $("#toggle-possword-icon").addClass("fa-eye");
    $("#toggle-possword-icon").attr('onclick', 'showPassword()');
    $("#hidden_password").text(res);
}

function showPassword() {
    var pass = $("#hidden_password").text("my_password");
    $("#toggle-possword-icon").removeClass("fa-eye");
    $("#toggle-possword-icon").addClass("fa-eye-slash");
    $("#toggle-possword-icon").attr('onclick', 'hidePassword()');
}

function persistAvatar() {
    var form = $("#avatar_form")[0],
        data = new FormData();

    var xhr = new XMLHttpRequest();
    xhr.open("POST", form.action);
    xhr.onload = function() {
        console.log("success");
    };
    xhr.onerror = function() {
        console.log("error");
    };
    xhr.send(data);
}

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
            // console.log('File content:', event.target.result);
            $("#img_avatar").attr('src', event.target.result);

            persistAvatar();
        };
        reader.readAsDataURL(files[0]);
    });

});
