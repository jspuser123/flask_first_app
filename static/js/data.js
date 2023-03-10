$(document).ready(function(){
    $('#data').DataTable();

   
    
 

      var dialog = document.getElementById('myFirstDialog');    
      document.getElementById('show').onclick = function() {    
          dialog.show();    
      };    
      document.getElementById('hide').onclick = function() {    
          dialog.close();    
      };  

 
      var dialog = document.getElementById('secDialog');    
      document.getElementById('edit1').onclick = function() {    
          dialog.show();    
      }; 

      document.getElementById('hide1').onclick = function() {    
        dialog.close();    
    }; 

});