$('#addressTab').on('click', 'tr #addPhoneButton', function(e){

    function hasLetters(str){
        return /[a-zA-Z]/.test(str);
    }

    e.preventDefault();
    person_id = $(this).parent().closest('tr').data('contact-id');

    $(this).closest('tr').children("#phone").append("<input value='Wpisz nr tel.'><span class='clickable-check-icon'><i class='tiny material-icons'>check</i></span>");

     $('.clickable-check-icon').on('click',function(e){
        span = $(this);
        phone_input = $(this).siblings('input').last()
        phone = phone_input.val()
        if (hasLetters(phone))
            M.toast({html: 'Nr tel. nie może posiadać liter', classes: 'red rounded', displayLength:3000})
        else{
            $.ajax({
                url: '/phone_add/'+person_id+'/',
                method: 'POST',
                data: {
                    'phone': phone,
                },
                error: function(result){},
                success: function(result){
                M.toast({html: 'Telefon poprawnie dodany', classes: 'green rounded', displayLength:3000});
                    phone_input.prop('disabled', true);
                    span.hide();
                },
            });

        }
     });
});