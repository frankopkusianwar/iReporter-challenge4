var valid_token = localStorage.getItem('access-token');
var redidentity = localStorage.getItem('allincntid');

//fetch all records
window.onload = function loadoneRecord(){
    fetch(`https://ireporter-challenge4.herokuapp.com/api/v1/incidents/${redidentity}`,{
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
                    if(incident_status ==='draft'){
                        records+=`<div class="redflag-content"><item1><img src="static/images/coruption1.jpg"></item1>
                        <item2><h1>${message['data'][item].title}</h1><blockquote>${message['data'][item].description}</blockquote><p><span class="label">Latitude: ${message['data'][item].latitude}</span> &nbsp&nbsp&nbsp&nbsp&nbsp<span class="label">Longitude: ${message['data'][item].longitude}</span></p>
                        </item2><p><span class="label">Status: ${message['data'][item].status}</span> </p><span class="view-buttons">
                            <form>
                                <span class="primary-button"><input onclick="resolve(${incidentId})" type="button" value="resolve"><input onclick="investigate(${incidentId})" type="button" value="investigate"></span><span class="delete"><input type="button" value="reject" onclick="reject(${incidentId})"></span>
                            </form>
                        </span></div>`
                    }else if(incident_status ==='Under Investigation'){
                        records+=`<div class="redflag-content"><item1><img src="static/images/coruption1.jpg"></item1>
                        <item2><h1>${message['data'][item].title}</h1><blockquote>${message['data'][item].description} <a href="recorddet.html">Read more...</a>&nbsp&nbsp&nbsp&nbsp&nbsp<a href="#" onclick=popText()>edit text</a></blockquote><p><span class="label">Latitude: ${message['data'][item].latitude}</span> &nbsp&nbsp&nbsp&nbsp&nbsp<span class="label">Longitude: ${message['data'][item].longitude}</span></p>
                        </item2><p><span class="label">Status: ${message['data'][item].status}</span> </p><span class="view-buttons">
                            <form>
                                <span class="primary-button"><input onclick="resolve(${incidentId})" type="button" value="resolve"></span><span class="delete"><input type="button" value="reject" onclick="reject(${incidentId})"></span>
                            </form>
                        </span></div>`
                    }else{
                        records+=`<div class="redflag-content"><item1><img src="static/images/coruption1.jpg"></item1>
                        <item2><h1>${message['data'][item].title}</h1><blockquote>${message['data'][item].description} <a href="recorddet.html">more</a></blockquote><p><span class="label">Latitude: ${message['data'][item].latitude}</span> &nbsp&nbsp&nbsp&nbsp&nbsp<span class="label">Longitude: ${message['data'][item].longitude}</span></p>
                        </item2><p><span class="label">Status: ${message['data'][item].status}</span> </p></div>`
                    }

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

function resolve(incId){
    var new_status='Resolved';

    var inc_data = {
        status:new_status

    }

    fetch(`https://ireporter-challenge4.herokuapp.com/api/v1/incidents/${incId}/status`,{
        method:'PATCH',
        headers: {
            'Accept': 'application/json, text/plain, */*',
            'Content-type':'application/json',
            'x-access-token':valid_token
        },
        body:JSON.stringify(inc_data)
    })
        .then((response) => response.json())
        .then(function(message){

            if(message['message'] ==="status updated successfully"){
                alert("updated record's status");
                window.location.replace('admindet.html');
            }

        });
}

function investigate(incId){
    var new_status='Under Investigation';

    var inc_data = {
        status:new_status

    }

    fetch(`https://ireporter-challenge4.herokuapp.com/api/v1/incidents/${incId}/status`,{
        method:'PATCH',
        headers: {
            'Accept': 'application/json, text/plain, */*',
            'Content-type':'application/json',
            'x-access-token':valid_token
        },
        body:JSON.stringify(inc_data)
    })
        .then((response) => response.json())
        .then(function(message){

            if(message['message'] ==="status updated successfully"){
                alert("updated record's status");
                window.location.replace('admindet.html');
            }

        });
}

function reject(incId){
    var new_status='Rejected';

    var inc_data = {
        status:new_status

    }

    fetch(`https://ireporter-challenge4.herokuapp.com/api/v1/incidents/${incId}/status`,{
        method:'PATCH',
        headers: {
            'Accept': 'application/json, text/plain, */*',
            'Content-type':'application/json',
            'x-access-token':valid_token
        },
        body:JSON.stringify(inc_data)
    })
        .then((response) => response.json())
        .then(function(message){

            if(message['message'] ==="status updated successfully"){
                alert("updated record's status");
                window.location.replace('admindet.html');
            }

        });
}
