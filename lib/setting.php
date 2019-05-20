<?php
// DATABASE
define('SERVERNAME','127.0.0.1');
define('USERNAME','root');
define('USERPWD','root');
define('DATANAME','myweb');
define('DATATYPE','mysqli');
define('ADMINMAIL',"jellyandjar@yahoo.com.tw");

// PATH
define('THEMES','./template/html/');
define('CSSPATH','./template/css/');
define('JSPATH','./js/');
define('PYTHONPATH','D:/xampp/htdocs/housepage/python/main.py');
#define('PYTHONPATH','python F:/xampp/htdocs/housepage/python/main.py');
define('_TMAIN',THEMES.'main.tpl');
define('_THEADER',THEMES.'header.tpl');
define('_TFOOTER',THEMES.'footer.tpl');
define('_TSIGN',THEMES.'signup.tpl');
define('_TLOGIN',THEMES.'login.tpl');
define('_TVIEWSEARCH',THEMES.'view_search.tpl');
define('_TVIEWMAIN',THEMES.'view_main.tpl');
define('_TSURVEY',THEMES.'survey.tpl');
define('_TINDEX',THEMES.'index.tpl');
define('_TALERT',THEMES.'alert.tpl');

define('INDEXPATH','index.php');
define('SIGNPATH','index.php?op=signup');
define('OUTOPATH','index.php?op=out');

define('MODULES','modules/');
define('_PVIEWSEARCH','view_search.php');
define('_PVIEWMAIN','view_main.php');
define('_PSURVEY','survey.php');
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
?>