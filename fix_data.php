<?php
ini_set('display_errors', 1);
error_reporting(E_ALL);

session_start();
include_once(__DIR__.'/lib/handling.php');
include_once(__DIR__.'/lib/lang.php');

$db 	= new db_function();

#$str 	= array('房','廳','衛');

$main_data  = $db->select_table_data('ex_main',
        array('id','floor'),
        array(array(3,"floor LIKE '%整棟/%'")));
#echo "<pre>";print_r($main_data);echo "</pre>";exit;
foreach ($main_data as $key => $value) {
	$floor = explode('整棟/',$value['floor']);
    $floor = rtrim($floor[1],"F");

    $up_record_sql  = "UPDATE `ex_main` SET `floor` = ? WHERE `id`= ? ";
    $vals_arr   = array($floor,$value['id']);

    $result     = $db->update_data($up_record_sql,$vals_arr);
}
?>