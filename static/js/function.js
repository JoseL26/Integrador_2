function message_error(obj) {
    var html = '';
    if(typeof (obj) === 'object') {
        html = '<ul style="ext-align: left;">';
        $.each(obj, function (key, value) {
            html += '<li>'+key+value+'</li>';
        });
        html += '</ul>';
    }
    else {
        html = '<p>'+obj+'</p>';
    }
    html +='</ul>';
    Swal.fire({
        title: 'Error!',
        html: html,
        icon: 'error'
    });
}