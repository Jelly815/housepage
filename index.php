<?php
session_start();
include_once('./lib/handling.php');
include_once('./lib/lang.php');

#echo "<pre>";print_r($_SERVER['REMOTE_ADDR']);echo "</pre>";
$db 	= new db_function();
$op 	= isset($_GET['op'])?filter_var($_GET['op'], FILTER_SANITIZE_STRING):'';
$selected 			= 'class="selected first"';

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
	'LOGIN_URL' 	=> '<a id="login_btn" href="javascript:;" title="'.LOGIN.'">'.LOGIN.'</a> | <a href="'.SIGNPATH.'" title="'.SIGNUP.'">'.SIGNUP.'</a>',
	'SUBMIT'		=> SUBMIT,
	'RETURNBTN'		=> RETURNBTN,
	'ALERTXT06'		=> ALERTXT06,
	'ALERTXT08'		=> ALERTXT08,
	'ALERTXT10'		=> ALERTXT10,
	'ALERTXT11'		=> ALERTXT11,
	'SIGNPATH'		=> SIGNPATH
);

if(isset($_SESSION['uname'])){
	$text['USER_NAME']	= HI.$_SESSION['uname'];
	$text['LOGIN_URL']	= '<a id="logout_btn" href="javascript:;" title="'.LOGOUT.'">'.LOGOUT.'</a>';
}

// 樣板
$tpl  	= new  TemplatePower(_TMAIN);
$tpl->assignInclude('header',_THEADER);
$tpl->assignInclude('footer',_TFOOTER);
$tpl->assignInclude('login',_TLOGIN);
$tpl->assignInclude('alert',_TALERT);

$text['SELECTED_DEFAULT']= $selected;
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


	case ULOGIN:	//登入
		if(chkLogin($uid)<>'')header('location:'.LOGINTOPATH);
		else{
			include_once(_PMAIN);
		}
	  break;
	 */
	case VIEWSEARCH:		// view all
		$text['PAGE_TITLE']			= TITLEVIEWSEARCH;
		include_once(_PVIEWSEARCH);
		$tpl->assignInclude('themes',_TVIEWSEARCH);
	break;
	case SIGN:		//註冊
		$text['PAGE_TITLE']			= SIGNUP;
		if(!isset($_SESSION['uname'])){
			include_once(_PSIGN);
			$text['SELECTED_SIGNUP']	= $selected;
			$text['SELECTED_DEFAULT']	= '';
			$tpl->assignInclude('themes',_TSIGN);
		}else{
			header('location:'.INDEXPATH);
		}
	break;
	default:		//首頁
		//$headTitle = HEADERTITLE;
		$tpl -> assignInclude('themes',_TINDEX);

}
$tpl->prepare ();
$tpl->assignGlobal(array(
	'CSSPATH'  		=> CSSPATH,
    'JSPATH'  		=> JSPATH
));
$tpl->assign($text);
if($op == ''){
	$tpl->newBlock("index_header");
}

$tpl->printToScreen ();
?>
