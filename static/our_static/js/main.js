$(function(){
	$('a.item').click(function(){
		alert('hello');
		$('.item').removeClass('active');
	$(this).addClass('active');
});
});
