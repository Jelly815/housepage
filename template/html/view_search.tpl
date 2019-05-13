<div id="offers">
	<h2>{PAGE_TITLE}</h2>
	<ul class="first">
		<!-- START BLOCK : view_search -->
		<li>
			<div>
				<h3><a href="index.php?op=view_main&main={search_uuid}" title="{search_title}" target="_blank">{search_title}</a></h3>
				<div id="left"><img src="{search_img}" alt="{search_title}" width="250" />
				</div>
				<div id="right">
					<h3><a href="index.php?op=view_main&main={search_uuid}" title="{search_title}" target="_blank">{search_price}</a></h3>
					<ul>
						<li>
							<p>{search_type} | {search_room} | {search_ping} | {search_age} | {search_floor}</p>
						</li>
						<li>
							<p>{search_builder} | {search_area} | {search_road}</p>
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