<?php
session_start();
include_once('./lib/handling.php');
include_once('./lib/lang.php');
echo "<pre>";print_r($_SERVER['REMOTE_ADDR']);echo "</pre>";
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
	'ALERTXT11'		=> ALERTXT11
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
	case SIGN:		//註冊
		$text['PAGE_TITLE']			= SIGNUP;
		if(!isset($_SESSION['uname'])){
			include_once(_PSIGN);
			$text['SELECTED_SIGNUP']= $selected;
			$tpl->assignInclude('themes',_TSIGN);
		}else{
			header('location:'.INDEXPATH);
		}
	break;
	default:		//首頁
		//$headTitle = HEADERTITLE;
		$text['SELECTED_DEFAULT']	= $selected;
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

// 初始化搜尋
$city_arr 	= $db->get_table_value('`ex_area`','`id`,`name`','`city_id` = 0 AND `disable` = 0','`sort`');

foreach ($city_arr as $city_value) {
	//$tpl->newBlock("city_option");
	//$tpl->assign(array(
	//	'city_id'	=> $city_value['id'],
	//	'city_name'	=> $city_value['name'],
	//));
}
$tpl->printToScreen ();
?>
