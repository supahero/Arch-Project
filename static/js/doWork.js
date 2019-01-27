//var ids = [];
//var e;

function reply_click(e) {

    //get id name onclick

    e = e || window.event;
    e = e.target || e.srcElement;
    if (e.nodeName != 'BUTTON') {
        //alert(e.id);
        ids = [];
        ids.push(e.id);
        console.log(ids);
        doWork()
    }
}

function doWork() {
    // ajax the JSON to the server
    $.ajax({
        type: "POST",
        url: "/receiver",
        dataType: "json",
        contentType: "application/json; charset=utf-8",
        data: JSON.stringify(ids),
        success: function (data) {
            console.log(data);
            $('#response').html('');
            for (let row of data) {
                $('#response').append($('<div></div>').text(row));
            }

        }

    });
// stop link reloading the page
    event.preventDefault();
}

