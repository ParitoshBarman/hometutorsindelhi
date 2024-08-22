/****************************************************************************************
||||||||||||||||||||||||||||     TABLE OF CONTENT  for JS    ||||||||||||||||||
*****************************************************************************************
* 1. Search box open
* 2. Scroll page
* 3. Animate the scroll to top
* 4. Video Popup
* 5. Slider operator
* 6. Mobile menu dropdown
* 7. Nice Select
* 8. Progressbar animation 

******************************************************************************/
(function ($) {
    "use strict";

    jQuery(document).ready(function ($) {
        if ($('.form-teart').is(':visible')) {
            $('select').niceSelect();

        }

        $(window).on('scroll', function () {
            var scroll = $(window).scrollTop();
            if (scroll < 100) {
                $(".header-middle").removeClass("scroll-header")
            } else {
                $(".header-middle").addClass("scroll-header");
            }

        });
	/*
	* 1. Search Box Open
	*/
        $('.ccdda, .ssdf').click(function () {

            $('.searchh').toggleClass('activee');
            $('.ccdda').toggleClass('toggle');
        });
	/*
	* 2. Scroll page
	*/
        $(window).scroll(function () {
            if ($(this).scrollTop() > 200) {
                $('.go-top').fadeIn(200);
            } else {
                $('.go-top').fadeOut(200);
            }
        });

	/*
	* 3. Animate the scroll to top
	*/
        $('.go-top').click(function (event) {
            event.preventDefault();

            $('html, body').animate({
                scrollTop: 0
            }, 800);
        })
		
    /*
	* 4. Video Popup
	*/
        $('.video-popup').magnificPopup({
            type: 'iframe',
            iframe: {
                markup: '<div class="mfp-iframe-scaler">' +
                    '<div class="mfp-close"></div>' +
                    '<iframe class="mfp-iframe" frameborder="0" allowfullscreen></iframe>' +
                    '</div>', // HTML markup of popup, `mfp-close` will be replaced by the close button

                patterns: {
                    youtube: {
                        index: 'youtube.com/', // String that detects type of video (in this case YouTube). Simply via url.indexOf(index).

                        id: 'v=', // String that splits URL in a two parts, second part should be %id%
                        // Or null - full URL will be returned
                        // Or a function that should return %id%, for example:
                        // id: function(url) { return 'parsed id'; }

                        src: 'https://www.youtube.com/embed/%id%?autoplay=1' // URL that will be set as a source for iframe.
                    },
                    vimeo: {
                        index: 'vimeo.com/',
                        id: '/',
                        src: '//player.vimeo.com/video/%id%?autoplay=1'
                    },
                    gmaps: {
                        index: '//maps.google.',
                        src: '%id%&output=embed'
                    }

                    // you may add here more sources

                },

                srcAction: 'iframe_src', // Templating object key. First part defines CSS selector, second attribute. "iframe_src" means: find "iframe" and set attribute "src".
            }
        });

    /*
	* 5. Slider operator
	*/
        $(".single-slider-active").owlCarousel({
            items: 1,
            nav: false,
            dot: false,
            loop: true,
            center: true,
            margin: 20,
            autoplay: true,
            autoplayTimeout: 3000,
            smartSpeed: 1000,
            responsiveClass: true,
            responsive: {
                0: {
                    items: 1,

                },
                481: {
                    items: 1,

                },
                1000: {
                    items: 3,

                }
            }
        });


        $(".view-slider").owlCarousel({
            items: 5,
            nav: true,
            dot: false,
            loop: true,
            margin: 20,
            autoplay: false,
            autoplayTimeout: 3000,
            smartSpeed: 1000,
            responsiveClass: true,
            responsive: {
                0: {
                    items: 1,
                },
                768: {
                    items: 3,
                },
                1000: {
                    items: 4,
                }
            }

        });

        $(".happy-slider").owlCarousel({
            items: 1,
            nav: false,
            dot: false,
            navText: ['<i class="fal fa-angle-left"></i>', '<i class="fal fa-angle-right"></i>'],
            loop: true,
            margin: 10,
            autoplay: true,
            autoplayTimeout: 3000,
            smartSpeed: 1000,
            responsiveClass: true,
            responsive: {
                0: {
                    items: 1,
                    stagePadding: 0,

                },
                768: {
                    items: 2,
                    stagePadding: 0,

                },
                1000: {
                    items: 3,
                    stagePadding: 100,
                    stagePadding: 0,

                },
                1740: {
                    items: 3,
                    stagePadding: 0,

                },
            }

        });
		
	/*
	* 6. Mobile menu dropdown
	*/
        jQuery('ul i').on('click', function () {
            jQuery(this).toggleClass('DDopen');
            jQuery(this).closest('ul').find('ul').removeClass('opened');
            jQuery(this).parent().find('> ul').addClass('opened');
            jQuery(this).closest('ul').find('ul').not('.opened').slideUp(350);
            jQuery(this).parent().find('> ul').slideToggle(350);
            jQuery(this).closest('ul').find('i').not(this).removeClass('DDopen');
        });


        if ($('#datepicker').is(':visible')) {
            $('#datepicker').datepicker({
                uiLibrary: 'bootstrap4'
            });
        }


    });

/*
* 7. Nice Select
*/
    if ($('.shop-qty').is(':visible')) {
        $('select').niceSelect();
    }

/*
* 8. Progressbar animation 
*/
    var web_designprogresbar = jQuery('.progressbar-area');

    jQuery(window).on('scroll', function () {
        var winT = jQuery(window).scrollTop(),
            winH = jQuery(window).height();


        if (web_designprogresbar.length)
            var webdesignT = web_designprogresbar.offset().top;
        if (winT + winH > webdesignT) {
            jQuery('.single-circle-progressber').each(function () {
                $("#web-designprogressbar").circleProgress({
                        value: 0.75,
                        size: 150,
                        fill: '#072264'
                    })
                    .on('circle-animation-progress', function (event, progress) {
                        $(this).find('.progressbar-percentage').html(Math.round(85 * progress) + '<i>%</i>');

                    });
                $("#Happy-designprogressbar").circleProgress({
                        value: 0.75,
                        size: 150,
                        fill: '#072264'
                    })
                    .on('circle-animation-progress', function (event, progress) {
                        $(this).find('.progressbar-percentage').html(Math.round(40 * progress) + '<i>%</i>');

                    });
                $("#Quick-designprogressbar").circleProgress({
                        value: 0.75,
                        size: 150,
                        fill: '#072264'
                    })
                    .on('circle-animation-progress', function (event, progress) {
                        $(this).find('.progressbar-percentage').html(Math.round(75 * progress) + '<i>%</i>');

                    });
                $("#Experience-designprogressbar").circleProgress({
                        value: 0.75,
                        size: 150,
                        fill: '#072264'
                    })
                    .on('circle-animation-progress', function (event, progress) {
                        $(this).find('.progressbar-percentage').html(Math.round(100 * progress) + '<i>%</i>');

                    });
            });
        }
    });

}(jQuery));