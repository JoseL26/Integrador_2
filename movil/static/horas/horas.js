var horas = {
    items : {
        Empleado: '',
        fecha: '',
        TotalHoras: 0.00,
        actividades:[]
    },
    add: function(){
    }
};

$(function () {
    $('.select2').select2({
        theme: "bootstrap4",
        language: 'es'
    });

    $('#fecha').datetimepicker({
        format: 'DD-MM-YYYY',
        date: moment().format("DD-MM-YYYY"),
        locale: 'es'
    });

    //busqueda de equipos
     $('input[name="buscar"]').autocomplete({
        source: function(request, response){
            $.ajax({
                url: window.location.pathname,
                type: 'POST',
                data: {
                    'action': 'buscar_productos',
                    'term': request.term
                },
                dataType: 'json'
            }).done(function (data) {
                response(data);
            }).fail(function (jqXHR, textStatus, errorThrown) {
                //alert(textStatus + ': ' + errorThrown);
            }).always(function (data) {

            });
        },
           delay: 500,
           minLength: 1,
           select: function(event, ui){
            console.log(ui.item);
           }
     });
});