<div id="featured">
	<h2>{search_title}</h2>
	<div>
		<h3 style="font-size: 25px;color:#ff7921;">{search_price}
			<label style="font-weight:normal;margin-left:20px;font-size: 16px;color:#555555;">單價：{search_unit}</label>
			<label style="font-weight:normal;margin-left:20px;font-size: 16px;color:#555555;">瀏覽人數：{search_view}</label>
		</h3>
		<a href="javascript:;"><img src="{search_img1}" alt="{search_title}" width="600" /></a>
		<ul>
			<li><a href="javascript:;"><img src="{search_img2}" alt="{search_title}" width="270" height="230" /></a></li>
			<li><a href="javascript:;"><img src="{search_img3}" alt="{search_title}" width="270" height="230" /></a></li>
		</ul>
		<div id="right">
			<ul>
				<li>
					<p>房數：{search_room}<br>坪數：{search_ping}<br>屋齡：{search_age}<br>樓層：{search_floor}</p>
				</li>
				<li>
					<p>區域：{search_builder} | {search_area} | {search_road} | {search_direction}</p>
				</li>
				<li>
					<p>生活機能：{search_arount}</p>
				</li>
				<li>
					{search_desc}
				</li>
				<li>
					<!-- START BLOCK : view_img -->
					<a href="javascript:;"><img src="{search_img}" alt="{search_title}" width="270" height="230" /></a>
					<!-- END BLOCK : view_img -->
				</li>
			</ul>
		</div>

	</div>
</div>