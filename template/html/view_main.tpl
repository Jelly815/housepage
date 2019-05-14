<div id="featured">
	<h2>{search_title}</h2>
	<div>
		<h3 style="font-size: 25px;color:#ff7921;">{search_price}
			<label style="font-weight:normal;margin-left:20px;font-size: 16px;color:#555555;">單價：{search_unit}</label>
			<label style="font-weight:normal;margin-left:20px;font-size: 16px;color:#555555;">瀏覽人數：{search_view}</label>
            <label style="font-weight:normal;margin-left:20px;font-size: 16px;color:#555555;">加入最愛 <a href="javascript:;" id="add_favorite"><img src="img/favorite_gray.jpg" alt="加入最愛" width="20" height="20" style="cursor: pointer;" /></label>
		</h3>
		<a href="javascript:;"><img src="{search_img1}" alt="{search_title}" width="600" /></a>
		<ul>
			<li><a href="javascript:;"><img src="{search_img2}" alt="{search_title}" width="270" height="230" /></a></li>
			<li><a href="javascript:;"><img src="{search_img3}" alt="{search_title}" width="270" height="230" /></a></li>
		</ul>
		<div id="right">
			<ul>
				<li>
                    <p>
    					<label>類型：{search_type}</label>
                        <label>房數：{search_room}</label>
                        <label>坪數：{search_ping}</label>
                    </p>
				</li>
                <li>
                    <p>
                        <label>屋齡：{search_age}</label>
                        <label>樓層：{search_floor}</label>
                        <label>建商/建案名稱：{search_builder}</label>
                    </p>
                </li>
                <li>
                    <p>
                        <label>車位：{search_parking}</label>
                        <label>面向：{search_direction}</label>
                        <label>管理費：{search_fee}</label>
                    </p>
                </li>
				<li>
					<p>區域：{search_area} | {search_road} &nbsp;<label style="font-weight:normal;margin-left:20px;font-size: 16px;color:#555555;"><a href="javascript:;" id="add_map" style="cursor: pointer;">[查看地圖]</a></label></p>
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
<script>
    $("#add_favorite").click(function(){
        $.ajax({
            url: 'action.php?action=add_favorite',
            type: 'POST',
            dataType: 'text',
            async:false,
            data: {
                main_id: "{main_id}"
            }
        })
        .done(function(like) {
            if(like == '1'){
                $("#featured").find("#add_favorite").children('img').attr("src","img/favorite_red.jpg");
            }else{
                $("#featured").find("#add_favorite").children('img').attr("src","img/favorite_gray.jpg");
            }
        })
        .fail(function() {
            console.log("error");
        });
    });
    $("#add_map").click(function(){
        $.ajax({
            url: 'action.php?action=add_map',
            type: 'POST',
            dataType: 'text',
            async:false,
            data: {
                main_id: "{main_id}"
            }
        })
        .done(function(like) {
        })
        .fail(function() {
            console.log("error");
        });
    });
	/*
	var count_down_sec = parseInt("{count_down_sec}");
    var count_down_confirm_sec = parseInt("{count_down_confirm_sec}");
    var text_minute = parseInt(count_down_sec/60);
    var text_second = parseInt(count_down_sec%60);
    function showTime(){
        $(".time_tool").show();
        if(count_down_sec>0){
            count_down_sec -= 1;
        }
        text_minute = parseInt(count_down_sec/60);
        text_second = parseInt(count_down_sec%60);
        $(".text_minute").text(text_minute);
        $(".text_second").text(text_second);
        text_time = "";
        if(text_minute>0){
            text_time += text_minute+"分";
        }
        text_time += text_second+"秒";
        $("#count_down_text").text(text_time);
        if(count_down_sec==count_down_confirm_sec){
            alertify.set({ labels:{ ok : "延長"}});
            alertify.alert("您將於<span id='count_down_text' style='color:red'>"+text_time+"</span>後被登出系統，請按下[延長] 按鈕延長使用時間。", function (e) {
                if (e) {
                    count_down_sec = parseInt("{count_down_sec}");
                }
            });
        }
        if(count_down_sec<=0){
            log_out();
            $("#alertify, #alertify-cover").remove();
            alertify.set({ labels:{ ok : "確定"}});
            alertify.alert("超出作業時間，已被登出系統", function (e) {
                if (e) {
                    location.href='index.php?module=SC&action=login'
                }
            });
            setTimeout("log_out()",3000);
        }
        //每秒執行一次,showTime()
        if(count_down_sec>0){
            setTimeout("showTime()",1000);
        }
    }*/
</script>