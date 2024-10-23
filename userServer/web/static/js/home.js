
$(function (){
	
	var $lampCardsContainer = $(".lamp-cards-container");

	$.ajax({
		type: "GET",
		url: "/lamps", // TODO: Replace it by "/api/lamps"
		success: function(lamps) {
			$.each(lamps, function(i, lamp) {
				var template;
				if (lamp.state === "off") {
					/*$lampCardsContainer.append('<div class="lamp-card"><h4 class="lamp-card-title"><b>' + lamp.name + '</b></h4><p class="lamp-card-state-text">Turned Off</p><button class="lamp-card-btn" name="turn-on-' + lamp.id + '">Turn On</button></div>');
					*/
					template = $("#lamp-card-off-template").html();
				} else {
					/*$lampCardsContainer.append('<div class="lamp-card"><h4 class="lamp-card-title"><b>' + lamp.name + '</b></h4><p class="lamp-card-state-text">Turned On</p><button class="lamp-card-btn" name="turn-off-' + lamp.id + '">Turn On</button></div>');
					*/
					template = $("#lamp-card-on-template").html();
				}
				$lampCardsContainer.append(Mustache.render(template, lamp));
			});
		},
		error: function() {
			alert("Error occured while loading lamps");
		}
	});
});
