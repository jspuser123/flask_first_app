$(document).ready(function(){




    $('#data').DataTable();


      var dialog = document.getElementById('myFirstDialog');    
      document.getElementById('show').onclick = function() {    
          dialog.show();    
      };    
      document.getElementById('hide').onclick = function() {    
          dialog.close();    
      };  

      // $('#myModal').on('shown.bs.modal', function () {
      //   $('#model').trigger('focus')
      // })

});
