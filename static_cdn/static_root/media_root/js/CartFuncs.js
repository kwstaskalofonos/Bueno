$( document ).ready(function() {
	updateCartView();
	// Add ready products to cart
	var crepes = [];
	loadCart();
	$('.add_product').click(function(){
		var product_title = $(this).closest('.modal-content').children('.modal-header').children('.modal-title').text();
		var product_desc = $(this).closest('.modal-content').children('.modal-body').children('.modal-description').text();
		var product_price = $(this).closest('.modal-content').children('.modal-body').children('.fa-eur').text();
		var product_comments = $('#message-text').val();
		var product_quan = $('#quantity').val();
		var total_price = parseFloat(product_price)*parseInt(product_quan);
		var crepe = {
			title:product_title,
			desc:product_desc,
			comments:product_comments,
			quantity:product_quan,
			price:total_price
		};
		crepes.push(crepe);
		cartupdate(product_title,product_quan,total_price);
		//save cart to localStorage
		sessionStorage.setItem("shoppingCart",JSON.stringify(crepes));
	});

	//clear the cart
	$('.clear-cart').click(function(e){
		crepes = [];
		sessionStorage.clear();
		$('#cartList').children('li').remove();
		updateCartView();
	});

	function loadCart(){
		if(sessionStorage.length != 0){
			crepes = JSON.parse(sessionStorage.getItem("shoppingCart"));
		}
	}

	function updateCartView(){
		if(sessionStorage.length != 0){
			crepes = JSON.parse(sessionStorage.getItem("shoppingCart"));
			crepes.forEach(function(item,index){
				cartupdate(item.title,item.quantity,item.price)
				console.log(item);
				console.log(item.quantity)
			});
		}
	}

});

function cartupdate(title,quantity,price){
			listnode = document.getElementById('cartList');
			linode = document.createElement("LI");
			linode.className = "list-group-item d-flex justify-content-between";
			removenode = document.createElement("I");
			removenode.className = "fa fa-minus";
			posotita = document.createElement("I");
			posotita.className = "fa fa-times"
			linode.append(title);
			linode.append(posotita,quantity);
			linode.append(removenode); 
			listnode.appendChild(linode);
		}