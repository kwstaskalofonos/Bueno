$( document ).ready(function() {
	$('#AjaxForm').on('submit',function(event){
		event.preventDefault();
		$.ajax({
			url:'/ajax/AjaxCall/',
			data:{
				name:'worked'
			},
			datatype:'json',
			success:function(data){
				alert('worked');
			},
			error:function(xhr,errmsg,err){
				alert('faileld');
			}
		});
	});
});
