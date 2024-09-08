(function ($) {
    "use strict";

// active nav item
    const navItem = document.getElementsByClassName("nav-link");
    for (const element of navItem) {
        element.addEventListener("click", () => {
            for (const ele of navItem) {
                ele.classList.remove("active");
            }
            element.classList.add("active");
        });
    }

// tab
    const tabs = document.getElementsByClassName("tab");
    const contents = document.getElementsByClassName("content");
    for (const element of tabs) {
        const tabId = element.getAttribute("tab-id");
        const content = document.getElementById(tabId);
        element.addEventListener("click", () => {
            for (const t of tabs) {
                t.classList.remove("active");
            }
            for (const c of contents) {
                c.classList.remove("active");
            }
            element.classList.add("active");
            content.classList.add("active");
        });
    }

// input file preview
    const previewImage = (id) => {
        document.getElementById(id).src = URL.createObjectURL(event.target.files[0]);
    };



    $(document).ready(function () {
        // owl carousel
        $(".testimonials").owlCarousel({
            loop: true,
            margin: 25,
            nav: false,
            dots: true,
            autoplay: true,
            autoplayTimeout: 3000,
            responsive: {
                0: {
                    items: 1,
                },
                768: {
                    items: 1,
                },
                992: {
                    items: 2,
                },
            },
        });

        $("#shareBlock").socialSharingPlugin({
            urlShare: window.location.href,
            description: $("meta[name=description]").attr("content"),
            title: $("title").text(),
        });

        // AOS ANIMATION
        AOS.init();

        // SCROLL TOP
        $(".scroll-up").fadeOut();
        $(window).scroll(function () {
            if ($(this).scrollTop() > 100) {
                $(".scroll-up").fadeIn();
            } else {
                $(".scroll-up").fadeOut();
            }
        });
    });


    /*--------------- Start extra JS added by me ------------------*/

// Cookies & Privacy
    if (localStorage.getItem('cookie-value') == 1 || sessionStorage.getItem('cookie-value') == 1) {
        $('.cookie-content').remove();
    } else {
        $('.cookie-content').removeClass('d-none');
    }

    $('#cookie-accept').on("click", function () {
        localStorage.setItem('cookie-value', 1);
        sessionStorage.removeItem('cookie-value');
        $('.cookie-content').remove();
    });

    $('#cookie-deny').on("click", function () {
        sessionStorage.setItem('cookie-value', 1);
        localStorage.removeItem('cookie-value');
        $('.cookie-content').remove();
    });
})(jQuery);

