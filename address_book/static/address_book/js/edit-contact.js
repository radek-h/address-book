$(document).ready(function(){

    function hasNumbers(str){
        return /\d/.test(str);
    }
    function hasLetters(str){
        return /[a-zA-Z]/.test(str);
    }

    $(".clickable-edit-icon").on('click',function(e){
        e.preventDefault();

        var span = $(this);
        var icon = span.children();
        var input = span.siblings('input');

        input.prop('disabled', false);
        span.siblings(".clickable-check-icon").show();
        span.hide();
    });

     $('.clickable-check-icon').on('click',function(e){
        e.preventDefault();
        var data = {};
        var span = $(this);
        var input = span.siblings('input');
        var $row = span.closest('tr');
        var edit_id = $row.data('contact-id');

        data['first_name'] = $row.find('#first_name').children('input').val();
        data['last_name'] = $row.find('#last_name').children('input').val();

        if (data['first_name'].length == 0 || data['last_name'].length == 0)
             M.toast({html: 'Imię i nazwisko nie może być puste', classes: 'red rounded', displayLength:3000})
        if (hasNumbers(data['first_name']) || hasNumbers(data['last_name']))
             M.toast({html: 'Imię i nazwisko nie może posiadać cyfr', classes: 'red rounded', displayLength:3000})
        else{
            $.ajax({
                url: '/edit/'+edit_id+'/',
                method: 'POST',
                data: {
                    'first_name': data['first_name'],
                    'last_name': data['last_name'],
                },
                error: function(result){
                    M.toast({html: 'Kontakt niepoprawnie edytowany', classes: 'red rounded', displayLength:3000})},
                success: function(result){
                    M.toast({html: 'Kontakt poprawnie edytowany', classes: 'green rounded', displayLength:3000})
                    input.prop('disabled', true);
                    span.siblings(".clickable-edit-icon").show();
                    span.hide();
                },
            });
        }
     });
});

