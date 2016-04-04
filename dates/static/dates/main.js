function init_map(map_date, latitude, longitude) {
    // this gets the lat and long from the geocoder below
    var var_location = new google.maps.LatLng(latitude, longitude);
 
    var var_mapoptions = {
        center: var_location,
        zoom: 17
    };
 
    var var_marker = new google.maps.Marker({
    position: var_location,
    map: var_map });
 
    var var_map = new google.maps.Map(map_date.get(0),
        var_mapoptions);
    // the zero will get the element the jquery object is wrapping
 
    var_marker.setMap(var_map); 
};


$(document).ready(function(){
  console.log("Hi there!")

    $('.details_button').on('submit', function(event){
	event.preventDefault();

    var data = $(this).serialize() // returns all the data in your form

	$.ajax({
        method: "GET",
        url: ("/details/" + $('#date_slug').html()), //just goest to url  
        data: data, //only sends the id so we can do the logic and sorting of db in our view
        success: function(data){
        	console.log("here"); //for testing 
            // console.log(data["dates"][0]["notes"])

        // use instead of success
        // .done(function(data, status)){
        //     console.log("here");//for testing 
        // }

// This will target the element with an id of list in the mustache file
// We use Mustache's "render" function to take the targeted template and load it with the data we got back earlier
// Use jQuery to target the div with the id of our postFK that we renamed to post 
// and change the inside of it's html with the variable of the rendered data
	
    		var template = $('#details').html();
			// we get an object with a property comments, so here we call data.comments or just pass the data
			var renderM = Mustache.render(template,data);
			// console.log(renderM); //for testing 


            var date_slug = (data.dates[0].slug) // gets the post fk from the comment data we send back
            var date = $("#" + date_slug) // targets the right div in the DOM that has the same post id as ou post FK

            // if (comment_fk === post) {
			date.html(renderM) // just attach it to post and we dont need to conditional 
                
			}
		})
	})

    $('.map_button').on('submit', function(event){

        event.preventDefault();
        var date_id = ($(this).find("[name='date_id']").attr("value")); // find tells it where in the this object to look for the value
        var map_date = $("#" + date_id) // targets the right div in the DOM that has the same post id as ou post FK
        console.log(map_date)

        var geocoder = new google.maps.Geocoder();
        var address = ($(this).find("[name='address']").attr("value")); // get the address from the DOM of the buttom you clicked

        geocoder.geocode({'address': address}, function(results, status) {
            // this takes the address we got from the DOM and uses google api to get the geocode, then send the geocode to the google maps api
            if (status == google.maps.GeocoderStatus.OK) {
                var latitude = results[0].geometry.location.lat();
                var longitude = results[0].geometry.location.lng();
                // console.log(latitude);
                // console.log(longitude);
                } 

            map_date.css({"height":"250px"});
            map_date.css({"margin-bottom":"1.5em"});
         
            init_map(map_date, latitude, longitude);

        }); 
    })

    // this checks the background light to change the color of the title
    BackgroundCheck.init({
        targets: '#welcome',
        images: '.landing'
    });

    BackgroundCheck.refresh();

    BackgroundCheck.get('targets');

});

