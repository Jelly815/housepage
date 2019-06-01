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
.score_div {
    font-weight:normal;font-size: 20px;color:#555555;
}
.score_div label{
    float: left;
}
.score_div input[type="radio"] {
    display: block;
    padding: 2px 8px;
    line-height: 31px;
    width: 27px;
    float: left;
}
</style>
<div id="re_list">
    <h2 style="color: #041c4c;font-size: 22px;text-transform: uppercase;margin: 10px 0 15px 28px;">推薦列表 </h2>
    <ul class="second" style="">

    </ul>
</div>
<div id="featured" style="margin: 10px auto 0 auto;">
	<h2 style="font-size: 25px;">{search_title}</h2>
	<div>
		<h3 style="font-size: 25px;color:#ff7921;">
            <label onmouseout="user_mouse('price')">{search_price}</label>
			<label style="font-weight:normal;margin-left:20px;font-size: 16px;color:#555555;">瀏覽人數：{search_view}</label>
            <label style="font-weight:normal;margin-left:20px;font-size: 16px;color:#555555;">加入最愛 <a href="javascript:;" id="add_favorite"><img src="{favorite_src}" alt="加入最愛" width="20" height="20" style="cursor: pointer;" /></a></label>
		</h3>
        <!-- START BLOCK : show_score -->
        <div class="score_div" style="">
            <label style="margin-left:25px;color:red">為此物件評分：</label>
            <input type="radio" name="{type}" class="score_input" value="5">
            <label for="5" style="float: left">非常喜歡</label>
            <input type="radio" name="{type}" class="score_input" value="4">
            <label for="4">喜歡</label>
            <input type="radio" name="{type}" class="score_input" value="3">
            <label for="3">普通</label>
            <input type="radio" name="{type}" class="score_input" value="2">
            <label for="2">尚可</label>
            <input type="radio" name="{type}" class="score_input" value="1">
            <label for="1">不喜歡</label>
        </div><br><br>
        <!-- END BLOCK : show_score -->
		<a href="javascript:;"><img src="{search_img1}" alt="{search_title}" width="600" /></a>
		<ul>
			<li><a href="javascript:;"><img src="{search_img2}" alt="{search_title}" width="270" height="230" /></a></li>
			<li><a href="javascript:;"><img src="{search_img3}" alt="{search_title}" width="270" height="230" /></a></li>
		</ul>
		<div id="right">
			<ul>
                <li>
                    <p>
                        <label onmouseout="user_mouse('area')">區域：{search_area}</label>
                        <label onmouseout="user_mouse('road')">路段：{search_road}</label>
                        <label><a href="javascript:;" id="add_map" style="cursor: pointer;">[查看地圖]</a></label>
                    </p>
                </li>
				<li>
                    <p>
    					<label onmouseout="user_mouse('type')">類型：{search_type}</label>
                        <label onmouseout="user_mouse('room')">房數：{search_room}</label>
                        <label onmouseout="user_mouse('ping')">坪數：{search_ping}</label>
                    </p>
				</li>
                <li>
                    <p>
                        <label onmouseout="user_mouse('age')">屋齡：{search_age}</label>
                        <label onmouseout="user_mouse('floor')">樓層：{search_floor}</label>
                        <label onmouseout="user_mouse('parking')">車位：{search_parking}</label>
                    </p>
                </li>
                <li>
                    <p>
                        <label onmouseout="user_mouse('direction')">面向：{search_direction}</label>
                        <label onmouseout="user_mouse('unit')">單價：{search_unit}</label>
                        <label onmouseout="user_mouse('fee')">管理費：{search_fee}</label>
                    </p>
                </li>
                <li>
                    <p>
                        <label onmouseout="user_mouse('builder')">建商：{search_builder}</label>
                        <label onmouseout="user_mouse('community')">建案名稱：{search_community}</label>
                        <label onmouseout="user_mouse('status')">屋況：{search_status}</label>
                    </p>
                </li>
				<li>
					<p onmouseout="user_mouse('around')">生活機能：{search_arount}</p>
				</li>
				<li>
					<p>{search_desc}</p>
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
    // 加入最愛
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
    // 點擊地圖
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

    // 停留時間
    show_time = 0;
    showTime();

    function showTime(){
        show_time =  show_time+1;
        setTimeout("showTime()",1000);
    }

    var userAgent = navigator.userAgent; // userAgent
    var isOpera = userAgent.indexOf("Opera") > -1; // Opera
    var isIE = userAgent.indexOf("compatible") > -1 && userAgent.indexOf("MSIE") > -1 && !isOpera; // IE
    var isIE11 = userAgent.indexOf("rv:11.0") > -1; // IE11
    var isEdge = userAgent.indexOf("Edge") > -1 && !isIE; // IE的Edge

    if(!isIE && !isEdge && !isIE11) {
        var is_fireFox = navigator.userAgent.indexOf("Firefox")>-1;

        if(is_fireFox){
            window.onbeforeunload = function (){
                if(is_fireFox){
                }
            };
        }else{
            window.onunload = function(){
                $.ajax({
                    url: 'action.php?action=stay_time',
                    type: 'POST',
                    dataType: 'text',
                    async: false,
                    data: {
                        main_id: "{main_id}",
                        stay_time: show_time
                    }
                })
                .done(function(data) {
                })
                .fail(function() {
                    console.log("error");
                });
            };
        }
    }else if(isIE) {
        window.onbeforeunload = function() {
        }
        window.onunload = onclose;
        function onclose(){
        }
    }

    // 使用者滑鼠事件
    function user_mouse(action){
        $.ajax({
            url: 'action.php?action=user_mouse',
            type: 'POST',
            dataType: 'text',
            async: false,
            data: {
                main_id: "{main_id}",
                mouse: action
            }
        })
        .done(function(data) {
        })
        .fail(function() {
            console.log("error");
        });
    }

    // 為此物件評分
    $(".score_input").click(function(){ // 依您所在xx區熱門推薦
        var this_val    = $(this).val();
        var this_type   = $(this).attr('name');

        $.ajax({
            url: 'action.php?action=to_score',
            type: 'POST',
            dataType: 'text',
            async:false,
            data: {
                main_id: "{main_id}",
                type: this_type,
                score: this_val
            }
        })
        .done(function(like) {
        })
        .fail(function() {
            console.log("error");
        });
    });
</script>