$(document).ready(function() {
		console.log("test");
		//console.log(task);
})

function showDetail(id)
{
	var _id = $(id).attr("id");
	
	var product = _id.split("_")[1];
	var item = _id.split("_")[2];
	var url = "/start_page/getstatus/" + product + "/" + item + "/";

	$.ajax({
		type: "GET",
		url: url
	})
	.done(function( msg ) {
		if(msg == "1")
			$(id).find( "rect" ).css("fill", "blue");
		else if(msg == "2")
			$(id).find( "rect" ).css("fill", "yellow");
		else if(msg == "3")
			$(id).find( "rect" ).css("fill", "red");
	});
}

function getallstatus()
{
	$("svg").each(function() {
		showDetail($(this));
	});
}