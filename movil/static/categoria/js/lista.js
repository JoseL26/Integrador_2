$(function () {
    $('#data').DataTable({
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
            {"data": "Descripcion"},
            {"data": "Descripcion"},
        ],
        columnDefs: [
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var buttons = '<a href="/movil/categoria/edit/' + row.id + '/" class="btn btn-warning btn-xs btn-flat"><i class="las la-pen"></i></a>';
                    buttons += '<a href="/movil/categoria/delete/' + row.id + '/" type="button" class="btn btn-danger btn-xs btn-flat"><i class="las la-trash"></i></a>';
                    return buttons;
                }
            },
        ],
        initComplete: function (settings, json) {

        }
    });
});