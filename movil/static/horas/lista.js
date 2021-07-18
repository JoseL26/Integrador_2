var tblParte;

$(function () {
    tblParte = $('#data').DataTable({
        responsive: true,
        autoWidth: false,
        destroy: true,
        deferRender: true,
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: {
                'action': 'searchdata'
            },
            dataSrc: ""
        },
        columns: [
            {"data": "id"},
            {"data": "Empleado.Nombres"},
            {"data": "fecha"},
            {"data": "TotalHoras"},
            {"data": "id"},
        ],
        columnDefs: [
            {
                targets: [-2],
                class: 'text-center',
                orderable: false,
                render: function(data, type, row){
                    return parseFloat(data).toFixed(2);
                }
            },
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var buttons = '<a href="/movil/actividades/delete/' + row.id + '/" type="button" class="btn btn-danger btn-xs btn-flat"><i class="las la-trash"></i></a>';
                    buttons += '<a href="/movil/actividades/edit/' + row.id + '/" class="btn btn-warning btn-xs btn-flat"><i class="las la-pen"></i></a>';
                    buttons += '<a rel="details" class="btn btn-success btn-xs btn-flat"><i class="fas fa-search"></i></a> ';
                    buttons += '<a href="/movil/actividades/imprimir/pdf/' + row.id + '/" target="blank" class="btn btn-info btn-xs btn-flat"><i class="fas fa-file-pdf"></i></a> ';
                    return buttons;
                }
            },
        ],
        initComplete: function (settings, json) {

        }
    });
    $('#data tbody')
        .on('click', 'a[rel="details"]', function () {
            var tr = tblParte.cell($(this).closest('td, li')).index();
            var data = tblParte.row(tr.row).data();
            console.log(data);

            $('#tblDet').DataTable({
                responsive: true,
                autoWidth: false,
                destroy: true,
                deferRender: true,
                //data: data.det,
                ajax: {
                    url: window.location.pathname,
                    type: 'POST',
                    data: {
                        'action': 'search_details_parte',
                        'id': data.id
                    },
                    dataSrc: ""
                },
                columns: [
                    {"data": "Orden.Orden"},
                    {"data": "Orden.equipo.Cod_equipo"},
                    {"data": "operacion"},
                    {"data": "desc_actividad"},
                    {"data": "Cantidad"},
                ],
                columnDefs: [
                    {
                        targets: [-1],
                        class: 'text-center',
                        render: function (data, type, row) {
                            return parseFloat(data).toFixed(2);
                        }
                    },

                ],
                initComplete: function (settings, json) {

                }
            });

            $('#myModelDet').modal('show');
        });
});