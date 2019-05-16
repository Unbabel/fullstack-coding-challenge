$(document).ready(function () {
    toastr.options.positionClass = 'toast-bottom-right';
    toastr.options.closeButton = true;

    var arr_up = false;

    if (window.location.hash === '#success') {
        toastr.success("Successfully requested translation.");
    }

    else if (window.location.hash === '#deleted') {
        toastr.success("Successfully deleted translation.");
    }

    else if (window.location.hash === '#no-such-user') {
        toastr.error("There doesn't seem to be a user registered under that name/email.");
    }

    else if (window.location.hash === '#wrong-password') {
        toastr.error("The credentials you provided are not valid.");
    }

    else if (window.location.hash === '#unknown-error') {
        toastr.error("An unknown error occurred. Please contact the system's administrator.");
    }

    $('.delete-me').click(function () {

        var rowid = this.id;

        toastr.warning("<button type='button' id='confirmationRevertYes' class='btn clear table-head' style='margin-top:1vh; background-color:green'> Yes </button> <button type='button' id='confirmationRevertNo' class='btn clear table-head' style='margin-top:1vh; background-color:red'> No </button>", 'Are you sure you want to delete this translation?',
            {
                closeButton: true,
                allowHtml: true,
                onShown: function (toast) {
                    $("#confirmationRevertYes").click(function () {
                        $(location).attr('href', '/translation/delete/' + rowid);
                    });
                    $("#confirmationRevertNope").click(function () {
                        toastr.clear();
                    });
                }
            });
    });

    $('#reverse').on('click', function () {
        var tbody = $('table tbody');
        tbody.html($('tr', tbody).get().reverse());
        $('#arrow').text(arr_up ? 'arrow_downwards' : 'arrow_upwards');
        arr_up = !arr_up;
    });
});


function verifyFields() {

    var textToTranslate = document.getElementById("textToTranslate").value;
    var sourceLanguage = document.getElementById("sourceLanguage").value;
    var targetLanguage = document.getElementById("targetLanguage").value;


    if (textToTranslate === "") {
        toastr.error('The text field can\'t be empty!');
        return false;
    }

    if (sourceLanguage === "choose_a_language") {
        toastr.error('The source language field can\'t be empty!');
        return false;
    }

    if (targetLanguage === "choose_a_language") {
        toastr.error('The target language field can\'t be empty!');
        return false;
    }

    if (sourceLanguage === targetLanguage) {
        toastr.error('The target language can\'t be the same as the source language!');
        return false;
    }

    return true;
}