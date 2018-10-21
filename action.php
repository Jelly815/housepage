<?php
session_start();
include_once('./lib/handling.php');

$action = isset($_GET['action'])?$_GET['action']:'';
switch($action){    
	case 'login':	//新增作品
		$user_mail 	= isset($_POST['user'])?filter_var($_POST['user'], FILTER_VALIDATE_EMAIL):'';
		$user_psw 	= isset($_POST['pwd'])?filter_var($_POST['pwd'], FILTER_SANITIZE_STRING):'';
echo $user_mail;exit;
		$user_psw 	= md5($user_psw);
        
        $sql = sprintf("select * from `ex_user` where ex_mail=%s and ex_pwd='%s'",$email,$pwd);
        $array = $db->getRow($sql);

        if(!empty($array)){
           $_SESSION['uid']=$array['ex_id'];
           $_SESSION['uname']=$array['ex_name'];
           $_SESSION['umail']=$array['ex_mail'];
           $_SESSION['uphone']=$array['ex_phone'];
           $_SESSION['udepartment'] =$array['ex_department'];
           header("location: ".LOGINTOPATH);
        }else{
           $error=ALERTXT05;
        }
	  break;
	
	default:
		
}
?>
