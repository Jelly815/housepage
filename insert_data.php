<?php
//echo "<pre>";print_r(md5(uniqid(rand())));echo "</pre>";exit;
include_once('./lib/handling.php');

$db 	= new db_function();

// Add User
/*
	$add_user_sql =
		"INSERT INTO `ex_user` (`unid`,`name`,`email`,`pwd`,`age`,`area_id`,`add_date`,`login_time`) values (?,?,?,?,?,?,?,?)";
	$add_user_arr = array(
		//array('m'.md5(uniqid(rand())),'張小姐','jellyandjar@yahoo.com.tw',md5('789456123'),'35',282,date('Y-m-d H:i:s'),date('Y-m-d H:i:s')),
		//array('m'.md5(uniqid(rand())),'郭先生','jellyandjar@yahoo.com.tw',md5('789456123'),'25',304,date('Y-m-d H:i:s'),date('Y-m-d H:i:s')),
		//array('m'.md5(uniqid(rand())),'劉先生','jellyandjar@yahoo.com.tw',md5('789456123'),'35',304,date('Y-m-d H:i:s'),date('Y-m-d H:i:s')),
		//array('m'.md5(uniqid(rand())),'陳先生','jellyandjar@yahoo.com.tw',md5('789456123'),'30',282,date('Y-m-d H:i:s'),date('Y-m-d H:i:s')),
		//array('m'.md5(uniqid(rand())),'潘先生','jellyandjar@yahoo.com.tw',md5('789456123'),'25',276,date('Y-m-d H:i:s'),date('Y-m-d H:i:s')),
		//array('m'.md5(uniqid(rand())),'張小姐','jellyandjar@yahoo.com.tw',md5('789456123'),'30',284,date('Y-m-d H:i:s'),date('Y-m-d H:i:s')),
		//array('m'.md5(uniqid(rand())),'鍾先生','jellyandjar@yahoo.com.tw',md5('789456123'),'30',304,date('Y-m-d H:i:s'),date('Y-m-d H:i:s')),
		//array('m'.md5(uniqid(rand())),'黃先生','jellyandjar@yahoo.com.tw',md5('789456123'),'35',251,date('Y-m-d H:i:s'),date('Y-m-d H:i:s')),
		array('m'.md5(uniqid(rand())),'蕭先生','jellyandjar@yahoo.com.tw',md5('789456123'),'25',304,date('Y-m-d H:i:s'),date('Y-m-d H:i:s')),
	);
	foreach ($add_user_arr as $user_key => $user_value) {
		$unid 		= filter_var($user_value[0], FILTER_SANITIZE_STRING);
		$name 		= filter_var($user_value[1], FILTER_SANITIZE_STRING);
		$email 		= filter_var($user_value[2], FILTER_VALIDATE_EMAIL);
		$pwd 		= filter_var($user_value[3], FILTER_SANITIZE_STRING);
		$age 		= intval($user_value[4]);
		$area_id	= intval($user_value[5]);
		$add_date	= $user_value[6];
		$login_time	= $user_value[7];

		// Add User
		$user_vals  = array($unid,$name,$email,$pwd,$age,$area_id,$add_date,$login_time);
		$user_id 	= $db->insert_data($add_user_sql,$user_vals);
	}
*/
// ex_record
/*
	$add_record_sql =
		"INSERT INTO `ex_record` (`user_unid`,`area`,`price`,`ping`,`style`,`type`,`times`)  values (?,?,?,?,?,?,?) ";

	$up_record_sql 	=
		"UPDATE `ex_record` SET `times` = `times` + 1 WHERE `user_id`= ? AND `area` = ? AND `price` = ? AND `ping` = ? AND `style` = ? AND `type` = ? ";

	$add_record_arr = array(
		'm185ccab81019a39cba16f666f070bb83' => array(
				array(275,283,304,286,284,280,278,282,285,276,277,279), // 區域
				array(20,30,40), 	// 坪數
				array(300,600), 	// 金額
				array(3), 			// 類型
				array(2,3), 		// 房數
		),
		'm1b414f0be20777c30e0423f441b09db8' => array(
				array(275,304,282,285), 		// 區域
				array(30,40), 		// 坪數
				array(600), 		// 金額
				array(3), 			// 類型
				array(2,3), 		// 房數
		),
		'm8456fba48ba8c14bdd683e92c7414dc8' => array(
				array(275,304), 	// 區域
				array(51), 			// 坪數
				array(1000), 		// 金額
				array(3,4), 		// 類型
				array(4,5), 		// 房數
		),
		'mc741ce94208d215dc1a80e40c5456cf1' => array(
				array(275,287,283,286,304), 	// 區域
				array(40), 			// 坪數
				array(600,1000), 	// 金額
				array(3), 			// 類型
				array(3,4), 		// 房數
		),
		'mf82803bf01099c75ac76e774d685b2dc' => array(
				array(275,276,278,283,277), 	// 區域
				array(30,40), 		// 坪數
				array(1000), 		// 金額
				array(3), 			// 類型
				array(2,3,4), 		// 房數
		),
		'm9e3954249a75ceccc925c5b11a9ab97' => array(
				array(275,284,299), // 區域
				array(40), 			// 坪數
				array(600,1000), 	// 金額
				array(3), 			// 類型
				array(3), 			// 房數
		),
		'm9e3954249a75ceccc925c5b11a9ab97' => array(
				array(275,284,299), // 區域
				array(40), 			// 坪數
				array(600,1000), 	// 金額
				array(3), 			// 類型
				array(3), 			// 房數
		),
		'm199cdc39ee6e65811960a187ccf1fcb9' => array(
				array(275,304,310,278), 		// 區域
				array(30,40), 		// 坪數
				array(600,1500), 	// 金額
				array(1,3,4), 		// 類型
				array(3), 			// 房數
		),
		'm50fc03640e41b3fb483812dab6a8ee7e' => array(
				array(237,245,251), 		// 區域
				array(50,51), 		// 坪數
				array(1000), 		// 金額
				array(4), 			// 類型
				array(34), 			// 房數
		),
		'm6dcd3e8e87edfa412028750da8c315b2' => array(
				array(275,304), 				// 區域
				array(30,40), 		// 坪數
				array(1000), 		// 金額
				array(3), 			// 類型
				array(2,3), 		// 房數
		),
	);

	foreach ($add_record_arr as $record_key => $record_value) {
		$user_unid 	= $record_key;

		foreach ($record_value[0] as $area_key => $area_value) {
			foreach ($record_value[1] as $ping_key => $ping_value) {
				foreach ($record_value[2] as $money_key => $money_value) {
					foreach ($record_value[3] as $type_key => $type_value) {
						foreach ($record_value[4] as $style_key => $style_value) {
							// 檢查是否有紀錄
							$get_record 	= $db->get_table_value('ex_record','id',
							"`user_unid`= '{$user_unid}' AND `area` = '{$area_value}' AND ".
							"`price` = '{$money_value}' AND `ping` = '{$ping_value}' AND ".
							"`style` = '{$style_value}' AND `type` = '{$type_value}' ");

							if(!empty($get_record)){
								$vals_arr 	= array($user_unid,$area_value,$money_value,$ping_value,$style_value,$type_value);

								$result 	= $db->update_data($up_record_sql,$vals_arr);
							}else{
								$vals_arr 	= array($user_unid,$area_value,$money_value,$ping_value,$style_value,$type_value,1);
								$result 	= $db->insert_data($add_record_sql,$vals_arr);
							}
						}
					}
				}
			}
		}
	}
*/


// ex_record_items

// ex_record_items_stay



// ex_record

// ex_record_items

// ex_record_items_stay



/*
$user_arr = array(
	array(2,3,1),
	array(2,3,1),
	array(2,3,2),
	array(2,3,3),
);

foreach ($user_arr as $user_key => $user_value) {
	$user_id 	= intval($user_value[0]);
	$record_id 	= intval($user_value[1]);
	$main_id 	= intval($user_value[2]);

	$get_record = $db->get_table_value('ex_record_items','id',
	"`user_id`= '{$user_id}' AND `record_id` = '{$record_id}' AND ".
	"`main_id` = '{$main_id}' ");

	if(!empty($get_record)){
		$record_items_id = $get_record[0]['id'];

		$sql 	=
			' UPDATE `ex_record_items` '.
			' SET `times` = `times` + 1 '.
			" WHERE `id`= ? ";

		$sql 	= $db->db->prepare($sql);
		$result = $db->db->execute($sql,array($record_items_id));
	}else{
		$sql 	= 'INSERT INTO `ex_record_items` '.
				' (user_id,record_id,main_id,times)'.
				' values (?,?,?,?)';
		$vals_arr = array($user_id,$record_id,$main_id,1);
		if($db->insert_data($sql,$vals_arr)){
			$record_items_id = $this->db->Insert_ID();
		}

	}

	if($record_items_id > 0){
		$sql 	= 'INSERT INTO `ex_record_items_stay` '.
		' (record_items_id,stay_time)'.
		' values (?,?)';
		$vals_arr = array($record_items_id,20);
		$db->insert_data($sql,$vals_arr);
	}
}*/
?>