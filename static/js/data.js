$(document).ready(function(){

    $("#btn3").click(function(){
		$("p").toggle();
	  });




      var dialog = document.getElementById('myFirstDialog');    
      document.getElementById('show').onclick = function() {    
          dialog.show();    
      };    
      document.getElementById('hide').onclick = function() {    
          dialog.close();    
      };  




});