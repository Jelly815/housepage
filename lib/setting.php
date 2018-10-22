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
define('UPLOADPICPATH','../160505pic/');
define('_TMAIN',THEMES.'main.tpl');
define('_THEADER',THEMES.'header.tpl');
define('_TFOOTER',THEMES.'footer.tpl');
define('_TSIGN',THEMES.'signup.tpl');
define('_TLOGIN',THEMES.'login.tpl');
define('_TSHOWPIC',THEMES.'showPic.tpl');
define('_TADDPIC',THEMES.'addPic.tpl');
define('_TEDITPIC',THEMES.'editPic.tpl');
define('_TINDEX',THEMES.'index.tpl');
define('_TALERT',THEMES.'alert.tpl');

define('INDEXPATH','index.php');
define('LOGINPATH','index.php?op=ulogin');
define('SIGNPATH','index.php?op=signup');
//define('LOGINTOPATH','index.php?op=showPic');
define('ADDPICTOPATH','index.php?op=addPic');
define('EDITPICTOPATH','index.php?op=editPic');
define('DELPICTOPATH','index.php?op=delPic');
define('OUTOPATH','index.php?op=out');

define('MODULES','modules/');
define('_PSHOWPIC',MODULES.'showPic.php');
define('_PADDPIC',MODULES.'addPic.php');
define('_PEDITPIC',MODULES.'editPic.php');
define('_PMAIN','login.php');
define('_PSIGN','signup.php');
define('_PINDEX','showAll.php');

// OP
define('ADDPIC','addPic');
define('SHOWPIC','showPic');
define('EDITPIC','editPic');
define('DELPIC','delPic');
define('SIGN','signup');
define('OUT','out');
define('ULOGIN','ulogin');
?>