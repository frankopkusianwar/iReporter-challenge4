var valid_token = localStorage.getItem('access-token');
var intidentity = localStorage.getItem('intvid');

// fetch one record
window.onload = function loadinterventions(){
    fetch(`https://ireporter-challenge4.herokuapp.com/api/v1/incidents/${intidentity}`,{
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
                    if(red_status ==='draft'){
                        records+=`<div class="redflag-content"><item1><img src="static/images/coruption1.jpg"><span class="location" id="edit_txt">
                                </br></br><textarea rows="8" id="new_com">${message['data'][item].description}</textarea></br></br><input type="button" value="update" id="submit" onclick="updatecomment(${redflagId})"></span></item1>
                        <item2><h1>${message['data'][item].title}</h1><blockquote>${message['data'][item].description} <a href="#" onclick=popText()>edit text</a></blockquote><p><span class="label">Latitude: ${message['data'][item].latitude}</span> &nbsp&nbsp&nbsp&nbsp&nbsp<span class="label">Longitude: ${message['data'][item].longitude}</span></p>
                        </item2><p><span class="label">Status: ${message['data'][item].status}</span> </p><span class="view-buttons">
                            <form>
                                <span class="delete"><input type="button" value="Delete" onclick="delet()"></span>
                                <span class="primary-button"><input onclick="poplocation()" type="button" value="edit location"></span>
                            </form>
                            <form><span class="location" id="loc"><input type="text" placeholder="New longitude" id="new_long"></input>
                                <input type="text" placeholder="New latitude" id="new_lat"></input><input type="button" value="update" id="submit" onclick="updatelocation(${redflagId})"></span></form>
                            <form><span class="location" id="del_loc"><input type="button" value="are you sure you want to delete!" style="color:red"></input><input type="button" value="cancel" id="submit" onclick="canc()"><input type="button" value="ok" id="submit" onclick="del(${redflagId})"></span></form>
                        </span></div>`
                    }else{
                        records+=`<div class="redflag-content"><item1><img src="static/images/coruption1.jpg"></item1>
                        <item2><h1>${message['data'][item].title}</h1><blockquote>${message['data'][item].description}</blockquote><p><span class="label">Latitude: ${message['data'][item].latitude}</span> &nbsp&nbsp&nbsp&nbsp&nbsp<span class="label">Longitude: ${message['data'][item].longitude}</span></p>
                        </item2><p><span class="label">Status: ${message['data'][item].status}</span> </p></div>`
                    }

                }
                document.getElementById('redflags').innerHTML=records;
            }else{
                window.location.replace('index.html');
            }

        });
}

function poplocation(){
    var popup = document.getElementById("loc");
    popup.classList.toggle("show");
}

function delet(){
    var popup = document.getElementById("del_loc");
    popup.classList.toggle("show");
}

function popText(){
    var popup = document.getElementById("edit_txt");
    popup.classList.toggle("show");
}

function updatelocation(redId){
    var new_lat=document.getElementById('new_lat').value;
    var new_long=document.getElementById('new_long').value;

    if(new_lat ==''){
        alert("please enter new latitude");
        return false
    }
    if(new_long ==''){
        alert("please enter new longitude");
        return false
    }

    var inc_data = {
        latitude:new_lat,
        longitude:new_long
    }

    fetch(`https://ireporter-challenge4.herokuapp.com/api/v1/incidents/${redId}/location`,{
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

            if(message['data'][0]['message'] ==="updated record's location"){
                alert("updated intervention location");
                window.location.replace('intervention.html');
            }

        });

}

function del(redId){
    fetch(`https://ireporter-challenge4.herokuapp.com/api/v1/incidents/${redId}`,{
        method:'DELETE',
        headers:{
            'Content-type':'application/json',
            'x-access-token':valid_token
        },
    }).then((response)=> response.json())
        .then(function (message){

            if(message['data'][0]['message'] ==='record has been deleted'){

                alert('intervention record has been deleted');
                window.location.replace('viewIntervention.html');
            }

        });
}

function canc(){
    window.location.replace('intervention.html');
}

function updatecomment(redId){
    var new_comment=document.getElementById('new_com').value;

    var inc_data = {
        comment:new_comment

    }

    fetch(`https://ireporter-challenge4.herokuapp.com/api/v1/incidents/${redId}/comment`,{
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

            if(message['data'][0]['message'] ==="updated record's comment"){
                alert("updated record's comment");
                window.location.replace('intervention.html');
            }

        });
}


