function initMap(){
			var boundaries =[
				{lat:38.09695, lng:23.80197},
				{lat:38.09563, lng:23.82925},
				{lat:38.06426, lng:23.82721},
				{lat:38.06507, lng:23.80013},
				{lat:38.07661, lng:23.79651}
			]
			var delivarea = new google.maps.Polygon({paths: boundaries});
			var options = {
				componentRestrictions: {country: "gr"}
			};
			var inputfield = document.getElementById('address');
			//var types = 'Addresses';
			//var autocomplete = new google.maps.places.Autocomplete(inputfield,options);
			var autocomplete = new google.maps.places.Autocomplete(document.getElementById('address'),options);
			autocomplete.setFields(['address_components','geometry']);
			$('#Check').click(function(e){
				//console.log(autocomplete.getPlace().geometry.location);
				//console.log(autocomplete.getPlace().geometry.location.lat());
				//console.log(autocomplete.getPlace().geometry.location.lng());
				console.log(google.maps.geometry.poly.containsLocation(autocomplete.getPlace().geometry.location,delivarea));
				if(google.maps.geometry.poly.containsLocation(autocomplete.getPlace().geometry.location,delivarea)==false){
					alert('Η διευθύνση είναι εκτός οριών διανομής')
				}
			});
		}