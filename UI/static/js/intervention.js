var valid_token = localStorage.getItem('access-token');

//fetch all interventions
window.onload = function loadinterventionrecords(){
    fetch("https://ireporter-challenge4.herokuapp.com/api/v1/interventions",{
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
                	interventionId = message['data'][item].id
                	red_status = message['data'][item].status
	                records+=`<item1><h1>${message['data'][item].title}</h1><a href="#" onclick="details(${interventionId})">viewdetails</a></item1>`
                }
                document.getElementById('interventions').innerHTML=records;
            }else if(message['message']==='intervention records not found'){
                records=`<h1>intervention records not found!</h1>`
                document.getElementById('interventions').innerHTML=records;
            }else{
                window.location.replace('index.html');
            }

        });
}

function details(interventionId){
    localStorage.setItem('intvid', interventionId);
    window.location.replace('intervention.html');
}
