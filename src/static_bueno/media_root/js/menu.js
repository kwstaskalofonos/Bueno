
$( document ).ready(function() {
	//Ready crepes modal
	$('.modalbtn').click(function(e){
		$(this).addClass('clicked');
		var title = $('.clicked').closest('.d-flex').children('strong').text();
		var desc = $('.clicked').closest('.d-flex').closest('.media-body').children('.desc').text();
		var price = $('.clicked').closest('.d-flex').closest('.media-body').children('.price').text();
		$('#exampleModal').find('.modal-title').text(title);
		$('#exampleModal').find('.modal-description').text(desc);
		$('#exampleModal').find('.price').text(price);
		$('#exampleModal').modal('show');
		$('.clicked').removeClass('clicked');
	});
	// Custom crepes modal
	$('.customCrepes').click(function(e){
		$('#customProductModal').modal('show');
		if($(this).attr("value")=='salt'){
			$('#customProductModal').find('.modal-title').text('Φτιάξε την αλμυρή της επιλογής σου');
		}else{
			$('#customProductModal').find('.modal-title').text('Φτιάξε την γλυκία της επιλογής σου');
		}
	});
	// Clear modal fields after close
	$('#exampleModal').on('hidden.bs.modal',function(e){
		$('#message-text').val('');
		$('#quantity').val('1');
	});
	// Redirect  function
	$('sweet3 a').on('click', function(event) {
		if (this.hash !=="") {
			event.preventDefault();
			const hash = this.hash;
			$('html, body').animate({
				scrollTop: $(hash).offset().top
			        }, 800, function() {
			          window.location.hash = hash;
			        });
			      }
	});

	$('.custom-control-input').change(function(){
		$(this).prop('interminate',true);
	});	

});
