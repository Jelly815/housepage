<?php
//DATABASE
define('SERVERNAME','127.0.0.1');
define('USERNAME','root');
define('USERPWD','root');
define('DATANAME','myweb');
define('DATATYPE','mysqli');

//PATH
define('THEMES','./template/html/');
define('CSSPATH','./template/css/');
define('UPLOADPICPATH','../160505pic/');
define('_TMAIN',THEMES.'main.tpl');
define('_THEADER',THEMES.'header.tpl');
define('_TFOOTER',THEMES.'footer.tpl');
define('_TSIGN',THEMES.'sign.tpl');
define('_TLOGIN',THEMES.'login.tpl');
define('_TSHOWPIC',THEMES.'showPic.tpl');
define('_TADDPIC',THEMES.'addPic.tpl');
define('_TEDITPIC',THEMES.'editPic.tpl');
define('_TINDEX',THEMES.'index.tpl');

define('INDEXPATH','index.php');
define('LOGINPATH','index.php?op=ulogin');
define('SIGNPATH','index.php?op=sign');
define('LOGINTOPATH','index.php?op=showPic');
define('ADDPICTOPATH','index.php?op=addPic');
define('EDITPICTOPATH','index.php?op=editPic');
define('DELPICTOPATH','index.php?op=delPic');
define('OUTOPATH','index.php?op=out');

define('MODULES','modules/');
define('_PSHOWPIC',MODULES.'showPic.php');
define('_PADDPIC',MODULES.'addPic.php');
define('_PEDITPIC',MODULES.'editPic.php');
define('_PMAIN','login.php');
define('_PSIGN','sign.php');
define('_PINDEX','showAll.php');

//OP
define('ADDPIC','addPic');
define('SHOWPIC','showPic'); 
define('EDITPIC','editPic');
define('DELPIC','delPic');
define('SIGN','sign');
define('OUT','out');
define('ULOGIN','ulogin');

//head
define('HEADERTITLE','公司內部攝影比賽');
define('LOGIN','員工登入');
define('TITLESIGN','參加者註冊');
define('TITLEADDPIC','新增作品');
define('TITLEVIEWPIC','我的作品');
define('TITLEEDITPIC','編輯作品');
define('HI','您好!');

//共用
define('PWD','密碼');
define('EMAIL','Email');
define('SUBMIT','送出');
define('RETURNBTN','返回');
define('LOGOUT','登出');
define('FILESIZE',2*1048576);
define('INSERTSUCC','上傳成功!');
define('EDITSUCC','編輯完成!');
define('INSERTUSERSUCC','註冊完成!');
define('EDIT','編輯');
define('DEL','刪除');
define('DELALERT','確定刪除?');

//員工登入
define('EMAILTXT','請輸入註冊的Email');
define('LOGINBTN','登入');
define('SIGNBTN','註冊');

//註冊
define('INPUTNAME','姓名');
define('INPUTPHONE','電話');
define('IMPUTPRTM','部門');

//新增作品
define('PICTITLE','作品名稱');
define('PICTITLEDSCPT','請輸入15字內作品名稱');
define('PIC','圖片');
define('PICDSCRIPT','僅可上傳.jpg檔案');
define('PICDSCRIPT2','每人最多上傳三張照片');
define('PICDSCRIPT3','檔案大小不可以超過2M');
define('PICAPTION','圖片說明');
define('PICAPDSCPT','請輸入150字內圖片說明');
define('PICFOLDER','160505pic');

//ALERT
define('ALERTXT01','不可包含中文字');
define('ALERTXT02','密碼需大於6個字');
define('ALERTXT03','Email格式錯誤');
define('ALERTXT04','已有相同Email');
define('ALERTXT05','登入錯誤，請重新登入!');
define('ALERTXT06','Error:請洽系統管理員!');
define('ALERTXT07','您作品數量已達上限');
define('ALERTXT08','請選擇檔案');
?>