function initMap() {
    var myLatLng = {lat: 18.415991, lng: -66.162384};

    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 14,
        center: myLatLng
    });

    var image = '/static/img/empire.png';

    var beachMarker = new google.maps.Marker({
        position: myLatLng,
        map: map,
        icon: image,
    });

    var contentString = "<div style='color: black;'> <h4>Real Empire Studio</h4>"
                        + "<table>"
                        + "<!--<tr><th>Dirección:</th><td></td></tr>-->"
                        + "<tr><th>Teléfono:<th><td>787-631-0059</td></tr>"
                        + "<tr><th>Email:<th><td>jefnielestrada@gmail.com</td></tr>"
                        + "</table>"
                        + "</div>"

    var infowindow = new google.maps.InfoWindow({
        content: contentString,
    });


    google.maps.event.addListener(beachMarker, 'click', function() {
       infowindow.open(map,beachMarker);
    });
    infowindow.open(map,beachMarker);

    $("#map").click(function(){
    // If it's an iPhone..
    if( (navigator.platform.indexOf("iPhone") != -1) 
        || (navigator.platform.indexOf("iPod") != -1)
        || (navigator.platform.indexOf("iPad") != -1))
         window.open("maps://maps.google.com/maps?q=18.415991,-66.162384");
    else
         window.open("http://maps.google.com/maps?q=18.415991,-66.162384");
});
}
