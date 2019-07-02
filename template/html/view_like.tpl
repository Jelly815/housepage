<style>
#re_list{
    background-color: #fff;
    overflow: hidden;
    border-radius: 5px;
    width: 970px;
    height:auto;
    display: block;
    margin:-50px auto 0px auto;
}
#re_list .second{
    list-style: none;
    background-color: #FFFFFF;
    padding: 15px;
    margin: 0;
    overflow: hidden;
    border-radius: 5px;
    min-height: 150px;
}
#re_list ul li{
    width: 188px;
    height: auto;
    overflow: hidden;
    margin: 0 0 20px 0;
    float: left;
}
#re_list ul li a {
    float: left;
    display: block;
    position: static;
    background: none;
    padding: 0 0 0 11px;
    font-family: arial;
    font-size: 14px;
    color: #4d4d4d;
    text-decoration: none;
}
#re_list ul li span {
    width: 158px;
    display: block;
    clear: none;
    float: left;
    text-align: justify;
    margin: 0 0 0 11px;
}
#re_list ul li span a {
    text-decoration: none;
    font-size: 14px;
    font-family: arial;
    color: #105272;
    font-weight: bold;
    background: none;
    position: static;
    padding: 0;
    float: left;
    display: block;
}
#re_list ul li p {
    clear: none;
    float: left;
    text-align: justify;
    width: 158px;
    color: #393D42;
    font-family: arial;
    font-size: 8.5pt;
    margin: 0 0 0 11px;
}
#re_list ul li a.details {
    font-size: 12px;
    color: #674900;
    text-decoration: none;
    font-family: arial;
    background: url(template/images/icons.gif) no-repeat 0 -155px;
    width: 74px;
    height: 18px;
    text-align: center;
    line-height: 18px;
    margin: 0 5px 0 11px;
    position: static;
    padding: 0;
}
#re_list ul li a.book {
    color: #d4ffff;
    text-decoration: none;
    font-family: arial;
    background: url(template/images/interface.gif) no-repeat;
    width: 70px;
    height: 18px;
    text-align: center;
    line-height: 18px;
    font-size: 12px;
    position: static;
    padding: 0;
}
</style>
<div id="re_list">
    <h2 style="color: #041c4c;font-size: 22px;text-transform: uppercase;margin: 10px 0 15px 28px;">預測您喜歡的 </h2>
    <ul class="second" style="">

    </ul>
</div>
<div id="offers" style="margin: 10px auto 0 auto;">
	<h2>{HEADERTITLE}</h2>
	<ul class="first">
		<!-- START BLOCK : view_search -->
		<li>
			<div>
				<h3><a href="index.php?op=view_main&main={search_uuid}" title="{search_title}" target="_blank">{search_title}</a></h3>
				<div id="left">
					<a href="index.php?op=view_main&main={search_uuid}" title="{search_title}" target="_blank">
						<img src="{search_img}" alt="{search_title}" width="250" />
					</a>
				</div>
				<div id="right">
					<h3><a href="index.php?op=view_main&main={search_uuid}" title="{search_title}" target="_blank">{search_price}</a></h3>
					<ul>
						<li>
							<p>{search_type} | {search_room} | {search_ping} | {search_age} | {search_floor}</p>
						</li>
						<li>
							<p>{search_area} | {search_road} | {search_builder}</p>
						</li>
						<li>
							<p>{search_arount}</p>
						</li>
						<li>
							<p>{search_view}</p>
						</li>
					</ul>
				</div>
			</div>
		</li>
		<!-- END BLOCK : view_search -->
	</ul>
</div>

<script type="text/javascript">
	// personalized recommendation
    $.ajax({
        url: 'recommend.php',
        type: 'POST',
        dataType: 'text',
        async: false,
        data: {
            area:   '',
            price:  '',
            type:   '',
            room:   '',
            ping:   ''
        },
    })
    .done(function(data) {
        $(".second").empty().html(data);
    })
    .fail(function() {
        console.log("error");
    });
</script>