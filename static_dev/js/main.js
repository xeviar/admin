$(document).ready(function() {
		console.log("test");
		getallstatus();
})

function showDetail(id)
{
	var _id = $(id).attr("id");
	
	var product = _id.split("_")[1];
	var item = _id.split("_")[2];
	var url = "/start_page/getdetail/" + product + "/" + item + "/";

	$.ajax({
		type: "GET",
		url: url
	})
	.done(function( msg ) {
		var obj = jQuery.parseJSON(msg);

		var _html = '<table class="data tableA"><tr class="headerA"><td>Status</td><td>Description</td><td>Time</td></tr>';

		$.each( obj.data, function( index, str ){
			_obj = jQuery.parseJSON(str)
			console.log(_obj["status"]);
			console.log("test")

			_html += '<tr class="row"><td>' + _obj["status"] + "</td>" +
					"<td>" + _obj["desc"] + "</td>" +
					"<td>" + _obj["timestamp"] + "</td></tr>";
		});

		_html += "</table>"

		//$("#detail").html(obj.data)
		$("#detail").html(_html)
	});
}

function showStatus(id)
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
			$(id).find( "rect" ).css("fill", "#5858FA");
		else if(msg == "2")
			$(id).find( "rect" ).css("fill", "yellow");
		else if(msg == "3")
			$(id).find( "rect" ).css("fill", "red");
	});
}

function getallstatus()
{
	$("svg").each(function() {
		showStatus($(this));
	});

	setTimeout("getallstatus()", 5000);
}