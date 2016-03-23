$(document).ready(function(){
  console.log("Hi there!")

    $('.details_button').on('submit', function(event){
	event.preventDefault();

    var data = $(this).serialize() // returns all the data in your form

	$.ajax({
        method: "GET",
        url: ("/dates/details/" + $('#date_slug').html()), //just goest to url  
        data: data, //only sends the id so we can do the logic and sorting of db in our view
        success: function(data){
        	console.log("here"); //for testing 
            console.log(data["dates"][0]["notes"])

// This will target the element with an id of list in the mustache file
// We use Mustache's "render" function to take the targeted template and load it with the data we got back earlier
// Use jQuery to target the div with the id of our postFK that we renamed to post 
// and change the inside of it's html with the variable of the rendered data
	
    		var template = $('#details').html();
			// we get an object with a property comments, so here we call data.comments or just pass the data
			var renderM = Mustache.render(template,data);
			console.log(renderM); //for testing 


            var date_slug = (data.dates[0].slug) // gets the post fk from the comment data we send back
            var date = $("#" + date_slug) // targets the right div in the DOM that has the same post id as ou post FK

            // if (comment_fk === post) {
			date.html(renderM) // just attach it to post and we dont need to conditional 
                
			}
		})
	})
});

