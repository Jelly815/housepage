<script src="js/masonry.pkgd.min.js"></script>
<script src="js/imagesloaded.pkgd.min.js"></script>
<script>
	$(document).ready(function(){
		var $grid = $('.grid').imagesLoaded( function() {
			$grid.masonry({
				itemSelector: '.grid-item',
				percentPosition:true
			});
		});
	});
</script>
<div class="grid">
<!-- START BLOCK : pic_row -->
	<div class="grid-item">
  		<div class="grid-content">
    		<div class="grid-title">
            	【{department}_{uname}】
                <a href="{EDITPICTOPATH}{para}{id}" title="{EDIT}">{EDIT}</a>&nbsp;
                <a href="javascript:;" title="{DEL}" onclick="javascript:if(confirm('{DELALERT}'))window.location.href ='{LOGINTOPATH}{para}{id}';return false;">{DEL}</a><br>
                {title}
            </div>
    		<img src="{UPLOADPICPATH}{pic}">
        	<div class="grid-txt">{txt}</div>
  		</div>
  	</div>
<!-- END BLOCK : pic_row -->
</div>
