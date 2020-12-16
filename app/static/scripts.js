function test() {
  alert("Funciona");
  return;   
}

$(document).ready(function(){
  $(document).on('keypress',function(e){
	if(e.which == 13){
		
		var a = $('#search').val();
		if(!a){
			return false;
		}else{
		      $.getJSON('/search_content', {
				query: $('#search').val()					
			  }, function(data) {		
				if(data.productos == 'error largo_query'){
					$('#productList').addClass('alert-warning');
					$('#productList').html('<strong>La búsqueda no puede tener menos de 2 caracteres si no son un identificador</strong>'); 
					$('#productList').fadeIn();
				}
				else{
					$('#productList').removeClass('alert-warning');
					$('#productList').html('');
	
					
					let list_html = $('#productList');
					
					first = 0;
					$.each(data.productos,function(key,entry){						 
					
						var product_entry = '<div class="container item-box rounded align-items-center justify-content-center">'+ 
						                    '<div class="row"><div class="col-md-6">'+
								    '<img src="https://'+entry.image+'" width="100px" height="100px"/>'+	
                                       			 	    '</div></div>'+
								    
								    '<div class="row"><div class="col-md-6">'+
								    '<h4>Marca: '+entry.brand+'<h4/>'+	
                                       			 	    '</div></div>'+

								    '<div class="row"><div class="col-md-6">'+
								    '<span>Descripción del producto: '+entry.description+'<span/>'+	
                                       			 	    '</div></div>'+

								    '<div class="row"><div class="col-md-6">'+
								    '<span>Precio: '+entry.price+'<span/>'+	
                                       			 	    '</div></div>'+

								    '<div class="row" style="background-color:#ffffff"><div class="col-md-6">'+
								    '</div></div>'+


							'</div>';
						
						list_html = list_html+product_entry;

					})
					
					list_html = list_html.replace('[object Object]','');
					$('#productList').html(list_html); 


				 }
			   });
		}		

      return false;
    }
  });
});


