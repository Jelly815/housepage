<?php
session_start();
include_once('./lib/handling.php');
include_once('./lib/lang.php');

$db         = new db_function();
$action     = isset($_GET['action'])?$_GET['action']:'';
$log_msg    = array('status' => True,'msg' => '','data' => array());

switch($action){
	case 'login':	//新增作品
		$user_mail 	= isset($_POST['user'])?filter_var($_POST['user'], FILTER_VALIDATE_EMAIL):'';
		$user_psw 	= isset($_POST['pwd'])?filter_var($_POST['pwd'], FILTER_SANITIZE_STRING):'';

		$user_psw 	= md5($user_psw);

        $re_array   = $db->login($user_mail,$user_psw);

        if(!empty($re_array)){
            $_SESSION['uname']  = $re_array[0]['ex_name'];
            $_SESSION['umail']  = $re_array[0]['ex_mail'];
            $log_msg['msg'] = HI.$_SESSION['uname'];
        }else{
            $log_msg    = array('status' => False,'msg' => ALERTXT05);
        }

        echo json_encode($log_msg);
	break;

	default:

}
?>
