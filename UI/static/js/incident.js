var valid_token = localStorage.getItem('access-token');

function addIncident(){
    //capturing user data
    var title=document.getElementById('title').value;
    var incidentType=document.getElementById('incidentType').value;
    var description=document.getElementById('description').value;
    var latitude=document.getElementById('latitude').value;
    var longitude = document.getElementById("longitude").value;

    //form validation
    if(title ==''){
        alert("please enter title");
        return false
    }
    if(description ==''){
        alert("please enter description");
        return false
    }
    if(latitude ==''){
        alert("please enter latitude");
        return false
    }
    if(longitude ==''){
        alert("please enter longitude");
        return false
    }

    //posting to the database

    var inc_data = {
        title:title,
        incidentType:incidentType,
        description:description,
        latitude:latitude,
        longitude:longitude
    }

    fetch('https://ireporter-challenge4.herokuapp.com/api/v1/incidents',{
        method:'POST',
        headers: {
            'Accept': 'application/json, text/plain, */*',
            'Content-type':'application/json',
            'x-access-token':valid_token
        },
        body:JSON.stringify(inc_data)
    })
        .then((response) => response.json())
        .then(function(message){

            if(message['message']=== 'token missing'){
                alert('token missing');
                return false
            }
            if(message['message']=== 'invalid token'){
                alert('invalid token');
                return false
            }
            if(message['message']=== 'please enter incidentType as red-flag or intervention'){
                alert('please select incident type');
                return false
            }
            else if(message['data'][0]['message']==='created incident record'){
                if (incidentType == 'red-flag'){
                    window.location.replace('viewFlag.html');
                }
                else{
                    window.location.replace('viewIntervention.html');
                }
            }

        });
}

// fetch all red-flags
window.onload = function loadRedFlags(){
    fetch("https://ireporter-challenge4.herokuapp.com/api/v1/red-flags",{
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
                    redflagId = message['data'][item].id
                    red_status = message['data'][item].status
                    records+=`<item1><h1>${message['data'][item].title}</h1><a href="#" onclick=details(${redflagId})>viewdetails</a></item1>`
                }
                document.getElementById('redflags').innerHTML=records;
            }else if(message['message']==='red-flag records not found'){
                records=`<h1>red-flag records not found!</h1>`
                document.getElementById('redflags').innerHTML=records;
            }else{
                window.location.replace('index.html');
            }

        });
}

function details(redid){
    localStorage.setItem('incntid', redid);
    window.location.replace('recorddet.html');
}
