var valid_token = localStorage.getItem('access-token');

//fetch all records
window.onload = function loadRecords(){
    fetch("https://ireporter-challenge4.herokuapp.com/api/v1/incidents",{
        method:'GET',
        headers:{
            'Content-type':'application/json',
            'x-access-token':valid_token
        },
    }).then((response)=> response.json())
        .then(function (message){
            if(message['data']){
                var item
                records=``
                for (item = message['data'].length-1; item >= 0; item--){
                    incidentId = message['data'][item].id
                    incident_status = message['data'][item].status
                    records+=`<item1><h1>${message['data'][item].title}</h1><p><b style="color:blue">status</b>: <i style="color:red">${incident_status}</i></p><a href="#" onclick=details(${incidentId})>viewdetails</a></item1>`

                }
                document.getElementById('redflags').innerHTML=records;
            }else if(message['message']==='records not found'){
                records=`<h1>records not found!</h1>`
                document.getElementById('redflags').innerHTML=records;
            }else{
                window.location.replace('index.html');
            }

        });
}

function details(redid){
    localStorage.setItem('allincntid', redid);
    window.location.replace('admindet.html');
}
