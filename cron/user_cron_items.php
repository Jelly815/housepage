<?php
ini_set('display_errors', 1);
error_reporting(E_ALL);

session_start();
include_once(__DIR__.'/../lib/handling.php');
include_once(__DIR__.'/../lib/lang.php');

$db 	= new db_function();

#$get_user   = $db->get_table_value('`ex_user`','`unid`','','');

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

	$user_id	= $get_user_value['user_id'];

	$sql 	= 	"SELECT main.`area`,main.`road`,main.`room`,main.`ping`,main.`parking`,main.`age`,main.`floor`,".
                     	"main.`type`,main.`direction`,main.`fee`,main.`builder`,main.`unit`,main.`price`,".
                     	"main.`description`,main.`around`,main.`status`,main.`community` ".
				"FROM 	`ex_record_items` items,`ex_main` main ".
				"WHERE 	items.`main_id` = main.`id`AND ".
      					"items.`user_id` = ?";

    $sql    = $db->db->Prepare($sql);
    $main_res 	= $db->db->Execute($sql,array($user_id))->getArray();

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
    	if($main_value['description'] != '')array_push($items_arr['description'], $main_value['description']);
    	if($main_value['around'] != '')array_push($items_arr['around'], $main_value['around']);
    	array_push($items_arr['status'], $main_value['status']);
    	if($main_value['community'] != '')array_push($items_arr['community'], $main_value['community']);
    }echo '<pre>';print_r($items_arr);echo '</pre>';exit;


}
?>
