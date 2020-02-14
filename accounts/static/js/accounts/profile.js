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
