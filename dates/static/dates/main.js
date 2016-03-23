$(document).ready(function(){
  console.log("Hi there!")

  // $('#comment').on('click', function(event){ //form submit event handler
  //   event.preventDefault();//prevents default which would reload page

  //   // this get the value of their comment text box from the form 
  //   var comment = $('#comment_form #id_content').val()
  //   console.log(comment); //for testing

  //   var data = $("#comment_form").serialize() // returns all the data in your form
  //   console.log(data); //for testing 


  //   // sending the data to the url then view
  //   $.ajax({
  //       method: "POST",
  //       url: ("/news/comment/" + $('#post_slug_thing').html()), // sends through with the slug value
  //       data: data,

  //     // comes back from the view with a json respone to our data 
  //     success:function(response){
  //       console.log(response) //for testing

  //       // basicallly prints it out by attaching it to a div (not using mustache)
  //       $('#comment_div').text(response["comment"])
  //     }
  //   })
  //   // this tells the user they have submitted the comment when they click the button
  //   $('#submit_comment_div').text("Comment submitted!");
  // })


/////////////////////       ////////////////////         /////////////////////


    $('.details_button').on('submit', function(event){
	event.preventDefault();

    var data = $(this).serialize() // returns all the data in your form
	console.log ("clicked!"); //for testing 

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

			// if (comment_fk === post) {
			$(".details_div").html(renderM) // just attach it to post and we dont need to conditional 
                
			}
		})
	})
});

