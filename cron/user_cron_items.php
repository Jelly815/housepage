<?php
ini_set('display_errors', 1);
error_reporting(E_ALL);

session_start();
include_once(__DIR__.'/../lib/handling.php');
include_once(__DIR__.'/../lib/lang.php');

$db         = new db_function();

$default_sql=   "SELECT SUM(score = 1) AS 'one',SUM(score = 2) AS 'two',SUM(score = 3) AS 'three',".
                    "SUM(score = 4) AS 'four',SUM(score = 5) AS 'five', ".
                    "(SUM(score = 1) +SUM(score = 2)+SUM(score = 3)+SUM(score = 4)+SUM(score = 5)) AS 'total'".
                "FROM   `ex_score` ";

$default_into   = "REPLACE INTO `ex_score_analysis` (`id`,`type_`,`value_`,`math_`) VALUES ";

// 預測喜歡
$sql_key    = 'like';
$sql_arr    = array();
$like_sql   = $default_sql."WHERE  `type` = '{$sql_key}' ";
$like_sql   = $db->db->Prepare($like_sql);
$like_res   = $db->db->Execute($like_sql)->getArray();

foreach ($like_res as $key => $value) {
    if(isset($value['one'])){
        $math   = round(($value['one'] / $value['total']),2);
        $sql_arr= array('type_' => $sql_key,'value_' => '1','math_' => $math);
        $db->insert_table_data('ex_score_analysis',$sql_arr);
    }

    if(isset($value['two'])){
        $math   = round(($value['two'] / $value['total']),2);
        $sql_arr= array('type_' => $sql_key,'value_' => '2','math_' => $math);
        $db->insert_table_data('ex_score_analysis',$sql_arr);
    }

    if(isset($value['three'])){
        $math   = round(($value['three'] / $value['total']),2);
        $sql_arr= array('type_' => $sql_key,'value_' => '3','math_' => $math);
        $db->insert_table_data('ex_score_analysis',$sql_arr);
    }

    if(isset($value['four'])){
        $math   = round(($value['four'] / $value['total']),2);
        $sql_arr= array('type_' => $sql_key,'value_' => '4','math_' => $math);
        $db->insert_table_data('ex_score_analysis',$sql_arr);
    }

    if(isset($value['five'])){
        $math   = round(($value['five'] / $value['total']),2);
        $sql_arr= array('type_' => $sql_key,'value_' => '5','math_' => $math);
        $db->insert_table_data('ex_score_analysis',$sql_arr);
    }
}

// 別人喜歡
$sql_key    = 'user';
$user_sql   = $default_sql."WHERE  `type` = '{$sql_key}' ";
$user_sql   = $db->db->Prepare($user_sql);
$user_res   = $db->db->Execute($user_sql)->getArray();
foreach ($user_res as $key => $value) {
    if(isset($value['one'])){
        $math   = round(($value['one'] / $value['total']),2);
        $sql_arr= array('type_' => $sql_key,'value_' => '1','math_' => $math);
        $db->insert_table_data('ex_score_analysis',$sql_arr);
    }

    if(isset($value['two'])){
        $math   = round(($value['two'] / $value['total']),2);
        $sql_arr= array('type_' => $sql_key,'value_' => '2','math_' => $math);
        $db->insert_table_data('ex_score_analysis',$sql_arr);
    }

    if(isset($value['three'])){
        $math   = round(($value['three'] / $value['total']),2);
        $sql_arr= array('type_' => $sql_key,'value_' => '3','math_' => $math);
        $db->insert_table_data('ex_score_analysis',$sql_arr);
    }

    if(isset($value['four'])){
        $math   = round(($value['four'] / $value['total']),2);
        $sql_arr= array('type_' => $sql_key,'value_' => '4','math_' => $math);
        $db->insert_table_data('ex_score_analysis',$sql_arr);
    }

    if(isset($value['five'])){
        $math   = round(($value['five'] / $value['total']),2);
        $sql_arr= array('type_' => $sql_key,'value_' => '5','math_' => $math);
        $db->insert_table_data('ex_score_analysis',$sql_arr);
    }
}

// 不喜歡
$sql_key    = 'nolike';
$nolike_sql = $default_sql."WHERE  `type` = '{$sql_key}' ";
$nolike_sql = $db->db->Prepare($nolike_sql);
$nolike_res = $db->db->Execute($nolike_sql)->getArray();
foreach ($nolike_res as $key => $value) {
    if(isset($value['one'])){
        $math   = round(($value['one'] / $value['total']),2);
        $sql_arr= array('type_' => $sql_key,'value_' => '1','math_' => $math);
        $db->insert_table_data('ex_score_analysis',$sql_arr);
    }

    if(isset($value['two'])){
        $math   = round(($value['two'] / $value['total']),2);
        $sql_arr= array('type_' => $sql_key,'value_' => '2','math_' => $math);
        $db->insert_table_data('ex_score_analysis',$sql_arr);
    }

    if(isset($value['three'])){
        $math   = round(($value['three'] / $value['total']),2);
        $sql_arr= array('type_' => $sql_key,'value_' => '3','math_' => $math);
        $db->insert_table_data('ex_score_analysis',$sql_arr);
    }

    if(isset($value['four'])){
        $math   = round(($value['four'] / $value['total']),2);
        $sql_arr= array('type_' => $sql_key,'value_' => '4','math_' => $math);
        $db->insert_table_data('ex_score_analysis',$sql_arr);
    }

    if(isset($value['five'])){
        $math   = round(($value['five'] / $value['total']),2);
        $sql_arr= array('type_' => $sql_key,'value_' => '5','math_' => $math);
        $db->insert_table_data('ex_score_analysis',$sql_arr);
    }
}

// 內容
$sql_key    = 'content';
$content_sql= $default_sql."WHERE  `type` = '{$sql_key}' ";
$content_sql= $db->db->Prepare($content_sql);
$content_res= $db->db->Execute($content_sql)->getArray();
foreach ($content_res as $key => $value) {
    if(isset($value['one'])){
        $math   = round(($value['one'] / $value['total']),2);
        $sql_arr= array('type_' => $sql_key,'value_' => '1','math_' => $math);
        $db->insert_table_data('ex_score_analysis',$sql_arr);
    }

    if(isset($value['two'])){
        $math   = round(($value['two'] / $value['total']),2);
        $sql_arr= array('type_' => $sql_key,'value_' => '2','math_' => $math);
        $db->insert_table_data('ex_score_analysis',$sql_arr);
    }

    if(isset($value['three'])){
        $math   = round(($value['three'] / $value['total']),2);
        $sql_arr= array('type_' => $sql_key,'value_' => '3','math_' => $math);
        $db->insert_table_data('ex_score_analysis',$sql_arr);
    }

    if(isset($value['four'])){
        $math   = round(($value['four'] / $value['total']),2);
        $sql_arr= array('type_' => $sql_key,'value_' => '4','math_' => $math);
        $db->insert_table_data('ex_score_analysis',$sql_arr);
    }

    if(isset($value['five'])){
        $math   = round(($value['five'] / $value['total']),2);
        $sql_arr= array('type_' => $sql_key,'value_' => '5','math_' => $math);
        $db->insert_table_data('ex_score_analysis',$sql_arr);
    }
}

// 熱門
$sql_key    = 'hot';
$hot_sql    = $default_sql."WHERE  `type` = '{$sql_key}' ";
$hot_sql    = $db->db->Prepare($hot_sql);
$hot_res    = $db->db->Execute($hot_sql)->getArray();
foreach ($hot_res as $key => $value) {
    if(isset($value['one'])){
        $math   = round(($value['one'] / $value['total']),2);
        $sql_arr= array('type_' => $sql_key,'value_' => '1','math_' => $math);
        $db->insert_table_data('ex_score_analysis',$sql_arr);
    }

    if(isset($value['two'])){
        $math   = round(($value['two'] / $value['total']),2);
        $sql_arr= array('type_' => $sql_key,'value_' => '2','math_' => $math);
        $db->insert_table_data('ex_score_analysis',$sql_arr);
    }

    if(isset($value['three'])){
        $math   = round(($value['three'] / $value['total']),2);
        $sql_arr= array('type_' => $sql_key,'value_' => '3','math_' => $math);
        $db->insert_table_data('ex_score_analysis',$sql_arr);
    }

    if(isset($value['four'])){
        $math   = round(($value['four'] / $value['total']),2);
        $sql_arr= array('type_' => $sql_key,'value_' => '4','math_' => $math);
        $db->insert_table_data('ex_score_analysis',$sql_arr);
    }

    if(isset($value['five'])){
        $math   = round(($value['five'] / $value['total']),2);
        $sql_arr= array('type_' => $sql_key,'value_' => '5','math_' => $math);
        $db->insert_table_data('ex_score_analysis',$sql_arr);
    }
}

// 最新
$sql_key    = 'new';
$new_sql    = $default_sql."WHERE  `type` = '{$sql_key}' ";
$new_sql    = $db->db->Prepare($new_sql);
$new_res    = $db->db->Execute($new_sql)->getArray();
foreach ($new_res as $key => $value) {
    if(isset($value['one'])){
        $math   = round(($value['one'] / $value['total']),2);
        $sql_arr= array('type_' => $sql_key,'value_' => '1','math_' => $math);
        $db->insert_table_data('ex_score_analysis',$sql_arr);
    }

    if(isset($value['two'])){
        $math   = round(($value['two'] / $value['total']),2);
        $sql_arr= array('type_' => $sql_key,'value_' => '2','math_' => $math);
        $db->insert_table_data('ex_score_analysis',$sql_arr);
    }

    if(isset($value['three'])){
        $math   = round(($value['three'] / $value['total']),2);
        $sql_arr= array('type_' => $sql_key,'value_' => '3','math_' => $math);
        $db->insert_table_data('ex_score_analysis',$sql_arr);
    }

    if(isset($value['four'])){
        $math   = round(($value['four'] / $value['total']),2);
        $sql_arr= array('type_' => $sql_key,'value_' => '4','math_' => $math);
        $db->insert_table_data('ex_score_analysis',$sql_arr);
    }

    if(isset($value['five'])){
        $math   = round(($value['five'] / $value['total']),2);
        $sql_arr= array('type_' => $sql_key,'value_' => '5','math_' => $math);
        $db->insert_table_data('ex_score_analysis',$sql_arr);
    }
}

// 搜尋
$sql_key    = 'search';
$search_sql = $default_sql."WHERE  `type` = '{$sql_key}' ";
$search_sql = $db->db->Prepare($search_sql);
$search_res = $db->db->Execute($search_sql)->getArray();
foreach ($search_res as $key => $value) {
    if(isset($value['one'])){
        $math   = round(($value['one'] / $value['total']),2);
        $sql_arr= array('type_' => $sql_key,'value_' => '1','math_' => $math);
        $db->insert_table_data('ex_score_analysis',$sql_arr);
    }

    if(isset($value['two'])){
        $math   = round(($value['two'] / $value['total']),2);
        $sql_arr= array('type_' => $sql_key,'value_' => '2','math_' => $math);
        $db->insert_table_data('ex_score_analysis',$sql_arr);
    }

    if(isset($value['three'])){
        $math   = round(($value['three'] / $value['total']),2);
        $sql_arr= array('type_' => $sql_key,'value_' => '3','math_' => $math);
        $db->insert_table_data('ex_score_analysis',$sql_arr);
    }

    if(isset($value['four'])){
        $math   = round(($value['four'] / $value['total']),2);
        $sql_arr= array('type_' => $sql_key,'value_' => '4','math_' => $math);
        $db->insert_table_data('ex_score_analysis',$sql_arr);
    }

    if(isset($value['five'])){
        $math   = round(($value['five'] / $value['total']),2);
        $sql_arr= array('type_' => $sql_key,'value_' => '5','math_' => $math);
        $db->insert_table_data('ex_score_analysis',$sql_arr);
    }
}
/*
// 計算標準差
if (!function_exists('stats_standard_deviation')) {
    function stats_standard_deviation(array $val_arr, $sample = false) {
        $n = count($val_arr);
        if ($n === 0) {
            #trigger_error("The array has zero elements", E_USER_WARNING);
            return false;
        }
        if ($sample && $n === 1) {
            #trigger_error("The array has only 1 element", E_USER_WARNING);
            return false;
        }
        $mean = array_sum($val_arr) / $n;
        $carry = 0.0;
        foreach ($val_arr as $val) {
            $d = ((double) $val) - $mean;
            $carry += $d * $d;
        };
        if ($sample) {
           --$n;
        }
        return sqrt($carry / $n);
    }
}

$sql    =   "SELECT items.`main_id`,main.`area`,main.`road`,main.`room`,main.`ping`,".
                    "main.`parking`,main.`age`,main.`floor`,main.`type`,".
                    "main.`direction`,main.`fee`,main.`builder`,main.`unit`,".
                    "main.`price`,main.`description`,main.`around`,".
                    "main.`status`,main.`community` ".
            "FROM   `ex_main` main,`ex_record_items` items ".
            "WHERE  items.`main_id` = main.`id` AND ".
                    "items.`last_time` >= (NOW() - INTERVAL 180 DAY) ";

$get_user   = $db->select_table_data('ex_record','DISTINCT `user_id`');
foreach ($get_user as $key => $get_user_value) {
    $main_id_arr    = array();
    $items_arr      = array(
        'area'  => array(),'room' => array(),'parking' => array(),
        'floor' => array(),'direction' => array(),'builder' => array(),
        'price' => array(),'around' => array(),'community' => array(),
        'road'  => array(),'ping' => array(),'age' => array(),
        'type'  => array(),'fee' => array(),'unit' => array(),
        'description' => array(),'status' => array()
    );

    // user uid
	$user_id	= $get_user_value['user_id'];

    // 可能喜歡的物件
    $like_sql   =   $sql.
                    " AND (`items`.`times` > 1 OR `items`.`add_favorite` = 1) ".
                    " AND `items`.`user_id` = ?";

    $like_sql   = $db->db->Prepare($like_sql);
    $main_res 	= $db->db->Execute($like_sql,array($user_id))->getArray();

    foreach ($main_res as $main_value) {
        array_push($main_id_arr, (int)$main_value['main_id']);
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

// 儲存至資料庫(1:喜歡)
    $like_data      = array(
        'user_id'   => $user_id,
        'items'     => json_encode($items_arr),
        'is_like'   => 1,
    );

    $db->insert_table_data('ex_record_items_obj',$like_data);
// 儲存至資料庫(2:喜歡物件的main_id)
    $main_id_arr  = array_unique($main_id_arr,SORT_NUMERIC);
    $like_data      = array(
        'user_id'   => $user_id,
        'items'     => implode(',',$main_id_arr),
        'is_like'   => 2,
    );

    $db->insert_table_data('ex_record_items_obj',$like_data);

    // 可能不喜歡的物件
    $items_arr  = array(
        'area' => array(),'room' => array(),'parking' => array(),
        'floor' => array(),'direction' => array(),'builder' => array(),
        'price' => array(),'around' => array(),'community' => array(),
        'road' => array(),'ping' => array(),'age' => array(),
        'type' => array(),'fee' => array(),'unit' => array(),
        'description' => array(),'status' => array()
    );

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

// 儲存至資料庫(0:不喜歡)
    $no_like_data   = array(
        'user_id'   => $user_id,
        'items'     => json_encode($items_arr),
        'is_like'   => 0,
    );

    $db->insert_table_data('ex_record_items_obj',$no_like_data);

    // User可能喜歡的物件
    $get_user   = $db->select_table_data('ex_record_items_obj','*',
                    array(array(0,'user_id','=',$user_id),array(0,'is_like','=',1)));
    $user_items = array();
    foreach ($get_user as $key => $value) {
        $item_matrix = array();

        $user_items = json_decode($value['items']);

        if($user_items){
        // 檢查community
        array_push($item_matrix, (!empty($user_items->community)?similar_matrix_value($user_items->community):0));

        // 檢查status
        array_push($item_matrix, similar_matrix_value($user_items->status));

        // 檢查around

        // 檢查description
        array_push($item_matrix, range_matrix_value($user_items->description));

        // 檢查price
        array_push($item_matrix, range_matrix_value($user_items->price));

        // 檢查unit
        array_push($item_matrix, range_matrix_value($user_items->unit));

        // 檢查builder
        array_push($item_matrix, similar_matrix_value($user_items->builder));

        // 檢查fee
        array_push($item_matrix, range_matrix_value($user_items->fee));

        // 檢查direction
        array_push($item_matrix, similar_matrix_value($user_items->direction));

        // 檢查type
        array_push($item_matrix, similar_matrix_value($user_items->type));

        // 檢查floor
        array_push($item_matrix, similar_matrix_value($user_items->floor));

        // 檢查age
        array_push($item_matrix, range_matrix_value($user_items->age));

        // 檢查parking
        array_push($item_matrix, similar_matrix_value($user_items->parking));

        // 檢查ping
        array_push($item_matrix, range_matrix_value($user_items->ping));

        // 檢查room
        array_push($item_matrix, similar_matrix_value($user_items->room));

        // 檢查area
        array_push($item_matrix, similar_matrix_value($user_items->area));

// 儲存至資料庫(3:喜歡的在意項目)
        $like_matrix_data   = array(
            'user_id'   => $user_id,
            'items'     => json_encode($item_matrix),
            'is_like'   => 3,
        );

        $db->insert_table_data('ex_record_items_obj',$like_matrix_data);
        }
    }

    // User可能不喜歡的物件
    $user_items2 = array();
    $get_user2   = $db->select_table_data('ex_record_items_obj','*',
                    array(array(0,'user_id','=',$user_id),array(0,'is_like','=',0)));
    foreach ($get_user2 as $key => $value) {
        $item_matrix2 = array();

        $user_items2 = json_decode($value['items']);
        if($user_items2){
        // 檢查community
        if(isset($item_matrix[0]) && $item_matrix[0] != 0){
            array_push($item_matrix2, similar_matrix_value($user_items->community,$user_items2->community));
        }else{
            array_push($item_matrix2, 0);
        }

        // 檢查status
        if(isset($item_matrix[1]) && $item_matrix[1] != 0){
            array_push($item_matrix2, similar_matrix_value($user_items->status,$user_items2->status));
        }else{
            array_push($item_matrix2, 0);
        }

        // 檢查around

        // 檢查description
        if(isset($item_matrix[2]) && $item_matrix[2] != 0){
            array_push($item_matrix2, range_matrix_value_nolike($user_items->description,$user_items2->description));
        }else{
            array_push($item_matrix2, 0);
        }

        // 檢查price
        if(isset($item_matrix[3]) && $item_matrix[3] != 0){
            array_push($item_matrix2, range_matrix_value_nolike($user_items->price,$user_items2->price));
        }else{
            array_push($item_matrix2, 0);
        }

        // 檢查unit
        if(isset($item_matrix[4]) && $item_matrix[4] != 0){
            array_push($item_matrix2, range_matrix_value_nolike($user_items->unit,$user_items2->unit));
        }else{
            array_push($item_matrix2, 0);
        }

        // 檢查builder
        if(isset($item_matrix[5]) && $item_matrix[5] != 0){
            array_push($item_matrix2, similar_matrix_value($user_items->builder,$user_items2->builder));
        }else{
            array_push($item_matrix2, 0);
        }

        // 檢查fee
        if(isset($item_matrix[6]) && $item_matrix[6] != 0){
            array_push($item_matrix2, range_matrix_value_nolike($user_items->fee,$user_items2->fee));
        }else{
            array_push($item_matrix2, 0);
        }

        // 檢查direction
        if(isset($item_matrix[7]) && $item_matrix[7] != 0){
            array_push($item_matrix2, similar_matrix_value($user_items->direction,$user_items2->direction));
        }else{
            array_push($item_matrix2, 0);
        }

        // 檢查type
        if(isset($item_matrix[8]) && $item_matrix[8] != 0){
            array_push($item_matrix2, similar_matrix_value($user_items->type,$user_items2->type));
        }else{
            array_push($item_matrix2, 0);
        }

        // 檢查floor
        if(isset($item_matrix[9]) && $item_matrix[9] != 0){
            array_push($item_matrix2, similar_matrix_value($user_items->floor,$user_items2->floor));
        }else{
            array_push($item_matrix2, 0);
        }

        // 檢查age
        if(isset($item_matrix[10]) && $item_matrix[10] != 0){
            array_push($item_matrix2, range_matrix_value_nolike($user_items->age,$user_items2->age));
        }else{
            array_push($item_matrix2, 0);
        }

        // 檢查parking
        if(isset($item_matrix[11]) && $item_matrix[11] != 0){
            array_push($item_matrix2, similar_matrix_value($user_items->parking,$user_items2->parking));
        }else{
            array_push($item_matrix2, 0);
        }

        // 檢查ping
        if(isset($item_matrix[12]) && $item_matrix[12] != 0){
            array_push($item_matrix2, range_matrix_value_nolike($user_items->ping,$user_items2->ping));
        }else{
            array_push($item_matrix2, 0);
        }

        // 檢查room
        if(isset($item_matrix[13]) && $item_matrix[13] != 0){
            array_push($item_matrix2, similar_matrix_value($user_items->room,$user_items2->room));
        }else{
            array_push($item_matrix2, 0);
        }

        // 檢查area
        if(isset($item_matrix[14]) && $item_matrix[14] != 0){
            array_push($item_matrix2, similar_matrix_value($user_items->area,$user_items2->area));
        }else{
            array_push($item_matrix2, 0);
        }

// 儲存至資料庫(4:不喜歡的在意項目)
        $like_matrix_data   = array(
            'user_id'   => $user_id,
            'items'     => json_encode($item_matrix2),
            'is_like'   => 4,
        );

        $db->insert_table_data('ex_record_items_obj',$like_matrix_data);
        }
    }
}

// 若大於一半有相似的，回傳1，否則回傳0
function similar_matrix_value($val_arr,$compare=array()){
    $org_count  = round(count($val_arr) / 2);
    $return_val = 0;
    if(!empty($compare)){
        $val_arr=array_diff($val_arr,$compare);
    }

    $chk_count  = count(array_unique($val_arr));

    if(!empty($compare)){
        $return_val     = ($chk_count != 0 && $org_count >= $chk_count)?0:1;
    }else{
        $return_val     = ($chk_count != 0 && $org_count >= $chk_count)?1:0;
    }

    return $return_val;
}

function range_matrix_value($val_arr){
    $get_range  = get_range($val_arr);

    $avg    = (count($val_arr) != 0)?array_sum($val_arr) / count($val_arr):0;
    $avg    = round($avg, 3);

    $dev    = stats_standard_deviation($val_arr);

    $start_avg  = $get_range[0];
    $end_avg    = $get_range[1];

    $value_sum  = 0;
    foreach ($val_arr as $value) {
        $value_sum += ($start_avg != 0 && $end_avg != 0 && $start_avg <= $value && $value <= $end_avg)?1:0;
    }

    return (count($val_arr) != 0 && round(count($val_arr) / 2) <= $value_sum)?1:0;
}

function range_matrix_value_nolike($val_arr,$compare=array()){
    $return_val = 0;

    if(!empty($compare)){
        sort($val_arr);

        $mid        = (!empty($val_arr))?(int)floor(count($val_arr) / 2):0;
        $get_range  = get_range($val_arr);
        $start_avg  = $get_range[0];
        $end_avg    = $get_range[1];

        $value_sum  = 0;

        foreach ($compare as $key => $value) {
            if(!empty($get_range)){
                $value_sum += ($start_avg <= $value && $value <= $end_avg)?1:0;
            }
        }
        $return_val = ($value_sum < $mid)?1:0;
    }

    return $return_val;
}
// 取得陣列區間範圍
function get_range($arr){
    $start_avg  = (double)0;
    $end_avg    = (double)0;

    if(!empty($arr)){
        $avg    = array_sum($arr) / count($arr);
        $avg    = round($avg, 3);

        $dev    = stats_standard_deviation($arr);

        $start_avg  = (double)($avg - $dev);
        $end_avg    = (double)($avg + $dev);
    }

    $return_val = array($start_avg,$end_avg);

    return $return_val;
}
*/
?>
