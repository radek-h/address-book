$('#addressTab').on('click', 'tr #deleteContactButton', function(e){
    e.preventDefault();
    delete_id = $(this).parent().closest('tr').data('contact-id');
    tr = $(this).closest('tr');
    $.ajax({
        url: 'delete/'+delete_id+'/',
        method: 'DELETE',
        data: {},
        contentType:'application/json',
        dataType: 'text',
        error: function(result){
            M.toast({html: 'Wpis niepoprawnie usunięty', classes: 'red rounded', displayLength:3000})
        },
        success: function(result) {
            tr.remove();
            M.toast({html: 'Wpis poprawnie usunięty', classes: 'green rounded', displayLength:3000})
        }
    });
});