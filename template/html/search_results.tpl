<!-- START BLOCK : search_row -->
<li>
    <a href="index.php?op=view_main&main={search_uuid}{search_page}" target="_blank"><img src="{search_img}" alt="" width="140" {search_click} /></a>
    <span><a href="index.php?op=view_main&main={search_uuid}{search_page}" target="_blank" {search_click}>{search_title}</a></span>
    <p>{search_area}|{search_type}|{search_room}|{search_ping}</p>
    <a href="javascript:;" class="details">{search_price}</a>
    <a href="javascript:;" class="book">{search_view}</a>
</li>
<!-- END BLOCK : search_row -->
<!-- START BLOCK : search_nodata -->
<li>{nodata}</li>
<!-- END BLOCK : search_nodata -->
<div id="search_val" style="display:none">{url}</div>
<script type="text/javascript">
	function click_recommend(uid,mid,type){
		$.ajax({
            url: 'action.php?action=click_recommend',
            type: 'POST',
            dataType: 'text',
            async: false,
            data: {
                user_id: uid,
                main_id: mid,
                re_type: type
            }
        })
        .done(function(data) {
        })
        .fail(function() {
            console.log("error");
        });
	}
</script>