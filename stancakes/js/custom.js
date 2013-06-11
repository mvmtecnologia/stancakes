/**
 * @author vinicius soliva
 * @author matheus cardoso
 */
jQuery(function($) {

	$("#slist a").click(function(e) {
		e.preventDefault();
		$(this).next('p').toggle(200);
	});

	$('#filters a').click(function() {
		var selector = $(this).attr('data-filter');
		$container.isotope({
			filter : selector
		});
		return false;
	});

	$("a[class^='prettyPhoto']").prettyPhoto({
		overlay_gallery : false,
		social_tools : false
	});

});
