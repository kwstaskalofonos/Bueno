$( document ).ready(function() {
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
			$('#exampleModal').on('hidden.bs.modal',function(e){
				$('#message-text').val('');
				$('#quantity').val('1');
			});

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
		var crepes = [];
		$('.add_product').click(function(){
			var product_title = $(this).closest('.modal-content').children('.modal-header').children('.modal-title').text();
			var product_desc = $(this).closest('.modal-content').children('.modal-body').children('.modal-description').text();
			var product_price = $(this).closest('.modal-content').children('.modal-body').children('.fa-eur').text();
			var product_comments = $('#message-text').val();
			var product_quan = $('#quantity').val();
			var total_price = parseFloat(product_price)*parseFloat(product_quan);
			var crepe = {
				title:product_title,
				desc:product_desc,
				comments:product_comments,
				quantity:product_quan,
				price:total_price
			};
			
			crepes.push(crepe)
			console.log(crepes);
		});
		});