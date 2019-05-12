<?php
session_start();
include_once('./lib/handling.php');
include_once('./lib/lang.php');

$db         = new db_function();
$action     = isset($_GET['action'])?$_GET['action']:'';
$log_msg    = array('status' => true,'msg' => '','data' => array());

switch($action){
    // 登入
	case 'login':
		$user_mail 	= isset($_POST['user'])?filter_var($_POST['user'], FILTER_VALIDATE_EMAIL):'';
		$user_psw 	= isset($_POST['pwd'])?filter_var($_POST['pwd'], FILTER_SANITIZE_STRING):'';

		$user_psw 	= md5($user_psw);

        $re_array   = $db->login($user_mail,$user_psw);

        if(!empty($re_array)){
            $_SESSION['uname']  = $re_array[0]['ex_name'];
            $_SESSION['umail']  = $re_array[0]['ex_mail'];
            $log_msg['msg'] = HI.$_SESSION['uname'];
        }else{
            $log_msg    = array('status' => false,'msg' => ALERTXT05);
        }

        echo json_encode($log_msg);
	break;
    // 登出
    case 'logout':
        $_SESSION['uname']  = null;
        $_SESSION['umail']  = null;
        unset($_SESSION['uname']);
        unset($_SESSION['umail']);

        header("Refresh:0; url=".INDEXPATH);
    break;
    // 註冊
    case 'signup':
        $profile_hid    = isset($_POST['profile_hid'])?$_POST['profile_hid']:'';

        if(str_replace(';;', '', $profile_hid) == ''){
            exit(json_encode(array('status' => false,'msg' => ALERTXT06)));
        }else{
            list($name,$pwd,$email,$age) = explode(';;', $profile_hid);
            $unid       = MEMBERID;
            $name       = filter_var($name, FILTER_SANITIZE_STRING);
            $pwd        = md5($pwd);
            $email      = filter_var($email, FILTER_SANITIZE_EMAIL);
            $age        = filter_var($age, FILTER_VALIDATE_INT);


            $data       = array($unid,$name,$pwd,$email,$age);
            $dataArr    = $db->add_user($data);

            if(!empty($dataArr)){
                $log_msg    = array('status' => true,'msg' => '','data' => array());
                $log_msg['data'] = $dataArr;
            }else{
                $log_msg    = array('status' => false,'msg' => ALERTXT06);
            }
        }

        echo json_encode($log_msg);
    break;
    // 檢查mail重複
    case 'chkmail':
        $user_mail  = isset($_POST['email'])?filter_var($_POST['email'], FILTER_VALIDATE_EMAIL):'';

        $re_chk     = $db->chk_mail($user_mail);

        if(!$re_chk){
            $log_msg    = array('status' => False,'msg' => ALERTXT04);
        }

        echo json_encode($log_msg);
    break;
    // 取得地區
    case 'getarea':
        $city_id    = isset($_GET['city_id'])?filter_var($_GET['city_id'], FILTER_VALIDATE_INT) + 0:'';
        $get_area   = $db->get_table_value('`ex_area`','`id`,`name`',"`city_id` = $city_id AND `disable` = 0",'`sort`');
        $re_area    = array();
        foreach ($get_area as $area_val) {
            $re_area[]  = array(
                'text'  => $area_val['name'],
                'value' => $area_val['id']
            );
        }

        $json_file  = fopen("json/data.json", "w") or die("Unable to open file!");
        $w_json     = json_encode($re_area);
        fwrite($json_file, $w_json);
        fclose($json_file);

        echo $w_json;
    break;
    case 'search_view':
        $area       = isset($_POST['area'])?explode(',', filter_var($_POST['area'], FILTER_SANITIZE_STRING)):array();
        $price      = isset($_POST['price'])?explode(',', filter_var($_POST['price'], FILTER_SANITIZE_STRING)):array();
        $type       = isset($_POST['type'])?explode(',', filter_var($_POST['type'], FILTER_SANITIZE_STRING)):array();
        $room       = isset($_POST['room'])?explode(',', filter_var($_POST['room'], FILTER_SANITIZE_STRING)):array();
        $ping       = isset($_POST['ping'])?explode(',', filter_var($_POST['ping'], FILTER_SANITIZE_STRING)):array();

        // 區域
            $area_str   = '';
            foreach ($area as $key => $value) {
                $area_str .= "'".$value."',";
            }
            $area       = $db->select_table_data('ex_area','id',array(array(2,'name','IN ('.rtrim($area_str,',').')','')));
            $area_str   = '';
            foreach ($area as $key => $value) {
                $area_str  .= $value['id'].",";
            }
        // 金額
            $price_str   = '';
            $min = $small = $large = $max = 0;

            foreach ($price as $key => $value) {
                $var_strpos = strpos($value,"萬以上");

                if($var_strpos){
                    $value = str_replace("萬以上", '', $value);
                    $max   = $value;
                }else{
                    $value = str_replace("萬以下", '', $value);
                    $val_arr = explode('-', $value);

                    if(count($val_arr) == 2){
                        if($small != 0){
                            $small = ($val_arr[0] < $small)?$val_arr[0]:$small;
                        }else{
                            $small = $val_arr[0];
                        }

                        if($large != 0){
                            $large = ($val_arr[1] > $large)?$val_arr[1]:$large;
                        }else{
                            $large = $val_arr[1];
                        }
                    }else{
                        $min   = $val_arr[0];
                    }
                }
            }

            $price_str = ($min != 0)?"`price` <= {$min} ":'';
            if($price_str != ''){
                $price_str = ($small != 0)?$price_str." OR `price` BETWEEN {$small} AND {$large} ":$price_str;
            }else{
                $price_str = ($small != 0)?"`price` BETWEEN {$small} AND {$large} ":$price_str;
            }
            if($price_str != ''){
                $price_str = ($max != 0)?$price_str." OR `price` >= {$max} ":$price_str;
            }else{
                $price_str = ($max != 0)?"`price` >= {$max} ":$price_str;
            }
        // 類型
            $type_str   = '';
            foreach ($type as $key => $value) {
                $type_str .= "'".$value."',";
            }
            $type       = $db->select_table_data('ex_type','id',array(array(2,'name','IN ('.rtrim($type_str,',').')','')));
            $type_str   = '';
            foreach ($type as $key => $value) {
                $type_str  .= $value['id'].",";
            }
        // 房數
            $room_str   = '';
            $max        = 0;
            foreach ($room as $key => $value) {
                $var_strpos = strpos($value,"及以上");

                if($var_strpos){
                    $value = str_replace("房及以上", '', $value);
                    $max   = $value;
                }elseif($value != ''){
                    $value = str_replace("房", '', $value);
                    $room_str .= $value.',';
                }
            }

            $room_str = ($max != '')?"`room` IN (".rtrim($room_str,',').") OR `room` >= $max ":(($room_str != '')?"`room` IN (".rtrim($room_str,',').") ":'');
        // 坪數
            $ping_str   = '';
            $min = $small = $large = $max = 0;

            foreach ($ping as $key => $value) {
                $var_strpos = strpos($value,"坪及以上");

                if($var_strpos){
                    $value = str_replace("坪及以上", '', $value);
                    $max   = $value;
                }else{
                    $value = str_replace("坪以下", '', $value);
                    $val_arr = explode('-', $value);

                    if(count($val_arr) == 2){
                        if($small != 0){
                            $small = ($val_arr[0] < $small)?$val_arr[0]:$small;
                        }else{
                            $small = $val_arr[0];
                        }

                        if($large != 0){
                            $large = ($val_arr[1] > $large)?$val_arr[1]:$large;
                        }else{
                            $large = $val_arr[1];
                        }
                    }else{
                        $min   = $val_arr[0];
                    }
                }
            }

            $ping_str = ($min != 0)?"`ping` <= {$min} ":'';
            if($ping_str != ''){
                $ping_str = ($small != 0)?$ping_str." OR `ping` BETWEEN {$small} AND {$large} ":$ping_str;
            }else{
                $ping_str = ($small != 0)?"`ping` BETWEEN {$small} AND {$large} ":$ping_str;
            }
            if($ping_str != ''){
                $ping_str = ($max != 0)?$ping_str." OR `ping` >= {$max} ":$ping_str;
            }else{
                $ping_str = ($max != 0)?"`ping` >= {$max} ":$ping_str;
            }

        // 查詢開始
            $select_arr = array();
            // 區域
            if($area_str != ''){
                $select_arr[] = array(2,'area','IN ('.rtrim($area_str,',').')','');
            }
            // 金額
            if($price_str != ''){
                $select_arr[] = array(3,$price_str);
            }
            // 類型
            if($type_str != ''){
                $select_arr[] = array(2,'type','IN ('.rtrim($type_str,',').')','');
            }
            // 房數
            if($room_str != ''){
                $select_arr[] = array(3,$room_str);
            }
            // 坪數
            if($ping_str != ''){
                $select_arr[] = array(3,$ping_str);
            }

            $main_data  = $db->select_table_data('ex_main',
                array('unid','number','area','title','road','room','style','ping',
                    'age','floor','type','parking','unit','view_num'),
                $select_arr,
                array('update_time' => 'DESC'),
                1,4,1);
            foreach ($main_data as $key => $value) {
                $main_data[$key]['imgs'] = array();
                $house_img  = $db->select_table_data('ex_images','img_url',array(array(0,'number','=',$value['number'])));
                $img    = array();
                $main_data[$key]['imgs'] = $house_img;

            }

        echo json_encode($main_data);
    break;
	default:

}
?>
