<?php
session_start();
include_once('./lib/handling.php');
include_once('./lib/lang.php');

if(!isset($_SESSION['uid'])){
    $_SESSION['uid'] = CUSTOMERID;
}
echo "<pre>";print_r($_SESSION['uid']);echo "</pre>";
$db 	= new db_function();
$op 	= isset($_GET['op'])?filter_var($_GET['op'], FILTER_SANITIZE_STRING):'';
$selected 			= 'class="selected first"';

$text 	= array(
	'ADMINMAIL'		=> ADMINMAIL,
	'HEADERTITLE' 	=> HEADERTITLE,
	'PAGETITLE' 	=> HEADERTITLE,
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
	'SIGNPATH'		=> SIGNPATH,
	'SURVEY'		=> TITLESURVEY,
	'LIKE'			=> TITLELIKE,
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

$area_arr   = array();
// 區域
$area_all   = $db->select_table_data('ex_area','id,name',array(array(0,'city_id','=',275)));
foreach ($area_all as $key => $value) {
	$area_arr[$value['id']] = $value['name'];
}
// 顯示問卷調查按鈕
$survey_data  = $db->select_table_data('ex_survey_ans',
    array('user_id'),
    array(array(0,'user_id','=',$_SESSION['uid'])),
    array(),2);
$text['SHOWSURVEY'] = (!empty($survey_data))?'style="display: none"':'';

switch($op){
	case VIEWLIKE:		// view like
		$text['HEADERTITLE']		= TITLELIKE;
		$text['SELECTED_LIKE']		= $selected;
		$text['SELECTED_DEFAULT']	= $text['SELECTED_SIGNUP'] = $text['SELECTED_SURVEY'] = '';
		$tpl->assignInclude('themes',_TLIKE);
		include_once(_PLIKE);
	break;
	case VIEWSURVEY:		// view survey
		$text['HEADERTITLE']		= TITLESURVEY;
		$text['SELECTED_SURVEY']	= $selected;
		$text['SELECTED_DEFAULT']	= $text['SELECTED_SIGNUP'] = $text['SELECTED_LIKE'] = '';
		$tpl->assignInclude('themes',_TSURVEY);
		include_once(_PSURVEY);
	break;
	case VIEWMAIN:		// view main
		$text['HEADERTITLE']			= TITLEVIEWMAIN;
		$tpl->assignInclude('themes',_TVIEWMAIN);
		include_once(_PVIEWMAIN);
	break;
	case VIEWSEARCH:		// view all
		$text['HEADERTITLE']			= TITLEVIEWSEARCH;
		$tpl->assignInclude('themes',_TVIEWSEARCH);
		include_once(_PVIEWSEARCH);
	break;
	case SIGN:		//註冊
		$text['HEADERTITLE']			= SIGNUP;
		if(!isset($_SESSION['uname'])){
			$text['SELECTED_SIGNUP']	= $selected;
			$text['SELECTED_DEFAULT']	= $text['SELECTED_SURVEY'] = $text['SELECTED_LIKE'] = '';
			$tpl->assignInclude('themes',_TSIGN);
			include_once(_PSIGN);
		}else{
			header('location:'.INDEXPATH);
		}
	break;
	default:		//首頁
		$tpl -> assignInclude('themes',_TINDEX);
		$tpl->prepare ();
		$tpl->newBlock("index_header");
}

$tpl->gotoBlock("_ROOT");
$tpl->assignGlobal(array(
	'CSSPATH'  		=> CSSPATH,
    'JSPATH'  		=> JSPATH
));
$tpl->assign($text);
$tpl->printToScreen ();
?>
