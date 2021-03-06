$(function() {	
	function log( message ) {
		$( "<div/\>" ).text( message ).prependTo( "#patient_results" );
		$( "#log" ).scrollTop( 0 );
	}

	//Yup this is my list of searchable patients for JQuery.
	//The team running the patient search will need to remedy this...
	//Sorry everyone!
	var availableTags = [
		"Alex Gainer",
		"Phil Strong",
		"Mary Roth",
		"James Davis",
		"Anthony Masuda",
		"Bob Bobbers",
		"Ryan Ryaners",
		"Paul Paulers",
		"George Georgers",
		"Eric Ericson"
	];

	//Basic autocomplete functionality...
	//the data source is the array above.
	$( ".demo #patients" ).autocomplete({
		source: availableTags,
		minLength: 2,
		select: function( event, ui ) {
			log( ui.item ?
				"Selected: " + ui.item.value :
				"Nothing selected, input was " + this.value );
		}
	});
});

/*
"""
Copyright 2011 Health Records for Everyone

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""*/
