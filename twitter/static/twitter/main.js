function showusers() {
    jQuery.ajax({
        url: '/get_users/',
        type: "GET",
        dataType: "html",
        success: function (response) {
            document.getElementById("showUsers").innerHTML = response;
        },
        error: function (response) {
            document.getElementById("showUsers").innerHTML = "LAL";
        }
    });
    return false;
}
