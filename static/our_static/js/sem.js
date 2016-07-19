$(document).ready(function(){
  $('#b').click(function(){
    alert(Hi);
    $('.ui.sidebar')
      .sidebar('toggle')
  });
});
    /*$(".launch.button").mouseenter(function() {
    $(this).stop().animate({
        width: '150px'
      }, 300,
      function() {
        $(this).find('.text').show();
      });
  }).mouseleave(function(event) {
    $(this).find('.text').hide();
    $(this).stop().animate({
      width: '70px'
    }, 300);
  });
  $(".ui.sidebar").sidebar()
    .sidebar('attach events', '.ui.launch.button');
    });

});*/