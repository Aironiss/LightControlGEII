
$(function (){
	
	var $lampCardsContainer = $(".lamp-cards-container");
	
	function addLampCard(lamp) {
		var template;
		if (lamp.State === "off") {	
			template = $("#lamp-card-off-template").html();
		} else {
			template = $("#lamp-card-on-template").html();
		}
		$lampCardsContainer.append(Mustache.render(template, lamp));
	}

	$.ajax({
		type: "GET",
		url: "api/lamps",
		success: function(lamps) {
			$.each(lamps, function(i, lamp) {
				addLampCard(lamp);
			});
		},
		error: function() {
			console.error("Error occured while loading lamps");
		}
	});

	$lampCardsContainer.delegate(".turn-on-lamp-btn, .turn-off-lamp-btn", "click", function() {
		var clickedButton = $(this);
		var id = clickedButton.attr("data-id");
		var data = {};
		if (clickedButton.hasClass("turn-on-lamp-btn")) {
			data["Action"] = "turnOn";
		} else {
			data["Action"] = "turnOff";
		}

		//alert("Api call: id=" + id + ", action=" + data["action"]);
		$.ajax({
			type: "PUT",
			url: "api/lamps/" + id,
			data: data,
			success: function(newLamp) {
				clickedButton.parent().remove();
				addLampToCard(newLamp);
			},
			error: function() {
				console.error("Error occured while changing lamp state");
			}
		});
	});
});
