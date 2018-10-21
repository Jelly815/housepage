<?php
session_start();
include_once('./lib/handling.php');

$db = new db_function();
//print_r($db->login('jelly6@yahoo.com','789456123'));exit;
$op = isset($_GET['op'])?$_GET['op']:'';
if($op==OUT){
		$_SESSION['uid']=null;
		$_SESSION['uname']=null;
		$_SESSION['umail']=null;
		$_SESSION['uphone']=null;
		$_SESSION['udepartment']=null;
		unset($_SESSION['uid']);
		unset($_SESSION['uname']);
		unset($_SESSION['umail']);
		unset($_SESSION['uphone']);
		unset($_SESSION['udepartment']);

		header('location:'.INDEXPATH);
}

if($db->conn){
	//if(chkLogin($uid)<>''){
		$tpl  = new  TemplatePower(_TMAIN);
		$tpl->assignInclude('header',_THEADER);
		$tpl->assignInclude('footer',_TFOOTER);
	//}
    switch($op){
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
		default:		//首頁
			$headTitle=HEADERTITLE;
			$tpl -> assignInclude('themes',_PINDEX);

    }
	//$tpl -> prepare ();

	if(isset($_SESSION['uname']) && $_SESSION['uname'] != ''){
		$tpl -> prepare ();
		$tpl -> assignGlobal('CSSPATH',CSSPATH);
		$tpl-> assign(array('HEADERTITLE'=>HEADERTITLE,'INDEXPATH'=>INDEXPATH,'TITLEMAIN'=>$headTitle));
		$tpl -> newBlock('loginBlock');
		$tpl-> assign(array('HI'=>HI,'USERNAME'=>$_SESSION['uname'],'TITLEADDPIC'=>TITLEADDPIC,'TITLEVIEWPIC'=>TITLEVIEWPIC,'LOGOUT'=>LOGOUT,'LOGINTOPATH'=>LOGINTOPATH,'ADDPICTOPATH'=>ADDPICTOPATH,'OUTOPATH'=>OUTOPATH));
		$tpl -> printToScreen ();
	}
	elseif($op==''){
		$tpl -> prepare ();
		$tpl -> assignGlobal('CSSPATH',CSSPATH);
		$tpl-> assign(array('HEADERTITLE'=>HEADERTITLE,'INDEXPATH'=>INDEXPATH,'TITLEMAIN'=>$headTitle,'HOMEPAGE'=>HOMEPAGE,'ADSEARCH'=>ADSEARCH));
		//$tpl -> newBlock('nologinBlock');
		$text = array(
			'LOGIN'		=> LOGIN,
			'LOGINPATH'	=> LOGINPATH,
			'TITLESIGN'	=> TITLESIGN,
			'SIGNPATH'	=> SIGNPATH,
			'COPYRIGHT'	=> COPYRIGHT,
			'HEADERTITLEDTAIL'	=> HEADERTITLEDTAIL,
			'ALERTXT05'	=> ALERTXT05
		);
		$tpl-> assign($text);
		$tpl -> printToScreen ();
	}
	//$tpl -> printToScreen ();

}else{
      echo 'no connection';exit;
}
?>
