<script src="photograph/js/masonry.pkgd.min.js"></script>
<script src="photograph/js/imagesloaded.pkgd.min.js"></script>

<script src="photograph/js/wayfinder.js"></script>
<script>
$( function() {
	$( "#search_btn" ).click(function() {
        $("#search_div").toggle();
    });

	var $grid = $('.grid').imagesLoaded( function() {
		$grid.masonry({
	  		itemSelector: '.grid-item',
			percentPosition: true,
			columnWidth: '.grid-sizer'
		});
	});
	
	flag = true;
	$(window).scroll(function() {
		if($(window).scrollTop() + $(window).height() == $(document).height()){
			first = $('#first').val();
			limit = $('#limit').val();
			no_data = true;
			if(flag && no_data){
				flag = false;
				$('#loader').show();
				$.ajax({
					url : 'ajax.php',
					method: 'post',
					data: {
					   start : first,
					   limit : limit
					},
					dataType:'html',
					success: function( data ) {
						flag = true;
						$('#loader').hide();
						if(data !=''){
							first = parseInt($('#first').val());
							limit = parseInt($('#limit').val());
				
							$('#first').val( first+limit );
							
							//$('#grid').append( data );
							//jQuery("#content").append(data).masonry( 'appended', data, true );
							var $items = $(data);
							$grid.append( $items ).masonry( 'appended', $items );
						}else{
							no_data = false;
						}
					},
					error: function( data ){
						flag = true;
						$('#loader').hide();
						no_data = false;
						alert('Something went wrong, Please contact admin');
					}
				});
			}
		}
	});	
});


</script>
<div class="grid" id="grid">
<div class="grid-sizer"></div>
<!-- START BLOCK : index_row -->
	<div class="grid-item">
  		<div class="grid-content box">
    		<div class="grid-title">【{department}_{uname}】<br>{title}</div>
    		<img src="{UPLOADPICPATH}{pic}">
        	<div class="grid-txt details">{txt}</div>
        	<a href="#" class="button">More Details</a>
  		</div>
  	</div>
<!-- END BLOCK : index_row -->
</div>

<div id="loader">
	<div class="sk-spinner sk-spinner-pulse"></div>
</div>
<input type="hidden" id="first" value="{FIRST}" />
<input type="hidden" id="limit" value="{LIMIT}" >