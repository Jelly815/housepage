<?php
// DATABASE
define('SERVERNAME','127.0.0.1');
define('USERNAME','root');
define('USERPWD','root');
define('DATANAME','myweb');
define('DATATYPE','mysqli');
define('ADMINMAIL',"jellyandjar@yahoo.com.tw");
define('default_area',282);

// PATH
define('THEMES','./template/html/');
define('CSSPATH','./template/css/');
define('JSPATH','./js/');
#define('PYTHONPATH','D:/xampp/htdocs/housepage/python/main');
#define('PYTHONPATH','python F:/xampp/htdocs/housepage/python/main');
define('PYTHONPATH','python3 /var/www/html/homepage/python/main');
define('_TMAIN',THEMES.'main.tpl');
define('_THEADER',THEMES.'header.tpl');
define('_TFOOTER',THEMES.'footer.tpl');
define('_TSIGN',THEMES.'signup.tpl');
define('_TLOGIN',THEMES.'login.tpl');
define('_TVIEWSEARCH',THEMES.'view_search.tpl');
define('_TVIEWMAIN',THEMES.'view_main.tpl');
define('_TSURVEY',THEMES.'survey.tpl');
define('_TLIKE',THEMES.'view_like.tpl');
define('_TINDEX',THEMES.'index.tpl');
define('_TALERT',THEMES.'alert.tpl');

define('INDEXPATH','index.php');
define('SIGNPATH','index.php?op=signup');
define('OUTOPATH','index.php?op=out');

define('MODULES','modules/');
define('_PVIEWSEARCH','view_search.php');
define('_PVIEWMAIN','view_main.php');
define('_PSURVEY','survey.php');
define('_PLIKE','view_like.php');
define('_PMAIN','login.php');
define('_PSIGN','signup.php');

// unid
define('MEMBERID','m'.md5(uniqid(rand())));
define('CUSTOMERID','c'.md5(uniqid(rand())));

// OP
//define('ADDPIC','addPic');
define('VIEWSEARCH','view_search');
define('VIEWMAIN','view_main');
define('VIEWSURVEY','survey');
define('VIEWLIKE','like');
define('SIGN','signup');
define('OUT','out');
//define('ULOGIN','ulogin');

// 年齡區間
$age_range		= array(
	'20'		=> '20-25歲',
	'25'		=> '25-30歲',
	'30'		=> '30-35歲',
	'35'		=> '35~40歲',
	'40'		=> '40-45歲',
	'45'		=> '45-50歲',
	'50'		=> '50-55歲',
	'55'		=> '55-60歲',
	'60'		=> '60-65歲',
	'65'		=> '65歲以上',
);

// 總價區間
$money_range	= array(
	'300'		=> '300萬以下',
	'600'		=> '300-600萬以下',
	'1000'		=> '600-1000萬以下',
	'1500'		=> '1000-1500萬以下',
	'2000'		=> '1500-2000萬以下',
	'2001'		=> '2000萬以上'
);

// 坪數區間
$ping_range	= array(
	'20'		=> '20坪以下',
	'30'		=> '20~30坪',
	'40'		=> '30~40坪',
	'50'		=> '40~50坪',
	'51'		=> '50坪以上',
);

// 格局
$style_range	= array(
	'1'			=> '1房',
	'2'			=> '2房',
	'3'			=> '3房',
	'4'			=> '4房',
	'5'			=> '5房以上'
);

// 朝向
$direction_arr	= array(
	'1'			=> '坐東朝西',
	'2'			=> '坐西朝東',
	'3'			=> '坐南朝北',
	'4'			=> '坐北朝南',
	'5'			=> '坐東南朝西北',
	'6'			=> '坐西北朝東南',
	'7'			=> '坐東北朝西南',
	'8'			=> '坐西南朝東北',
);

// 評分類別
$scord_type = array('hot','user','content','nolike','new','search','like');

// 說明文字
$mem_1		= '<b>第一階段</b>：<br>
        1. 正常搜尋與瀏覽(搜尋 > 瀏覽列表 > 瀏覽內頁)。<br>
        2. <b>喜歡的房子</b>：(2-1、2-2 擇一操作)<br>
        &nbsp;&nbsp;&nbsp;&nbsp;2-1. 加入最愛<br>
        &nbsp;&nbsp;&nbsp;&nbsp;2-2. 瀏覽2次(or 以上)，按"重整"會累計。<br>
        &nbsp;&nbsp;&nbsp;&nbsp;2-3. 瀏覽間超過5秒(or 以上)。<br>
        3. <b>不喜歡的房子</b>：<br>
        &nbsp;&nbsp;&nbsp;&nbsp;3-1. 未加入最愛。<br>
        &nbsp;&nbsp;&nbsp;&nbsp;3-2. 只瀏覽過1次。<br>
        4. <b>在意的項目</b>：請於<label style="color:red">內容頁</label>操作(滑過/選取文字)。<br>
        5. 若您的瀏覽習慣，無加入最愛/滑過項目/選取文字，可不用。<br>
        6. 目的為建立(收集)<label style="color:red">操作紀錄</label>。';

$nomem_1 	= '<b>第一階段</b>：<br>
        1. 操作與(會員)相同，請參見[操作說明(會員)]。<br>
        2. 需扮演4種角色，每種角色切換時，需要關閉瀏覽器，重新開啟，才會抓新的ID。<br>
        3. <b>角色說明</b>：(以下請擇一操作)<br>
         &nbsp;&nbsp;&nbsp;&nbsp;角色1：有 加入最愛 的習慣。角色2：有 滑過/選取文字 的習慣。<br>
         &nbsp;&nbsp;&nbsp;&nbsp;角色3：以上兩種習慣皆無。 &nbsp;角色4：以上兩種習慣都有。<br>
        4. 或者您可以<label style="color:red">加入會員</label>，該會員可以為以上4種角色之一。<br>
        5. <b>目的</b>：<br>
         &nbsp;&nbsp;&nbsp;&nbsp;5-1. 建立(收集)<label style="color:red">操作紀錄</label>。<br>
         &nbsp;&nbsp;&nbsp;&nbsp;5-2. 創造多位相同 <label style="color:red">習慣/紀錄</label> 的人。';
$mem_2		= '<b>第二階段</b>：<br>
        1. 請於搜尋過後，於瀏覽清單頁，點擊各個推薦列表，進入房屋內頁，為此次推薦的房屋評分。<br>
        2. 填寫問卷(此為一次性問卷，請於測試過後再填寫，非會員可填寫N次)。<br>';
?>