<<<<<<< HEAD
var tblOrdens;
var tareas = {
    items : {
        Empleado: '',
        fecha: '',
        TotalHoras: 0.00,
        actividades:[]
    },
    calculo_total: function(){
        var subtotal =0.00;
        $.each(this.items.actividades, function(pos, dict){
            dict.pos = pos;
            subtotal += dict.Cantidad;
        });
        //console.log(subtotal);
        this.items.TotalHoras=subtotal;
        $('input[name="TotalHoras"]').val(this.items.TotalHoras.toFixed(2));
    },
    add: function(item){
        this.items.actividades.push(item);
        this.list();
    },
    list: function(){
    this.calculo_total();
        tblOrdens = $('#tblorden').DataTable({
            responsive: true,
            autoWidth: false,
            destroy: true,
            data: this.items.actividades,
            columns: [
                {"data": "Orden"},
                {"data": "Orden"},
                {"data": "equipo.Cod_equipo"},
                {"data": "operacion"},
                {"data": "desc_actividad"},
                {"data": "Cantidad"},

            ],
            columnDefs: [
                {
                    targets: [0],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<a rel="remove" class="btn btn-danger btn-xs btn-flat"><i class="las la-trash"></i></a>';

                    }
                },
                {
                    targets: [-3],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="text" name="operacion" class="form-control form-control-sm" autocomplete="off" value="'+row.operacion+'">';

                    }
                },
                {
                    targets: [-2],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="text" name="desc_actividad" class="form-control form-control-sm" autocomplete="off" value="'+row.desc_actividad+'">';
                    }
                },
                {
                    targets: [-1],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="text" name="Cantidad" class="form-control form-control-sm" autocomplete="off" value="'+row.Cantidad+'">';
                    }
                },

            ],
            rowCallback(row, data, displayNum, displayIndex, dataIndex){
               $(row).find('input[name="Cantidad"]').TouchSpin({
                    min: 1,
                    max: 1000000000,
                    step: 1
               });
               $(row).find('input[name="operacion"]').TouchSpin({
                    min: 10,
                    max: 1000000000,
                    step: 10
               });

            },
            initComplete: function (settings, json) {

            }
        });
    },
};
=======
>>>>>>> dfcde0dbb6efe413d73efe77042402d6398d59fe

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
        format: 'YYYY-MM-DD',
        date: moment().format("YYYY-MM-DD"),
        locale: 'es',
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
<<<<<<< HEAD
           delay: 500,
           minLength: 1,
           select: function(event, ui){
               event.preventDefault();
               console.clear();
               ui.item.operacion=1;
               ui.item.desc_actividad='';
               ui.item.Cantidad=1;
               console.log(tareas.items);

               tareas.add(ui.item);
               tareas.list();
               $(this).val('');
           }
     });

     //evento cantidad
     $('#tblorden tbody')
         .on('click', 'a[rel="remove"]', function(){
            var tr = tblOrdens.cell($(this).closest('td, li')).index();
            tareas.items.actividades.splice(tr.row, 1);
            tareas.list();
         })
         .on('change keyup', 'input[name="operacion"]', function(){
            console.clear();
            var oper = parseInt($(this).val());
            var tr = tblOrdens.cell($(this).closest('td, li')).index();
            tareas.items.actividades[tr.row].operacion = oper;
            tareas.calculo_total();
         })
         .on('change keyup', 'input[name="desc_actividad"]', function(){
            console.clear();
            var desc = ($(this).val());
            var tr = tblOrdens.cell($(this).closest('td, li')).index();
            tareas.items.actividades[tr.row].desc_actividad = desc;

         })
         .on('change keyup', 'input[name="Cantidad"]', function(){
            console.clear();
            var cant = parseInt($(this).val());
            var tr = tblOrdens.cell($(this).closest('td, li')).index();
            tareas.items.actividades[tr.row].Cantidad = cant;
            tareas.calculo_total();

         });

     //eliminar busqueda
     $('.btnClearSearch').on('click', function () {
        $('input[name="buscar"]').val('').focus();
     });

     //event submit
     $('form').on('submit', function (e) {
            e.preventDefault();
            //validado que sea vacio el detalle
            if(tareas.items.actividades.length === 0){
            message_error('Debe al menos tener un item en su detalle de venta');
            return false;
            }

            tareas.items.Empleado = $('select[name="Empleado"]').val();
            tareas.items.fecha = $('input[name="fecha"]').val();
            var parameters = new FormData();
            parameters.append('action', $('input[name="action"]').val());
            parameters.append('tareas', JSON.stringify(tareas.items));
            submit_with_ajax(window.location.pathname, 'Notificación', '¿Estas seguro de realizar la siguiente acción?', parameters, function () {
                location.href = '/movil/actividades/lista/';
            });
     });

     tareas.list();

=======
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
>>>>>>> dfcde0dbb6efe413d73efe77042402d6398d59fe
});