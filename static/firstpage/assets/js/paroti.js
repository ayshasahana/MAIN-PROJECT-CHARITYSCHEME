(function ($) {
	"use strict";
	if ($('.niceselect').length) {
		$('.niceselect').niceSelect();
	}
	if ($('.lettering-text').length) {
		$('.lettering-text').lettering();
	}
	if ($(".video-popup").length) {
		$('.video-popup').YouTubePopUp();
	}
	if ($(".count-bar").length) {
		$(".count-bar").appear(
			function () {
				var el = $(this);
				var percent = el.data("percent");
				$(el).css("width", percent).addClass("counted");
			}, {
				accY: -50
			}
		);
	}
	if ($(".count-bar--no-appear").length) {
		$(".count-bar--no-appear").each(
			function () {
				var el = $(this);
				var percent = el.data("percent");
				$(el).css("width", percent).addClass("counted");
			}
		);
	}
	//Fact Counter + Text Count
	if ($(".count-box").length) {
		$(".count-box").appear(
			function () {
				var $t = $(this),
					n = $t.find(".count-text").attr("data-stop"),
					r = parseInt($t.find(".count-text").attr("data-speed"), 10);

				if (!$t.hasClass("counted")) {
					$t.addClass("counted");
					$({
						countNum: $t.find(".count-text").text()
					}).animate({
						countNum: n
					}, {
						duration: r,
						easing: "linear",
						step: function () {
							$t.find(".count-text").text(Math.floor(this.countNum));
						},
						complete: function () {
							$t.find(".count-text").text(this.countNum);
						}
					});
				}
			}, {
				accY: 0
			}
		);
	}
	if ($(".accrodion-grp").length) {
		var accrodionGrp = $(".accrodion-grp");
		accrodionGrp.each(function () {
			var accrodionName = $(this).data("grp-name");
			var Self = $(this);
			var accordion = Self.find(".accrodion");
			Self.addClass(accrodionName);
			Self.find(".accrodion .accrodion-content").hide();
			Self.find(".accrodion.active").find(".accrodion-content").show();
			accordion.each(function () {
				$(this)
					.find(".accrodion-title")
					.on("click", function () {
						if ($(this).parent().hasClass("active") === false) {
							$(".accrodion-grp." + accrodionName)
								.find(".accrodion")
								.removeClass("active");
							$(".accrodion-grp." + accrodionName)
								.find(".accrodion")
								.find(".accrodion-content")
								.slideUp();
							$(this).parent().addClass("active");
							$(this).parent().find(".accrodion-content").slideDown();
						}
					});
			});
		});
	}


	let thmTnsCarousels = $(".thm-tns__carousel");
	if (thmTnsCarousels.length) {
		thmTnsCarousels.each(function () {
			let elm = $(this);
			let options = elm.data("tns-options");
			let thmTnsCarousels = tns(
				"object" === typeof options ? options : JSON.parse(options)
			);
		});
	}

	let thmOwlCarousels = $(".thm-owl__carousel");
	if (thmOwlCarousels.length) {
		thmOwlCarousels.each(function () {
			let elm = $(this);
			let options = elm.data("owl-options");
			let thmOwlCarousel = elm.owlCarousel(
				"object" === typeof options ? options : JSON.parse(options)
			);
		});
	}

	let thmOwlNavCarousels = $(".thm-owl__carousel--custom-nav");
	if (thmOwlNavCarousels.length) {
		thmOwlNavCarousels.each(function () {
			let elm = $(this);
			let owlNavPrev = elm.data("owl-nav-prev");
			let owlNavNext = elm.data("owl-nav-next");
			$(owlNavPrev).on("click", function (e) {
				elm.trigger("prev.owl.carousel");
				e.preventDefault();
			});

			$(owlNavNext).on("click", function (e) {
				elm.trigger("next.owl.carousel");
				e.preventDefault();
			});
		});
	}

	if ($(".img-popup").length) {
		var groups = {};
		$(".img-popup").each(function () {
			var id = parseInt($(this).attr("data-group"), 10);

			if (!groups[id]) {
				groups[id] = [];
			}

			groups[id].push(this);
		});

		$.each(groups, function () {
			$(this).magnificPopup({
				type: "image",
				closeOnContentClick: true,
				closeBtnInside: false,
				gallery: {
					enabled: true
				}
			});
		});
	}


	// mailchimp form
	if ($(".mc-form").length) {
		$(".mc-form").each(function () {
			var Self = $(this);
			var mcURL = Self.data("url");
			var mcResp = Self.parent().find(".mc-form__response");

			Self.ajaxChimp({
				url: mcURL,
				callback: function (resp) {
					// appending response
					mcResp.append(function () {
						return '<p class="mc-message">' + resp.msg + "</p>";
					});
					// making things based on response
					if (resp.result === "success") {
						// Do stuff
						Self.removeClass("errored").addClass("successed");
						mcResp.removeClass("errored").addClass("successed");
						Self.find("input").val("");

						mcResp.find("p").fadeOut(10000);
					}
					if (resp.result === "error") {
						Self.removeClass("successed").addClass("errored");
						mcResp.removeClass("successed").addClass("errored");
						Self.find("input").val("");

						mcResp.find("p").fadeOut(10000);
					}
				}
			});
		});
	}

	if ($(".contact-form-validated").length) {
		$(".contact-form-validated").each(function () {
			let contactForm = $(this);
			contactForm.validate({
				// initialize the plugin
				rules: {
					name: {
						required: true
					},
					phone: {
						required: true
					},
					email: {
						required: true,
						email: true
					},
					message: {
						required: true
					},
					subject: {
						required: true
					}
				},
				submitHandler: function (form) {
					// sending value with ajax request
					$.post(
						$(form).attr("action"),
						$(form).serialize(),
						function (response) {
							$(form).parent().find(".result").append(response);
							$(form).find('input[type="text"]').val("");
							$(form).find('input[type="email"]').val("");
							$(form).find("textarea").val("");
						}
					);
					return false;
				}
			});
		});
	}

	function dynamicCurrentMenuClass(selector) {
		let FileName = window.location.href.split("/").reverse()[0];

		selector.find("li").each(function () {
			let anchor = $(this).find("a");
			if ($(anchor).attr("href") == FileName) {
				$(this).addClass("current");
			}
		});
		// if any li has .current elmnt add class
		selector.children("li").each(function () {
			if ($(this).find(".current").length) {
				$(this).addClass("current");
			}
		});
		// if no file name return
		if ("" == FileName) {
			selector.find("li").eq(0).addClass("current");
		}
	}

	if ($(".main-menu__list").length) {
		// dynamic current class
		let mainNavUL = $(".main-menu__list");
		dynamicCurrentMenuClass(mainNavUL);
	}

	if ($(".main-menu__list").length && $(".mobile-nav__container").length) {
		$(".main-menu__list").clone().removeClass('main-menu__list').addClass('mobile-menu__list').appendTo('.mobile-nav__container');
	}
	if ($(".sticky-header").length) {
		$(".sticky-header").clone().insertAfter('.sticky-header').addClass('sticky-header--cloned');
	}

	if ($(".mobile-menu__list").length) {
		let dropdownAnchor = $(".mobile-menu__list .menu-item-has-children > a");
		dropdownAnchor.each(function () {
			let self = $(this);
			let toggleBtn = document.createElement("BUTTON");
			toggleBtn.setAttribute("aria-label", "dropdown toggler");
			toggleBtn.innerHTML = "<i class='fa fa-angle-down'></i>";
			self.append(function () {
				return toggleBtn;
			});
			self.find("button").on("click", function (e) {
				e.preventDefault();
				let self = $(this);
				self.toggleClass("expanded");
				self.parent().toggleClass("expanded");
				self.parent().parent().children("ul").slideToggle();
			});
		});
	}

	if ($(".mobile-nav__toggler").length) {
		$(".mobile-nav__toggler").on("click", function (e) {
			e.preventDefault();
			$(".mobile-nav__wrapper").toggleClass("expanded");
			$("body").toggleClass("locked");
		});
	}

	if ($(".search-toggler").length) {
		$(".search-toggler").on("click", function (e) {
			e.preventDefault();
			$(".search-popup").toggleClass("active");
			$(".mobile-nav__wrapper").removeClass("expanded");
			$("body").toggleClass("locked");
		});
	}

	if ($(".scroll-to-target").length) {
		$(".scroll-to-target").on("click", function () {
			var target = $(this).attr("data-target");
			$("html, body").animate({
					scrollTop: $(target).offset().top,
				},
				1000
			);
			return false;
		});
	}
	if ($(".dynamic-year").length) {
		let currentYear = new Date().getFullYear();
		$(".dynamic-year").html(currentYear);
	}
	if ($(".wow").length) {
		var wow = new WOW({
			boxClass: "wow", // animated element css class (default is wow)
			animateClass: "animated", // animation css class (default is animated)
			mobile: true, // trigger animations on mobile devices (default is true)
			live: true // act on asynchronously loaded content (default is true)
		});
		wow.init();
	}
	// custom coursor
	if ($(".custom-cursor").length) {
		var cursor = document.querySelector(".custom-cursor__cursor");
		var cursorinner = document.querySelector(".custom-cursor__cursor-two");
		var a = document.querySelectorAll("a");

		document.addEventListener("mousemove", function (e) {
			var x = e.clientX;
			var y = e.clientY;
			cursor.style.transform = `translate3d(calc(${e.clientX}px - 50%), calc(${e.clientY}px - 50%), 0)`;
		});

		document.addEventListener("mousemove", function (e) {
			var x = e.clientX;
			var y = e.clientY;
			cursorinner.style.left = x + "px";
			cursorinner.style.top = y + "px";
		});

		document.addEventListener("mousedown", function () {
			cursor.classList.add("click");
			cursorinner.classList.add("custom-cursor__innerhover");
		});

		document.addEventListener("mouseup", function () {
			cursor.classList.remove("click");
			cursorinner.classList.remove("custom-cursor__innerhover");
		});

		a.forEach((item) => {
			item.addEventListener("mouseover", () => {
				cursor.classList.add("custom-cursor__hover");
			});
			item.addEventListener("mouseleave", () => {
				cursor.classList.remove("custom-cursor__hover");
			});
		});
	}

	function testimonialsThumbCarousel() {
		if ($("#testimonials-two__thumb").length) {
			let testimonialsThumb = new Swiper("#testimonials-two__thumb", {
				slidesPerView: 3,
				spaceBetween: 10,
				speed: 1400,
				direction: 'vertical',
				watchSlidesVisibility: true,
				watchSlidesProgress: true,
				autoplay: {
					delay: 5000
				}
			});

			let testimonialsCarousel = new Swiper("#testimonials-two__carousel", {
				observer: true,
				observeParents: true,
				speed: 1400,
				mousewheel: false,
				slidesPerView: 1,
				autoplay: {
					delay: 5000
				},
				thumbs: {
					swiper: testimonialsThumb
				},
				pagination: {
					el: '#testimonials-two__carousel-pagination',
					type: 'bullets',
					clickable: true
				},
			});
		}
	}

	$(window).on("scroll", function () {
		if ($(".sticky-header--cloned").length) {
			var headerScrollPos = 130;
			var stricky = $(".sticky-header--cloned");
			if ($(window).scrollTop() > headerScrollPos) {
				stricky.addClass("sticky-fixed");
			} else if ($(this).scrollTop() <= headerScrollPos) {
				stricky.removeClass("sticky-fixed");
			}
		}
		if ($(".scroll-to-top").length) {
			var strickyScrollPos = 100;
			if ($(window).scrollTop() > strickyScrollPos) {
				$(".scroll-to-top").fadeIn(500);
			} else if ($(this).scrollTop() <= strickyScrollPos) {
				$(".scroll-to-top").fadeOut(500);
			}
		}

	});

	$(window).on("load", function () {
		if ($(".preloader").length) {
			$(".preloader").fadeOut();
		}

		if ($(".circle-progress").length) {
			$(".circle-progress").appear(function () {
				let circleProgress = $(".circle-progress");
				circleProgress.each(function () {
					let progress = $(this);
					let progressOptions = progress.data("options");
					progress.circleProgress(progressOptions);
				});
			});
		}
		testimonialsThumbCarousel();
	});
})(jQuery);