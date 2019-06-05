// Dodawanie buttonów dla usuwania i edycji wpisów

$('#addressTab tbody tr').each((i, el) => {
    tr = $(el);
    id = tr.data('contact-id');

    $("#actions", tr).append("<button id='addEmailButton' title='Dodaj email' class='btn-small'><i class='small material-icons' style='color:green'>contact_mail</i></button>");
    $("#actions", tr).append("<button id='addPhoneButton' title='Dodaj tel.' class='btn-small'><i class='tiny material-icons' style='color:green'>contact_phone</i></button>");

    phone_len = $(tr).children('#phone').children('input').length;
    email_len = $(tr).children('#email').children('input').length;
    console.log(phone_len, email_len)
    if (phone_len == 0 || email_len == 0){
        $("#actions", tr).append("<button id='deleteContactButton' title='Usuń wpis' class='btn-small'><i class='small material-icons' style='color:red'>delete</i></button>");
    }
});

