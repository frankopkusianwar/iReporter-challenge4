function addUser(){
	//capturing user data
	var fname=document.getElementById('firstName').value;
	var lname=document.getElementById('lastName').value;
	var onames=document.getElementById('otherNames').value;
	var username=document.getElementById('username').value;
    var email = document.getElementById("email").value;
    var password=document.getElementById('password').value;

    //form validation
    if(fname ==''){
        alert("please enter first name");
        return false
    }
    if(lname ==''){
        alert("please enter last name");
        return false
    }
    if(username ==''){
        alert("please enter username");
        return false
    }
    if(email== ''){
        alert("please enter email");
        return false
    }
    if(password== ''){
        alert("please enter password");
        return false
    }

    //posting to the database

    var user_data = {
    	firstName:fname,
    	lastName:lname,
    	otherNames:onames,
    	username:username,
    	email:email,
    	password:password
    }

    fetch('https://ireporter-challenge4.herokuapp.com/api/v1/users',{
        method:'POST',
        headers: {
            'Accept': 'application/json, text/plain, */*',
            'Content-type':'application/json'
        },
        body:JSON.stringify(user_data)
    })
    	.then((response) => response.json())
        .then(function(message){

            if(message['message']=== 'invalid email adress'){
                alert('invalid email adress');
                return false
            }
            else if(message['message']=== 'password should be more than 8 characters'){
                alert('password should be more than 8 characters');
                return false
            }
            else if(message['message']=== 'username already exists'){
                alert('username already exists');
                return false
            }
            else if(message['message']=== 'email already exists'){
                alert('email already exists');
                return false
            }
            else if(message['data'][0]['message']==='user created successfully'){
            	window.location.replace('index.html');
                alert('account created successfully');
            }

        });

}
