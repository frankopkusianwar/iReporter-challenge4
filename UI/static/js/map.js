//This div will display Google map
const mapArea = document.getElementById('map');

//This button will set everything into motion when clicked
const actionBtn = document.getElementById('showMe');
const latit = document.getElementById('latitude');
const longit = document.getElementById('longitude');

const paragraph = document.getElementById('p');

//This will display all the available addresses returned by Google's Geocode Api
const locationsAvailable = document.getElementById('locationList');

//Let's bring in our API_KEY
const __KEY = 'AIzaSyC04WV5MMYyaXRaVv3SsFGem5mUzW76GKA';

//Let's declare our Gmap and Gmarker variables that will hold the Map and Marker Objects later on
var Gmap;
var Gmarker;

function showmap(){
    actionBtn.style.display = "none";
    paragraph.style.display = "none";
    getLocation();
}

getLocation = () => {
  // check if user's browser supports Navigator.geolocation
  	if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(displayLocation, showError, options);
  	}else {
    	alert("Sorry, your browser does not support this feature... Please Update your Browser to enjoy it");
  	}
}

// Displays the different error messages
showError = (error) => {
	  mapArea.style.display = "block"
	  switch (error.code) {
	    case error.PERMISSION_DENIED:
	      mapArea.innerHTML = "You denied the request for your location."
	      break;
	    case error.POSITION_UNAVAILABLE:
	      mapArea.innerHTML = "Your Location information is unavailable."
	      break;
	    case error.TIMEOUT:
	      mapArea.innerHTML = "Your request timed out. Please try again"
	      break;
	    case error.UNKNOWN_ERROR:
	      mapArea.innerHTML = "An unknown error occurred please try again after some time."
	      break;
  	}
}
//Makes sure location accuracy is high
const options = {
  enableHighAccuracy: true
}

displayLocation = (position) => {
	const lat = position.coords.latitude;
	const lng = position.coords.longitude;
	const latlng = {lat, lng}
	showMap(latlng, lat, lng);
	createMarker(latlng);
	mapArea.style.display = "block";
	// getGeolocation(lat, lng)
	latit.value = lat
	longit.value = lng
}

showMap = (latlng, lat, lng) => {
	var mapOptions = {
	    center: latlng,
	    zoom: 17
	};
	Gmap = new google.maps.Map(mapArea, mapOptions);
	Gmap.addListener('drag', function () {
	    Gmarker.setPosition(this.getCenter()); // set marker position to map center
	});
	Gmap.addListener('dragend', function () {
	    Gmarker.setPosition(this.getCenter()); // set marker position to map center
	});
	Gmap.addListener('idle', function () {
	    Gmarker.setPosition(this.getCenter()); // set marker position to map center
	    if (Gmarker.getPosition().lat() !== lat || Gmarker.getPosition().lng() !== lng) {
	      	setTimeout(() => {
	      		latit.value = Gmarker.getPosition().lat();
	      		longit.value = Gmarker.getPosition().lng();
	        	// updatePosition(this.getCenter().lat(), this.getCenter().lng()); // update position display
	      	}, 2000);
	    }
	});
}

createMarker = (latlng) => {
	var markerOptions = {
	    position: latlng,
	    map: Gmap,
	    animation: google.maps.Animation.BOUNCE,
	    clickable: true
	};
	Gmarker = new google.maps.Marker(markerOptions);
}

// getGeolocation = (lat, lng) => {
//   const latlng = lat + "," + lng;
//   fetch( `https://maps.googleapis.com/maps/api/geocode/json?latlng=${latlng}&key=${__KEY}` )
//     .then(res => res.json())
//     .then(data => populateCard(data.results));
// }

// populateCard = (geoResults) => {

//   removeAddressCards();


//   geoResults.map(geoResult => {
//     // first create the input div container
//     const addressCard = document.createElement('div');
//     // then create the input and label elements
//     const input = document.createElement('input');
//     const label = document.createElement('label');
//     // then add styling classes to the div and input
//     addressCard.classList.add("card");
//     input.classList.add("card_space");
//     // add attributes to them
//     input.setAttribute("name", "address");
//     input.setAttribute("type", "radio");
//     input.setAttribute("value", geoResult.formatted_address);
//     input.setAttribute("id", geoResult.place_id);
//     label.setAttribute("for", geoResult.place_id);
//     label.innerHTML = geoResult.formatted_address;
//     addressCard.appendChild(label)
//     addressCard.appendChild(input);
//     return (
//       // append the created div to the locationsAvailable div
//       locationsAvailable.appendChild(addressCard)
//     );
//   })

// }

// updatePosition = (lat, lng) => {
//   	getGeolocation(lat, lng);
// }

// check if the container has a child node to force re-render of dom
// function removeAddressCards(){
//   if (locationsAvailable.hasChildNodes()) {
//     	while (locationsAvailable.firstChild) {
//       		locationsAvailable.removeChild(locationsAvailable.firstChild);
//     	}
//   	}
// }

// const inputAddress = document.getElementById('latitude')

// inputClicked = result => {

// 	alert('yes');
//   // inputAddress.value = result.formatted_address;

//   // removeAddressCards();
// }
