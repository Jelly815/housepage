<?php
ini_set('display_errors', 1);
error_reporting(E_ALL);

session_start();
include_once(__DIR__.'/lib/handling.php');
include_once(__DIR__.'/lib/lang.php');

$db 	= new db_function();

#$str 	= array('房','廳','衛');

$main_data  = $db->select_table_data('ex_main',
        array('id','style'),
        array(array(3,"direction = ''")));
#echo "<pre>";print_r($main_data);echo "</pre>";exit;
foreach ($main_data as $key => $value) {
	#foreach ($str as $str_val) {
		#$value['style'] = str_replace($str_val,";",$value['style']);
		$value['direction'] = rand(1, 8);
	#}
	#$up_record_sql  = "UPDATE `ex_main` SET `style` = ? WHERE `id`= ? ";
    #$vals_arr   = array($value['style'],$value['id']);
    $up_record_sql  = "UPDATE `ex_main` SET `direction` = ? WHERE `id`= ? ";
    $vals_arr   = array($value['direction'],$value['id']);

    $result     = $db->update_data($up_record_sql,$vals_arr);
}
?>