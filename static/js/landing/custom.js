/******************************************************************************************************************************
COMMING SOON PAGE
*******************************************************************************************************************************/
(function($) {
    /**
    * Set your date here  (YEAR, MONTH (0 for January/11 for December), DAY, HOUR, MINUTE, SECOND)
    * according to the GMT+0 Timezone
    **/
    var launch = new Date(2015, 9, 10, 9, 00);
    /**
    * The script
    **/
    var message = $('#message');
    var days = $('#days');
    var hours = $('#hours');
    var minutes = $('#minutes');
    var seconds = $('#seconds');
    
    setDate();
    function setDate(){
        var now = new Date();
        if( launch < now ){
            days.html('<h2>0</h2><p>Día</p>');
            hours.html('<h2>0</h2><p>Hora</p>');
            minutes.html('<h2>0</h2><p>Minuto</p>');
            seconds.html('<h2>0</h2><p>Segundo</p>');
            // message.html('Mantengase al tanto!');
        }
        else{
            var s = -now.getTimezoneOffset()*60 + (launch.getTime() - now.getTime())/1000;
            var d = Math.floor(s/86400);
            days.html('<h2>'+d+'</h2><p>Día'+(d>1?'s':''),'</p>');
            s -= d*86400;

            var h = Math.floor(s/3600);
            hours.html('<h2>'+h+'</h2><p>Hora'+(h>1?'s':''),'</p>');
            s -= h*3600;

            var m = Math.floor(s/60);
            minutes.html('<h2>'+m+'</h2><p>Minuto'+(m>1?'s':''),'</p>');

            s = Math.floor(s-m*60);
            seconds.html('<h2>'+s+'</h2><p>Segundo'+(s>1?'s':''),'</p>');
            setTimeout(setDate, 1000);

            // message.html('MAntengase al tanto!');
        }
    }
})(jQuery);
/******************************************************************************************************************************
ANIMATIONS
*******************************************************************************************************************************/
(function($) {
    "use strict";
    var isMobile = false;
    if (navigator.userAgent.match(/Android/i) || 
        navigator.userAgent.match(/webOS/i) ||
        navigator.userAgent.match(/iPhone/i) || 
        navigator.userAgent.match(/iPad/i)|| 
        navigator.userAgent.match(/iPod/i) || 
        navigator.userAgent.match(/BlackBerry/i)) {                 
        isMobile = true;            
    }
    if (isMobile == true) {
        $('body').removeClass('nomobile');
        $('.animated').removeClass('animated');
    }
    $(function() {
        if (isMobile == false) {
            $('*[data-animated]').addClass('animated');
        }
        function animated_contents() {
            $(".animated:appeared").each(function (i) {
                var $this    = $(this),
                    animated = $(this).data('animated');

                setTimeout(function () {
                    $this.addClass(animated);
                }, 50 * i);
            });
        }
        animated_contents();
        $(window).scroll(function () {
            animated_contents();
        });
    });
})(jQuery);