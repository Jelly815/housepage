<?php
session_start();
include_once('./lib/handling.php');
include_once('./lib/lang.php');

$db 	= new db_function();
//print_r($db->login('jelly6@yahoo.com','789456123'));exit;
$op 	= isset($_GET['op'])?$_GET['op']:'';

$text 	= array(
	'ADMINMAIL'		=> ADMINMAIL,
	'HEADERTITLE' 	=> HEADERTITLE,
	'INDEXPATH'		=> INDEXPATH,
	'HOMEPAGE'		=> HOMEPAGE,
	'ADSEARCH'		=> ADSEARCH,
	'COPYRIGHT'		=> COPYRIGHT,
	'HEADERTITLEDTAIL'	=> HEADERTITLEDTAIL,
	'OUTOPATH'		=> OUTOPATH,
	'LOGOUT'		=> LOGOUT,
	'LOGIN'			=> LOGIN,
	'LOGIN_URL' 	=> '<a id="login_btn" href="javascript:;" title="'.LOGIN.'">'.LOGIN.'</a> | <a href="'.SIGNPATH.'" title="'.SIGNUP.'">'.SIGNUP.'</a>'
);

if(isset($_SESSION['uname']) && $op == OUT){
	$_SESSION['uname']	= null;
	$_SESSION['umail']	= null;
	unset($_SESSION['uname']);
	unset($_SESSION['umail']);

	header('location:'.INDEXPATH);
}elseif(isset($_SESSION['uname'])){
	$text['USER_NAME']	= HI.$_SESSION['uname'];
	$text['LOGIN_URL']	= '<a id="logout_btn" href="javascript:;" title="'.LOGOUT.'">'.LOGOUT.'</a>';
}

// 樣板
$tpl  	= new  TemplatePower(_TMAIN);
$tpl->assignInclude('header',_THEADER);
$tpl->assignInclude('footer',_TFOOTER);
$tpl->assignInclude('login',_TLOGIN);
$tpl->assignInclude('alert',_TALERT);
$tpl->prepare ();

$tpl->assignGlobal(array(
	'CSSPATH'  		=> CSSPATH,
    'JSPATH'  		=> JSPATH));

$tpl->assign($text);

switch($op){
	/*
	case ADDPIC:	//新增作品
		if(chkLogin($uid)<>''){
			$headTitle=TITLEADDPIC;
			$tpl -> assignInclude('themes',_PADDPIC);
		}else header('location:'.OUTOPATH);
	  break;
	case SHOWPIC:	//瀏覽作品
		if(chkLogin($uid)<>''){
			$headTitle=TITLEVIEWPIC;
			$tpl -> assignInclude('themes',_PSHOWPIC);
		}else header('location:'.OUTOPATH);
	  break;
	case EDITPIC:	//編輯作品
		if(chkLogin($uid)<>''){
			$headTitle=TITLEEDITPIC;
			$tpl -> assignInclude('themes',_PEDITPIC);
		}else header('location:'.OUTOPATH);
	  break;
	case DELPIC:	//刪除作品
		if(chkLogin($uid)<>''){

		}else header('location:'.OUTOPATH);
	  break;
	case SIGN:		//註冊
		if(chkLogin($uid)<>'')header('location:'.LOGINTOPATH);
		else{
			include_once(_PSIGN);
		}
	  break;

	case ULOGIN:	//登入
		if(chkLogin($uid)<>'')header('location:'.LOGINTOPATH);
		else{
			include_once(_PMAIN);
		}
	  break;
	 */
	default:		//首頁
		$headTitle=HEADERTITLE;
		$tpl -> assignInclude('themes',_PINDEX);

}

$tpl-> assign($text);
$tpl -> printToScreen ();
?>
