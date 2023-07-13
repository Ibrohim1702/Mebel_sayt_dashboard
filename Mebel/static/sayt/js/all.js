$(document).ready(function () {
	
	// mob nav
	$(document).on('click','.mob-nav-icon',function(e){
		e.preventDefault();
		if($(this).hasClass('active')){
			$('.header-nav-list').removeClass('vis');
			$('.mob-nav-icon').removeClass('active');
		}else{
			$('.header-nav-list').addClass('vis');
			$('.mob-nav-icon').addClass('active');
		}
	});

	// scroll
	if ($(this).scrollTop() > 0){
		$('.header-fixed').addClass('fixed');
	}else{
		$('.header-fixed').removeClass('fixed');
	}
	$(window).scroll( function(){
		if ($(this).scrollTop() > 0){
			$('.header-fixed').addClass('fixed');
		}else{
			$('.header-fixed').removeClass('fixed');
		}
	});	
	$('.scroll').click(function(e){
		e.preventDefault();
		var selected = $(this).attr('href').replace('/', '');
		$.scrollTo(selected, 1000, {offset: -70});
		return false;
	});

	// catalog nav mobile
	$(document).on('click','.filter-top',function(e){
		e.preventDefault();
		if($(this).hasClass('active')){
			$('.filter-hidden').slideUp();
			$('.filter-top').removeClass('active');
		}else{
			$('.filter-hidden').slideUp();
			$('.filter-top').removeClass('active');
			$(this).parent().find('.filter-hidden').slideDown();
			$(this).addClass('active');
		}
	});

	// partners slider
	$('.banner-slider').slick({
		dots: false,
		arrows: false,
		autoplay: true,
		speed: 1500,
		slidesToShow: 1,
		slidesToScroll: 1,
	});
	$('.catalog-img').slick({
		dots: false,
		arrows: true,
		autoplay: false,
		speed: 1500,
		slidesToShow: 1,
		slidesToScroll: 1,
	});
	$('.photo-slider').slick({
		dots: false,
		arrows: true,
		autoplay: false,
		speed: 1500,
		slidesToShow: 1,
		slidesToScroll: 1,
		asNavFor: '.thumbs-slider',
	});
	$('.thumbs-slider').slick({
		dots: false,
		arrows: false,
		autoplay: false,
		vertical: true,
		speed: 1500,
		slidesToShow: 5,
		slidesToScroll: 5,
		focusOnSelect: true,
		asNavFor: '.photo-slider',
		responsive: [
			{
				breakpoint: 1200,
				settings: {
					vertical: false,
				}
			},{
				breakpoint: 576,
				settings: {
					vertical: false,
					slidesToShow: 3,
					slidesToScroll: 3,
				}
			}
		]
	});
	$('.compare-slider').slick({
		dots: false,
		arrows: true,
		autoplay: false,
		speed: 1000,
		slidesToShow: 4,
		slidesToScroll: 1,
		prevArrow: $('.compare-prev'),
		nextArrow: $('.compare-next'),
		responsive: [
			{
				breakpoint: 1300,
				settings: {
				  slidesToShow: 3,
				}
			},{
				breakpoint: 1200,
				settings: {
				  slidesToShow: 2,
				}
			},{
				breakpoint: 576,
				settings: {
				  slidesToShow: 1,
				}
			}
		]
	});
	$('.catalog-slider').slick({
		dots: false,
		arrows: true,
		autoplay: false,
		speed: 1000,
		infinite: false,
		slidesToShow: 4,
		slidesToScroll: 1,
		responsive: [
			{
				breakpoint: 1200,
				settings: {
				  slidesToShow: 3,
				}
			},{
				breakpoint: 1024,
				settings: {
				  slidesToShow: 2,
				}
			},{
				breakpoint: 480,
				settings: {
				  slidesToShow: 1,
				}
			}
		]
	});

	// quantity input
	$(document).on('click', '.minus', function () {
		var $input = $(this).parent().find('.quantity-input');
		var count = parseInt($input.val()) - 1;
		count = count < 1 ? 1 : count;
		$input.val(count);
		$input.change();
		return false;
	});
	$(document).on('click', '.plus', function () {
		var $input = $(this).parent().find('.quantity-input');
		$input.val(parseInt($input.val()) + 1);
		$input.change();
		return false;
	});

	/*---------------------------------
		Tabs
	-----------------------------------*/
	// tab setup
	$('.tab-content').addClass('clearfix').not(':first').hide();
	$('ul.tabs').each(function(){
		var current = $(this).find('li.active');
		if(current.length < 1) { $(this).find('li:first').addClass('active'); }
		current = $(this).find('li.active a').attr('href');
		$(current).show();
	});
	
	// tab click
	$(document).on('click', 'ul.tabs a[href^="#"]', function(e){
		e.preventDefault();
		var tabs = $(this).parents('ul.tabs').find('li');
		var tab_next = $(this).attr('href');
		var tab_current = tabs.filter('.active').find('a').attr('href');
		$(tab_current).hide();
		tabs.removeClass('active');
		$(this).parent().addClass('active');
		$(tab_next).show();		
		return false;
	});

	// delivery checkbox change
	var delivery1 = $('#delivery1');
	var delivery2 = $('#delivery2');
	$(delivery1).change(function() {
		if ($(this).is(":checked")){
			$('#payment1').prop("checked", true);
		}
	}); 
	$(delivery2).change(function() {
		if ($(this).is(":checked")){
			$('#payment2').prop("checked", true);
		}
	}); 

});