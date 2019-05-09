<div class="header">
    <ul id="navigation">
        <li>
            <a href="index.php" id="home" title="Home">Home</a>
        </li>
        <li>
            <a href="mailto:{ADMINMAIL}" id="email" title="Email">Email</a>
        </li>
    </ul>
    <div id="log_in_text">{USER_NAME}</div>
    <a href="index.php" id="logo" title="{HEADERTITLE}">
        <h1>{HEADERTITLE}</h1>
        <div>{HEADERTITLEDTAIL}</div>
    </a>
    <ul class="navigation">
        <li {SELECTED_DEFAULT}>
            <a href="index.php" title="{HOMEPAGE}">{HOMEPAGE}</a>
        </li>
        <li>
            <a id="navi_search" href="javascript:;" title="{ADSEARCH}">{ADSEARCH}</a>
        </li>
        <li {SELECTED_SIGNUP} id="login_li">
            {LOGIN_URL}
        </li>
    </ul>
    <div id="search_div">
        <input id="search_key" name="key" type="text" value="" placeholder="{ALERTXT11}">
        <a class="search_key_button sprited" id="key_button" href="javascript:;" title=""></a>
        <!--
        <form class="attireCodeToggleBlock" action="" style="display: none">
            <input
                    type="text"
                    multiple = "multiple"
                    class="multipleInputDynamicWithInitialValue"
                    name="search_key"
                    data-url="json/data.json"
                    placeholder="{ALERTXT10}"
                    id="area"
            />

            <button class="submitBtn" type="submit">Submit</button>
        </form>-->
    </div>
    <!-- START BLOCK : index_header -->
    <div id="featured">
        <div class="first">
            <ul>
                <li class="selected first">
                    <a href="featured.html">Search</a>
                    <div>



                    </div>
                </li>
                <div>
    <div>
        <div class="filter-row">
            <div class="clearfix">
                <div class="filter-name pull-left" style="padding-top: 6px;">位置</div>
                <div class="filter-body clearfix relative">
                    <div class="filter-location">
                        <div class="clearfix">
                            <div title="高雄市" class="filter-region filter-location-btn pull-left  z-active">
                                <div class="u-arrow"></div>
                                <div class="j-region filter-location-btn-txt">高雄市</div>
                            </div>
                            <div title="" class="filter-section filter-location-btn pull-left">
                                <div class="u-arrow"></div>
                                <div class="filter-location-btn-txt">選擇鄉鎮</div>
                            </div>
                    </div>
                    <div class="filter-location-list" style="display:none;">
                        <div class="region-list clearfix">
                            <div class="region-list-row clearfix">
                                <strong class="region-list-orientation">北部</strong>
                                <div class="region-list-item"><a href="javascript:;">新北市</a></div>
                                <div class="region-list-item"><a href="javascript:;">桃園市</a></div>
                                <div class="region-list-item"><a href="javascript:;">台北市</a></div>
                                <div class="region-list-item"><a href="javascript:;">新竹縣</a></div>
                                <div class="region-list-item"><a href="javascript:;">新竹市</a></div>
                                <div class="region-list-item"><a href="javascript:;">基隆市</a></div>
                                <div class="region-list-item"><a href="javascript:;">宜蘭縣</a></div>
                            </div>
                            <div class="region-list-row clearfix">
                                <strong class="region-list-orientation">中部</strong>
                                <div class="region-list-item"><a href="javascript:;">台中市</a></div>
                                <div class="region-list-item"><a href="javascript:;">苗栗縣</a></div>
                                <div class="region-list-item"><a href="javascript:;">彰化縣</a></div>
                                <div class="region-list-item"><a href="javascript:;">南投縣</a></div>
                                <div class="region-list-item"><a href="javascript:;">雲林縣</a></div>
                            </div>
                            <div class="region-list-row clearfix">
                                <strong class="region-list-orientation">南部</strong>
                                <div class="region-list-item z-select"><a href="javascript:;">高雄市</a></div>
                                <div class="region-list-item"><a href="javascript:;">台南市</a></div>
                                <div class="region-list-item"><a href="javascript:;">屏東縣</a></div>
                                <div class="region-list-item"><a href="javascript:;">嘉義市</a></div>
                                <div class="region-list-item"><a href="javascript:;">嘉義縣</a></div>
                            </div>
                            <div class="region-list-row clearfix">
                                <strong class="region-list-orientation">東部</strong>
                                <div class="region-list-item"><a href="javascript:;">花蓮縣</a></div>
                                <div class="region-list-item"><a href="javascript:;">台東縣</a></div>
                                <div class="region-list-item"><a href="javascript:;">金門縣</a></div>
                                <div class="region-list-item"><a href="javascript:;">澎湖縣</a></div>
                                <div class="region-list-item"><a href="javascript:;">連江縣</a></div>
                            </div>
                            <div class="region-list-row clearfix">
                                <strong class="region-list-orientation">其他</strong>
                                <div class="region-list-item"><a href="javascript:;">海外</a>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="filter-location-list" style="display:none;">
                        <div class="section-list clearfix">
                            <div class="section-list-unlimited pull-left">不限</div>
                            <div class="section-list-options clearfix">
                                <div class="section-list-item"><a href="javascript:;" j-tips-txt="您最多可選擇5個鄉鎮" class="section-list-item-link">三民區</a></div>
                                <div class="section-list-item"><a href="javascript:;" j-tips-txt="您最多可選擇5個鄉鎮" class="section-list-item-link">鳳山區</a></div>
                                <div class="section-list-item"><a href="javascript:;" j-tips-txt="您最多可選擇5個鄉鎮" class="section-list-item-link">左營區</a></div>
                                <div class="section-list-item"><a href="javascript:;" j-tips-txt="您最多可選擇5個鄉鎮" class="section-list-item-link">鼓山區</a></div>
                                <div class="section-list-item"><a href="javascript:;" j-tips-txt="您最多可選擇5個鄉鎮" class="section-list-item-link">苓雅區</a></div>
                                <div class="section-list-item"><a href="javascript:;" j-tips-txt="您最多可選擇5個鄉鎮" class="section-list-item-link">楠梓區</a></div>
                                <div class="section-list-item"><a href="javascript:;" j-tips-txt="您最多可選擇5個鄉鎮" class="section-list-item-link">前鎮區</a></div>
                                <div class="section-list-item"><a href="javascript:;" j-tips-txt="您最多可選擇5個鄉鎮" class="section-list-item-link">仁武區</a></div>
                                <div class="section-list-item"><a href="javascript:;" j-tips-txt="您最多可選擇5個鄉鎮" class="section-list-item-link">大寮區</a></div>
                                <div class="section-list-item"><a href="javascript:;" j-tips-txt="您最多可選擇5個鄉鎮" class="section-list-item-link">小港區</a></div>
                                <div class="section-list-item"><a href="javascript:;" j-tips-txt="您最多可選擇5個鄉鎮" class="section-list-item-link">鳥松區</a></div>
                                <div class="section-list-item"><a href="javascript:;" j-tips-txt="您最多可選擇5個鄉鎮" class="section-list-item-link">新興區</a></div>
                                <div class="section-list-item"><a href="javascript:;" j-tips-txt="您最多可選擇5個鄉鎮" class="section-list-item-link">前金區</a></div>
                                <div class="section-list-item"><a href="javascript:;" j-tips-txt="您最多可選擇5個鄉鎮" class="section-list-item-link">岡山區</a></div>
                                <div class="section-list-item"><a href="javascript:;" j-tips-txt="您最多可選擇5個鄉鎮" class="section-list-item-link">大社區</a></div>
                                <div class="section-list-item"><a href="javascript:;" j-tips-txt="您最多可選擇5個鄉鎮" class="section-list-item-link">橋頭區</a></div>
                                <div class="section-list-item"><a href="javascript:;" j-tips-txt="您最多可選擇5個鄉鎮" class="section-list-item-link">大樹區</a></div>
                                <div class="section-list-item"><a href="javascript:;" j-tips-txt="您最多可選擇5個鄉鎮" class="section-list-item-link">鹽埕區</a></div>
                                <div class="section-list-item"><a href="javascript:;" j-tips-txt="您最多可選擇5個鄉鎮" class="section-list-item-link">美濃區</a></div>
                                <div class="section-list-item"><a href="javascript:;" j-tips-txt="您最多可選擇5個鄉鎮" class="section-list-item-link">林園區</a></div>
                                <div class="section-list-item"><a href="javascript:;" j-tips-txt="您最多可選擇5個鄉鎮" class="section-list-item-link">燕巢區</a></div>
                                <div class="section-list-item"><a href="javascript:;" j-tips-txt="您最多可選擇5個鄉鎮" class="section-list-item-link">湖內區</a></div>
                                <div class="section-list-item"><a href="javascript:;" j-tips-txt="您最多可選擇5個鄉鎮" class="section-list-item-link">旗山區</a></div>
                                <div class="section-list-item"><a href="javascript:;" j-tips-txt="您最多可選擇5個鄉鎮" class="section-list-item-link">路竹區</a></div>
                                <div class="section-list-item"><a href="javascript:;" j-tips-txt="您最多可選擇5個鄉鎮" class="section-list-item-link">梓官區</a></div>
                                <div class="section-list-item"><a href="javascript:;" j-tips-txt="您最多可選擇5個鄉鎮" class="section-list-item-link">茄萣區</a></div>
                                <div class="section-list-item"><a href="javascript:;" j-tips-txt="您最多可選擇5個鄉鎮" class="section-list-item-link">六龜區</a></div>
                                <div class="section-list-item"><a href="javascript:;" j-tips-txt="您最多可選擇5個鄉鎮" class="section-list-item-link">杉林區</a></div>
                                <div class="section-list-item"><a href="javascript:;" j-tips-txt="您最多可選擇5個鄉鎮" class="section-list-item-link">阿蓮區</a></div>
                                <div class="section-list-item"><a href="javascript:;" j-tips-txt="您最多可選擇5個鄉鎮" class="section-list-item-link">甲仙區</a></div>
                                <div class="section-list-item"><a href="javascript:;" j-tips-txt="您最多可選擇5個鄉鎮" class="section-list-item-link">旗津區</a></div>
                                <div class="section-list-item"><a href="javascript:;" j-tips-txt="您最多可選擇5個鄉鎮" class="section-list-item-link">彌陀區</a></div>
                                <div class="section-list-item"><a href="javascript:;" j-tips-txt="您最多可選擇5個鄉鎮" class="section-list-item-link">田寮區</a></div>
                                <div class="section-list-item"><a href="javascript:;" j-tips-txt="您最多可選擇5個鄉鎮" class="section-list-item-link">內門區</a></div>
                                <div class="section-list-item"><a href="javascript:;" j-tips-txt="您最多可選擇5個鄉鎮" class="section-list-item-link">永安區</a></div>
                                <div class="section-list-item"><a href="javascript:;" j-tips-txt="您最多可選擇5個鄉鎮" class="section-list-item-link">桃源區</a></div>
                                <div class="section-list-item"><a href="javascript:;" j-tips-txt="您最多可選擇5個鄉鎮" class="section-list-item-link">那瑪夏區</a></div>
                                <div class="section-list-item"><a href="javascript:;" j-tips-txt="您最多可選擇5個鄉鎮" class="section-list-item-link">茂林區</a></div>
                            </div>
                        </div>
                    </div>
                    <div class="filter-location-list" ><div class="school-list clearfix"><div class="school-list-item-wrap"><a href="javascript:;" class="school-list-item">高雄師範大學</a></div><div class="school-list-item-wrap"><a href="javascript:;" class="school-list-item">中山大學</a></div><div class="school-list-item-wrap"><a href="javascript:;" class="school-list-item">高雄應用科技大學</a></div><div class="school-list-item-wrap"><a href="javascript:;" class="school-list-item">高雄醫學大學</a></div><div class="school-list-item-wrap"><a href="javascript:;" class="school-list-item">高雄第一科技大學</a></div><div class="school-list-item-wrap"><a href="javascript:;" class="school-list-item">國立高雄大學</a></div><div class="school-list-item-wrap"><a href="javascript:;" class="school-list-item">高雄餐旅大學</a></div><div class="school-list-item-wrap"><a href="javascript:;" class="school-list-item">樹德科技大學</a></div><div class="school-list-item-wrap"><a href="javascript:;" class="school-list-item">輔英科技大學</a></div><div class="school-list-item-wrap"><a href="javascript:;" class="school-list-item">正修科技大學</a></div><div class="school-list-item-wrap"><a href="javascript:;" class="school-list-item">義守大學</a></div><div class="school-list-item-wrap"><a href="javascript:;" class="school-list-item">國立高雄海洋科技大學</a></div><div class="school-list-item-wrap"><a href="javascript:;" class="school-list-item">文藻外語學院</a></div><div class="school-list-item-wrap"><a href="javascript:;" class="school-list-item">高苑科技大學</a></div><div class="school-list-item-wrap"><a href="javascript:;" class="school-list-item">東方設計學院</a></div></div></div> <div class="filter-location-list" ><div class="business-list clearfix"><div class="business-list-item-wrap"><a href="javascript:;" class="school-list-item">三鳳中街形象商圈</a></div><div class="business-list-item-wrap"><a href="javascript:;" class="school-list-item">新堀江商圈</a></div><div class="business-list-item-wrap"><a href="javascript:;" class="school-list-item">大連街形象商圈</a></div><div class="business-list-item-wrap"><a href="javascript:;" class="school-list-item">中心魅力商圈</a></div><div class="business-list-item-wrap"><a href="javascript:;" class="school-list-item">長明商圈</a></div><div class="business-list-item-wrap"><a href="javascript:;" class="school-list-item">興中花卉街商圈</a></div><div class="business-list-item-wrap"><a href="javascript:;" class="school-list-item">鹽埕堀江商場商圈</a></div><div class="business-list-item-wrap"><a href="javascript:;" class="school-list-item">後驛商圈</a></div><div class="business-list-item-wrap"><a href="javascript:;" class="school-list-item">南華觀光商場</a></div><div class="business-list-item-wrap"><a href="javascript:;" class="school-list-item">六合觀光夜市商圈</a></div><div class="business-list-item-wrap"><a href="javascript:;" class="school-list-item">興中觀光夜巿商圈</a></div><div class="business-list-item-wrap"><a href="javascript:;" class="school-list-item">光華觀光夜巿商圈</a></div><div class="business-list-item-wrap"><a href="javascript:;" class="school-list-item">忠孝觀光夜巿商圈</a></div><div class="business-list-item-wrap"><a href="javascript:;" class="school-list-item">明誠商圈</a></div><div class="business-list-item-wrap"><a href="javascript:;" class="school-list-item">瑞峰商圈</a></div><div class="business-list-item-wrap"><a href="javascript:;" class="school-list-item">美術館商圈</a></div><div class="business-list-item-wrap"><a href="javascript:;" class="school-list-item">崇德商圈</a></div><div class="business-list-item-wrap"><a href="javascript:;" class="school-list-item">愛河商圈</a></div><div class="business-list-item-wrap"><a href="javascript:;" class="school-list-item">漢神大力商圈</a></div><div class="business-list-item-wrap"><a href="javascript:;" class="school-list-item">三多商圈</a></div><div class="business-list-item-wrap"><a href="javascript:;" class="school-list-item">旗山鎮中山路商圈</a></div><div class="business-list-item-wrap"><a href="javascript:;" class="school-list-item">甲仙鄉形象商圈</a></div><div class="business-list-item-wrap"><a href="javascript:;" class="school-list-item">鳳山市三民路商圈</a></div><div class="business-list-item-wrap"><a href="javascript:;" class="school-list-item">高雄科學園區</a></div><div class="business-list-item-wrap"><a href="javascript:;" class="school-list-item">大發工業區</a></div><div class="business-list-item-wrap"><a href="javascript:;" class="school-list-item">鳳山工業區</a></div><div class="business-list-item-wrap"><a href="javascript:;" class="school-list-item">鳳山工業區</a></div><div class="business-list-item-wrap"><a href="javascript:;" class="school-list-item">大社工業區</a></div><div class="business-list-item-wrap"><a href="javascript:;" class="school-list-item">仁武工業區</a></div><div class="business-list-item-wrap"><a href="javascript:;" class="school-list-item">永安工業區</a></div><div class="business-list-item-wrap"><a href="javascript:;" class="school-list-item">林園工業區</a></div><div class="business-list-item-wrap"><a href="javascript:;" class="school-list-item">高雄市臨海工業區</a></div></div></div></div></div></div></div></div> <div class="mb20 filter-kind-wrap"><div class="filter-row clearfix"><div class="filter-name pull-left">類型</div> <div class="filter-body clearfix"><div data-gtm-stat="中古屋列表頁_類型_不限" class="filter-items filter-kind-items-0 z-small"><a href="javascript:;">不限</a></div><div data-gtm-stat="中古屋列表頁_類型_住宅" class="filter-items filter-kind-items-9"><a href="javascript:;">住宅</a></div><div data-gtm-stat="中古屋列表頁_類型_套房" class="filter-items filter-kind-items-10"><a href="javascript:;">套房</a></div><div data-gtm-stat="中古屋列表頁_類型_車位" class="filter-items filter-kind-items-8"><a href="javascript:;">車位</a></div><div data-gtm-stat="中古屋列表頁_類型_法拍屋" class="filter-items filter-kind-items-22"><a href="javascript:;">法拍屋</a></div><div data-gtm-stat="中古屋列表頁_類型_其他" class="filter-items filter-kind-items-24"><a href="javascript:;">其他</a></div></div></div></div> <div class="filter-saleprice-wrap"><div class="filter-row clearfix"><div class="filter-name pull-left">售金</div> <div class="filter-body clearfix relative"><!----> <div class="filter-saleprice-options clearfix oh"><div class="filter-items z-small"><a href="javascript:;" data-gtm-stat="中古屋列表頁_售金_不限" class="">
不限
</a></div><div class="filter-items z-multiple"><a href="javascript:;" data-gtm-stat="中古屋列表頁_售金_1000萬以下" class="">
1000萬以下
</a></div><div class="filter-items z-multiple"><a href="javascript:;" data-gtm-stat="中古屋列表頁_售金_1000-1500萬" class="">
1000-1500萬
</a></div><div class="filter-items z-multiple"><a href="javascript:;" data-gtm-stat="中古屋列表頁_售金_1500-2000萬" class="">
1500-2000萬
</a></div><div class="filter-items z-multiple"><a href="javascript:;" data-gtm-stat="中古屋列表頁_售金_2000-2500萬" class="">
2000-2500萬
</a></div><div class="filter-items z-multiple"><a href="javascript:;" data-gtm-stat="中古屋列表頁_售金_2500-3000萬" class="">
2500-3000萬
</a></div><div class="filter-items z-multiple"><a href="javascript:;" data-gtm-stat="中古屋列表頁_售金_3000-4000萬" class="">
3000-4000萬
</a></div><div class="filter-items z-multiple"><a href="javascript:;" data-gtm-stat="中古屋列表頁_售金_4000萬以上" class="">
4000萬以上
</a></div> <div class="filter-custom pull-left flex-row flex-ai-center"><input type="text" maxlength="6" class="filter-custom-min filter-custom-input"> <span class="filter-custom-line">-</span> <input type="text" maxlength="6" class="filter-custom-max filter-custom-input"> <span class="filter-custom-unit">萬</span> <button type="button" class="filter-custom-submit">確定</button></div> <a href="javascript:;" data-gtm-stat="中古屋列表頁_入口_購房能力評估" class="filter-saleprice-assessbtn"></a></div></div></div> <!----></div> <div class="mb20 filter-shape-wrap"><div class="filter-row clearfix"><div class="filter-name pull-left">型態</div> <div class="filter-body clearfix"><div class="filter-items z-small"><a href="javascript:;" data-gtm-stat="中古屋列表頁_型態_不限" class="">不限</a></div><div class="filter-items z-multiple"><a href="javascript:;" data-gtm-stat="中古屋列表頁_型態_公寓" class="">公寓</a></div><div class="filter-items z-multiple"><a href="javascript:;" data-gtm-stat="中古屋列表頁_型態_電梯大樓" class="">電梯大樓</a></div><div class="filter-items z-multiple"><a href="javascript:;" data-gtm-stat="中古屋列表頁_型態_透天厝" class="">透天厝</a></div><div class="filter-items z-multiple"><a href="javascript:;" data-gtm-stat="中古屋列表頁_型態_別墅" class="">別墅</a></div></div></div></div> <div class="mb20 filter-pattern-wrap"><div class="filter-row clearfix"><div class="filter-name pull-left">格局</div> <div class="filter-body clearfix"><div class="filter-items z-small"><a href="javascript:;" data-gtm-stat="中古屋列表頁_格局_不限" class="">不限</a></div><div class="filter-items z-multiple"><a href="javascript:;" data-gtm-stat="中古屋列表頁_格局_1房" class="">1房</a></div><div class="filter-items z-multiple"><a href="javascript:;" data-gtm-stat="中古屋列表頁_格局_2房" class="">2房</a></div><div class="filter-items z-multiple"><a href="javascript:;" data-gtm-stat="中古屋列表頁_格局_3房" class="">3房</a></div><div class="filter-items z-multiple"><a href="javascript:;" data-gtm-stat="中古屋列表頁_格局_4房" class="">4房</a></div><div class="filter-items z-multiple"><a href="javascript:;" data-gtm-stat="中古屋列表頁_格局_5房及以上" class="">5房及以上</a></div></div></div></div> <div class="filter-area-wrap"><div class="filter-row clearfix"><div class="filter-name pull-left"><div class="area-switch"><div title="權狀坪數" class="area-switch-cur">
權狀
<i class="area-switch-icon fa fa-angle-down"></i></div> <div title="主建坪數" data-gtm-stat="中古屋列表頁_坪數_主建" class="area-switch-float">主建</div></div></div> <div class="filter-body clearfix"><!----> <div class="filter-area-options clearfix oh"><div class="filter-items z-small"><a href="javascript:;" data-gtm-stat="中古屋列表頁_坪數_不限" class="">不限</a></div><div class="filter-items z-multiple"><a href="javascript:;" data-gtm-stat="中古屋列表頁_坪數_20坪以下" class="">20坪以下</a></div><div class="filter-items z-multiple"><a href="javascript:;" data-gtm-stat="中古屋列表頁_坪數_20-30坪" class="">20-30坪</a></div><div class="filter-items z-multiple"><a href="javascript:;" data-gtm-stat="中古屋列表頁_坪數_30-40坪" class="">30-40坪</a></div><div class="filter-items z-multiple"><a href="javascript:;" data-gtm-stat="中古屋列表頁_坪數_40-50坪" class="">40-50坪</a></div><div class="filter-items z-multiple"><a href="javascript:;" data-gtm-stat="中古屋列表頁_坪數_50-60坪" class="">50-60坪</a></div><div class="filter-items z-multiple"><a href="javascript:;" data-gtm-stat="中古屋列表頁_坪數_60坪以上" class="">60坪以上</a></div> <div class="filter-custom pull-left flex-row flex-ai-center"><input type="text" maxlength="6" class="filter-custom-min filter-custom-input"> <span class="filter-custom-line">-</span> <input type="text" maxlength="6" class="filter-custom-max filter-custom-input"> <span class="filter-custom-unit">坪</span> <button type="button" class="filter-custom-submit" >確定</button></div></div></div></div></div> <div class="filter-more-wrap mb20 z-kind-null"><div class="filter-row clearfix"><div class="filter-name pull-left" style="padding-top: 7px;">更多</div> <div class="filter-body clearfix"><div class="filter-fcicount filter-more pull-left" style="width: 80px;"><div class="u-arrow"></div>
</div>
<div class="filter-houseage filter-more pull-left" style="width: 90px;"><div class="u-arrow"></div> <div title="" class="filter-more-txt">
屋齡
</div> <div class="filter-more-list" ><div data-gtm-stat="中古屋列表頁_更多_屋齡" class="filter-more-item">
5年以下
</div><div data-gtm-stat="中古屋列表頁_更多_屋齡" class="filter-more-item">
5-10年
</div><div data-gtm-stat="中古屋列表頁_更多_屋齡" class="filter-more-item">
10-20年
</div><div data-gtm-stat="中古屋列表頁_更多_屋齡" class="filter-more-item">
20-30年
</div><div data-gtm-stat="中古屋列表頁_更多_屋齡" class="filter-more-item">
30-40年
</div><div data-gtm-stat="中古屋列表頁_更多_屋齡" class="filter-more-item">
40年以上
</div> <div class="mb15 clearfix"><div class="filter-custom pull-left flex-row flex-ai-center"><input type="text" maxlength="3" class="filter-custom-min filter-custom-input"> <span class="filter-custom-line">-</span> <input type="text" maxlength="3" class="filter-custom-max filter-custom-input"> <span class="filter-custom-unit">年</span> <button type="button" class="filter-custom-submit">確定</button></div></div></div></div> <div class="filter-price filter-more pull-left" style="width: 80px;"><div class="u-arrow"></div> <div title="" class="filter-more-txt">
單價
</div> <div class="filter-more-list" ><div data-gtm-stat="中古屋列表頁_更多_單價" class="filter-more-item">
20萬以下
</div><div data-gtm-stat="中古屋列表頁_更多_單價" class="filter-more-item">
20-30萬
</div><div data-gtm-stat="中古屋列表頁_更多_單價" class="filter-more-item">
30-50萬
</div><div data-gtm-stat="中古屋列表頁_更多_單價" class="filter-more-item">
50-70萬
</div><div data-gtm-stat="中古屋列表頁_更多_單價" class="filter-more-item">
70萬以上
</div></div></div> <div class="filter-direction filter-more pull-left" style="width: 90px;"><div class="u-arrow"></div> <div title="" class="filter-more-txt">
朝向
</div> <div class="filter-more-list" ><div data-gtm-stat="中古屋列表頁_更多_朝向" class="filter-more-item">
坐東朝西
</div><div data-gtm-stat="中古屋列表頁_更多_朝向" class="filter-more-item">
坐西朝東
</div><div data-gtm-stat="中古屋列表頁_更多_朝向" class="filter-more-item">
坐南朝北
</div><div data-gtm-stat="中古屋列表頁_更多_朝向" class="filter-more-item">
坐北朝南
</div><div data-gtm-stat="中古屋列表頁_更多_朝向" class="filter-more-item">
坐東南朝西北
</div><div data-gtm-stat="中古屋列表頁_更多_朝向" class="filter-more-item">
坐西南朝東北
</div><div data-gtm-stat="中古屋列表頁_更多_朝向" class="filter-more-item">
坐西北朝東南
</div><div data-gtm-stat="中古屋列表頁_更多_朝向" class="filter-more-item">
坐東北朝西南
</div></div></div> <div class="filter-floor filter-more pull-left" style="width: 80px;"><div class="u-arrow"></div> <div title="" class="filter-more-txt">
樓層
</div>
<div class="filter-more-list" >



<div class="mb15 clearfix"><div class="filter-custom pull-left flex-row flex-ai-center"><input type="text" maxlength="3" class="filter-custom-min filter-custom-input"> <span class="filter-custom-line">-</span> <input type="text" maxlength="3" class="filter-custom-max filter-custom-input"> <span class="filter-custom-unit">層</span> <button type="button" class="filter-custom-submit">確定</button></div></div></div></div> <div class="filter-fitment filter-more pull-left" style="width: 100px;"><div class="u-arrow"></div> <div title="" class="filter-more-txt">
裝潢程度
</div> <div class="filter-more-list" ><div data-gtm-stat="中古屋列表頁_更多_裝潢程度" class="filter-more-item">
尚未裝潢
</div><div data-gtm-stat="中古屋列表頁_更多_裝潢程度" class="filter-more-item">
簡易裝潢
</div><div data-gtm-stat="中古屋列表頁_更多_裝潢程度" class="filter-more-item">
中檔裝潢
</div><div data-gtm-stat="中古屋列表頁_更多_裝潢程度" class="filter-more-item">
高檔裝潢
</div></div></div> <div class="filter-life filter-more pull-left" style="width: 100px;"><div class="u-arrow"></div> <div title="" class="filter-more-txt">
生活機能
</div>
<div class="filter-more-list" >
<div data-gtm-stat="中古屋列表頁_更多_生活機能" class="filter-more-item">
便利店
</div>
<div data-gtm-stat="中古屋列表頁_更多_生活機能" class="filter-more-item">
傳統市場
</div>
<div data-gtm-stat="中古屋列表頁_更多_生活機能" class="filter-more-item">
近醫療機構
</div>
<div data-gtm-stat="中古屋列表頁_更多_生活機能" class="filter-more-item">
近學校
</div><div data-gtm-stat="中古屋列表頁_更多_生活機能" class="filter-more-item">
近公園
</div><div data-gtm-stat="中古屋列表頁_更多_生活機能" class="filter-more-item">
近夜市
</div><div data-gtm-stat="中古屋列表頁_更多_生活機能" class="filter-more-item">
百貨公司
</div></div></div>

</div></div></div></div>
            </ul>

        </div>

    </div>
    <!-- END BLOCK : index_header -->
</div>
<script>
$(function () {
    //var $select = $('select');

    // Run, fire and forget
    //$select.fastselect()

    // Run via plugin facade and get instance
    //var fastSelectInstance = $select.fastselect(options).data('fastselect');

    // run directly
    //var fastSelectInstance = new $.Fastselect($select.get(0), options);
    // 關鍵字搜尋
    $('#search_key').tagsInput({placeholder:'{ALERTXT11}'});
    // 縣市
    //$('.singleSelect').fastselect();
    //$('.multipleInputDynamicWithInitialValue').fastselect();
    $('#search_city').change(function(event) {
        if($(this).select().val() != ''){
            $('.attireCodeToggleBlock').show();
            //$('.fstMultipleMode .fstResultItem').remove();
//console.log('start');
            $.ajax({
                url: 'action.php',
                type: 'GET',
                dataType: 'json',
                async: false,
                data: {
                    action: 'getarea',
                    city_id: $(this).select().val()},
            })
            .done(function(re_data) {
                var new_option = '';

                $.each(re_data, function(i, val) {
                     new_option += '<span id="'+re_data[i].value+'" class="fstResultItem">'+re_data[i].text+'</span>';
                });

                $('.attireCodeToggleBlock .fstResults').remove('span').html(new_option);

                $('.multipleInputDynamicWithInitialValue').fastselect();
                $('.multipleInputDynamicWithInitialValue').data('data-url', 'json/data.json');
            })
            .fail(function() {
                console.log("error");
            });
            /*
            $.get('action.php',
                {
                    action: 'getarea',
                    city_id: $(this).select().val()
                },
                function(re_data){
                    var restaurant = $('.multipleInputDynamicWithInitialValue');

                    var owner = restaurant.data("data-url");
                    restaurant.data("data-url", JSON.parse("json/data.json"));
                    //console.log(re_data);
                    //$('.multipleInputDynamicWithInitialValue').data(re_data);

                    //var a = $('.multipleInputDynamicWithInitialValue').data('data-url'); //getter

                    //$('.multipleInputDynamicWithInitialValue').data('data-url',"json/data.json"); //setter
                }
            );*/
        }else{
            $('.attireCodeToggleBlock').hide();
        }
    });
    $('#navi_search').click(function(event) {
        $('.navigation li').removeClass('selected first');
        $(this).parent('li').addClass('selected first');
        $('#search_div').show().css('display',"inline-block" );
    });
});
</script>