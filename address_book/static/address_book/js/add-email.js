$('#addressTab').on('click', 'tr #addEmailButton', function(e){

    function isEmail(email) {
        var regex = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;
        return regex.test(email);
    }

    e.preventDefault();
    person_id = $(this).parent().closest('tr').data('contact-id');

    $(this).closest('tr').children("#email").append("<input value='Wpisz mail'><span class='clickable-check-icon'><i class='tiny material-icons'>check</i></span>");

     $('.clickable-check-icon').on('click',function(e){
        span = $(this);
        email_input = span.siblings('input').last()
        email = email_input.val()
        if (!isEmail(email))
             M.toast({html: 'Wpisz poprawny adres email', classes: 'red rounded', displayLength:3000})
        else
            $.ajax({
                url: '/email_add/'+person_id+'/',
                method: 'POST',
                data: {
                    'email': email,
                },
                error: function(result){},
                success: function(result){
                    M.toast({html: 'Email poprawnie dodany', classes: 'green rounded', displayLength:3000});
                    email_input.prop('disabled', true);
                    console.log(span)
                    span.hide();
                },
            });
        });
    });