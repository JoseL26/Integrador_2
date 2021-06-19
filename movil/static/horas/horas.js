
$(function () {

    const horas = {
        items : {
            Empleado: '',
            fecha: '',
            TotalHoras: 0.00,
            activity: []
        },
    };

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
                dataType: 'json',
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
            event.preventDefault();
            
            const item = ui.item;
         //   horas.items.activity.push(item);
           // console.log(horas);
            const table = document.getElementById('tbdeth')
            table.insertRow(-1).innerHTML = `
                <td>
                    <button type="button" onclick="eliminar(this)" class="btn btn-danger btn-xs btn-flat">
                        <span class="las la-trash"></span>
                    </button>
                </td>
                <td>${item.id}</td>
                <td>${item.Cod_equipo}</td>
                <td><input type="text" class="form-control"></td>
                <td><input type="text" class="form-control"></td>
                <td><input type="number" class="form-control" oninput="calcular()" value="0" id = "idcampo_${item.id}" name = "ncampo_${item.id}"></td>
            `;


        }
    });
});