/**
 * Script to manage the map displayed to list companies
 * Created by foutoucour on 26/03/17.
 * The theme of the map is loaded from `snazzy_theme.py` file.

 * CUSTOMS infos windows ref : http://en.marnoto.com/2014/09/5-formas-de-personalizar-infowindow.html
 */

// namespace
var google_map = {
    map: null,

    /*
     Get the current position of the user and move the google map to the location
     */
    getLocation: function () {
        var ajax_locate_me_stats = function(success, latitude, longitude) {
            $.ajax({
                type: "post",
                url: "/ajax/locate_me_stats",
                data: {
                    success: success,
                    latitude: latitude,
                    longitude: longitude
                }
            });
        };

        // default values for the ajax call
        var success = false;
        var latitude = null;
        var longitude = null;

        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(function (position) {
                latitude = position.coords.latitude;
                longitude = position.coords.longitude;
                success= true;
                var center = new google.maps.LatLng(latitude, longitude);
                google_map.map.panTo(center);
                setTimeout("google_map.map.setZoom(7)",1000);
                ajax_locate_me_stats(success, latitude, longitude);

            });
        } else {
            x.innerHTML = "Geolocation is not supported by this browser.";
            ajax_locate_me_stats(success, latitude, longitude);
        }
    }
};

function initialize(geoloc) {
    //To center map on markers
    var bounds = new google.maps.LatLngBounds();

    var mapCanvas = document.getElementById('map');
	
	
    var mapOptions = {
		minZoom: 3,
		gestureHandling: 'greedy',

        mapTypeId: google.maps.MapTypeId.ROADMAP,
        mapTypeControl: false,
        zoomControl: true,
        zoomControlOptions: {
            position: google.maps.ControlPosition.LEFT_CENTER
        },
        scaleControl: true,
        streetViewControl: true,
        streetViewControlOptions: {
            position: google.maps.ControlPosition.LEFT_CENTER
        }
    };
    google_map.map = new google.maps.Map(mapCanvas, mapOptions);
    var markers = [];
    var icon = '/frontend_listing/static/src/marker.svg';
    var iconStudio = '/frontend_listing/static/src/marker-studio.svg';


    //INFOWINDOWS
    var infowindow = new google.maps.InfoWindow({
        //content: contentString,
        width: 250,
        maxWidth: 300
    });


    jQuery.each(geoloc, function (i, val) {
        var contentString = '<div id="content">' + val[2] + '</div>';

        var marker = new google.maps.Marker({
            position: {lat: val[0], lng: val[1]},
            map: google_map.map,
            icon: iconStudio,
            title: i
        });

        //extend the bounds to include each marker's position
        bounds.extend(marker.position);
        markers.push(marker);

        google.maps.event.addListener(marker, 'click', function () {
            infowindow.setContent(contentString);
            infowindow.open(google_map.map, marker);
        });

    });

    var clusterStyles = [
        {
            textColor: '#f1f1f3',
            url: icon,
            textSize: 18,
            height: 48,
            width: 48
        }
    ];

    var mcOptions = {
        gridSize: 50,
        styles: clusterStyles,
        maxZoom: 15
    };

    var mc = new MarkerClusterer(google_map.map, markers, mcOptions);
    //now fit the map to the newly inclusive bounds
    google_map.map.fitBounds(bounds);
    google_map.map.setOptions({styles: snazzy_theme()});


}

google.maps.event.addDomListener(window, 'load', initialize);
