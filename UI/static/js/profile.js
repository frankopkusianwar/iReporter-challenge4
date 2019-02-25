var valid_token = localStorage.getItem('access-token');

window.onload = function loadFlags(){
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
                for (item = 0; item < message['data'].length; item++){
                    records+=`<a href="viewFlag.html"><h3>${message['data'][item].title}</h3>`

                }
                document.getElementById('list2').innerHTML=records;
            }

        });
}