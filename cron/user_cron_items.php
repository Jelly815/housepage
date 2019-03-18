<?php
ini_set('display_errors', 1);
error_reporting(E_ALL);

session_start();
include_once(__DIR__.'/../lib/handling.php');
include_once(__DIR__.'/../lib/lang.php');

$db 	= new db_function();

$sql    =   "SELECT main.`area`,main.`road`,main.`room`,main.`ping`,".
                        "main.`parking`,main.`age`,main.`floor`,main.`type`,".
                        "main.`direction`,main.`fee`,main.`builder`,main.`unit`,".
                        "main.`price`,main.`description`,main.`around`,".
                        "main.`status`,main.`community` ".
                "FROM   `ex_main` main,`ex_record_items` items,`ex_user` user ".
                "WHERE  items.`main_id` = main.`id` AND ".
                        "items.`user_id` = user.`unid` AND ".
                        "items.`last_time` >= (NOW() - INTERVAL 180 DAY) ";

$get_user   = $db->select_table_data('ex_record','DISTINCT `user_id`');
foreach ($get_user as $key => $get_user_value) {
	$items_arr['area']		= $items_arr['road']		=
	$items_arr['room']		= $items_arr['ping']		=
	$items_arr['parking']	= $items_arr['age']			=
	$items_arr['floor']		= $items_arr['type']		=
	$items_arr['direction']	= $items_arr['fee']			=
	$items_arr['builder']	= $items_arr['unit']		=
	$items_arr['price']		= $items_arr['description'] =
	$items_arr['around']	= $items_arr['status']		=
	$items_arr['community']	= array();

    // user uid
	$user_id	= $get_user_value['user_id'];

    // 可能喜歡的物件
    $like_sql   =   $sql.
                    " AND items.`times` > 1 ".
                    " AND items.`user_id` = ?";

    $like_sql   = $db->db->Prepare($like_sql);
    $main_res 	= $db->db->Execute($like_sql,array($user_id))->getArray();

    foreach ($main_res as $main_value) {
    	if($main_value['area'] != '')array_push($items_arr['area'], $main_value['area']);
    	if($main_value['road'] != '')array_push($items_arr['road'], $main_value['road']);
    	if($main_value['room'] != '0')array_push($items_arr['room'], $main_value['room']);
    	if($main_value['ping'] != '0')array_push($items_arr['ping'], $main_value['ping']);
    	array_push($items_arr['parking'], $main_value['parking']);
    	array_push($items_arr['age'], $main_value['age']);
    	array_push($items_arr['floor'], $main_value['floor']);
    	array_push($items_arr['type'], $main_value['type']);
    	if($main_value['direction'] != '')array_push($items_arr['direction'], $main_value['direction']);
    	array_push($items_arr['fee'], $main_value['fee']);
    	if($main_value['builder'] != '')array_push($items_arr['builder'], $main_value['builder']);
    	if($main_value['unit'] != '0')array_push($items_arr['unit'], $main_value['unit']);
    	if($main_value['price'] != '0')array_push($items_arr['price'], $main_value['price']);
    	if($main_value['description'] != '')array_push($items_arr['description'], ltrim(rtrim(trim(mb_substr($main_value['description'],4,5,'utf-8')),'坪'),'：'));
    	if($main_value['around'] != '')array_push($items_arr['around'], $main_value['around']);
    	array_push($items_arr['status'], $main_value['status']);
    	if($main_value['community'] != '')array_push($items_arr['community'], $main_value['community']);
    }

    $like_json  = json_encode($items_arr);
    // 儲存至資料庫
    $like_data      = array(
        'user_id'   => $user_id,
        'items'     => $like_json,
        'is_like'   => 1,
    );

    $db->insert_table_data('ex_record_items_obj',$like_data);

    // 可能不喜歡的物件
    $items_arr['area']      = $items_arr['road']        =
    $items_arr['room']      = $items_arr['ping']        =
    $items_arr['parking']   = $items_arr['age']         =
    $items_arr['floor']     = $items_arr['type']        =
    $items_arr['direction'] = $items_arr['fee']         =
    $items_arr['builder']   = $items_arr['unit']        =
    $items_arr['price']     = $items_arr['description'] =
    $items_arr['around']    = $items_arr['status']      =
    $items_arr['community'] = array();

    $no_like_sql=   $sql.
                    " AND items.`times` = 1 ".
                    " AND items.`user_id` = ?";

    $no_like_sql= $db->db->Prepare($no_like_sql);
    $main_res   = $db->db->Execute($no_like_sql,array($user_id))->getArray();

    foreach ($main_res as $main_value) {
        if($main_value['area'] != '')array_push($items_arr['area'], $main_value['area']);
        if($main_value['road'] != '')array_push($items_arr['road'], $main_value['road']);
        if($main_value['room'] != '0')array_push($items_arr['room'], $main_value['room']);
        if($main_value['ping'] != '0')array_push($items_arr['ping'], $main_value['ping']);
        array_push($items_arr['parking'], $main_value['parking']);
        array_push($items_arr['age'], $main_value['age']);
        array_push($items_arr['floor'], $main_value['floor']);
        array_push($items_arr['type'], $main_value['type']);
        if($main_value['direction'] != '')array_push($items_arr['direction'], $main_value['direction']);
        array_push($items_arr['fee'], $main_value['fee']);
        if($main_value['builder'] != '')array_push($items_arr['builder'], $main_value['builder']);
        if($main_value['unit'] != '0')array_push($items_arr['unit'], $main_value['unit']);
        if($main_value['price'] != '0')array_push($items_arr['price'], $main_value['price']);
        if($main_value['description'] != '')array_push($items_arr['description'], ltrim(rtrim(trim(mb_substr($main_value['description'],4,5,'utf-8')),'坪'),'：'));
        if($main_value['around'] != '')array_push($items_arr['around'], $main_value['around']);
        array_push($items_arr['status'], $main_value['status']);
        if($main_value['community'] != '')array_push($items_arr['community'], $main_value['community']);
    }

    $no_like_json  = json_encode($items_arr);

    // 儲存至資料庫
    $no_like_data   = array(
        'user_id'   => $user_id,
        'items'     => $no_like_json,
        'is_like'   => 0,
    );

    $db->insert_table_data('ex_record_items_obj',$no_like_data);
}

$get_user   = $db->select_table_data('ex_record_items_obj','*',array(array(0,'user_id','=','m1b414f0be20777c30e0423f441b09db8')));

foreach ($get_user as $key => $value) {
    if($value['is_like'] == 1){
        echo "<pre>";print_r('=====喜歡=====');echo "</pre>";
    }else{
        echo "<pre>";print_r('=====不喜歡=====');echo "</pre>";
    }
    $user_items = json_decode($value['items']);

    echo "<pre>";print_r($user_items);echo "</pre>";

    // 檢查community

    // 檢查status
    // 檢查around
    // 檢查description
    // 檢查price
    // 檢查unit
    // 檢查builder
    // 檢查fee
    // 檢查direction
    // 檢查type
    // 檢查floor
    // 檢查age
    // 檢查parking
    // 檢查ping
    // 檢查room
    // 檢查road
    // 檢查area
}
?>
