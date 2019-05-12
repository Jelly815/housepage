<?php
	session_start();
	include_once('./lib/handling.php');
	include_once('./lib/lang.php');
	$db 	= new db_function();
	$tpl  	= new  TemplatePower(THEMES.'search_results.tpl');
	$tpl->prepare();
    $area   = isset($_POST['area'])?explode(',', filter_var($_POST['area'], FILTER_SANITIZE_STRING)):array();
    $price  = isset($_POST['price'])?explode(',', filter_var($_POST['price'], FILTER_SANITIZE_STRING)):array();
    $type   = isset($_POST['type'])?explode(',', filter_var($_POST['type'], FILTER_SANITIZE_STRING)):array();
    $room   = isset($_POST['room'])?explode(',', filter_var($_POST['room'], FILTER_SANITIZE_STRING)):array();
    $ping   = isset($_POST['ping'])?explode(',', filter_var($_POST['ping'], FILTER_SANITIZE_STRING)):array();

    // 區域
    	$area_arr   = array();
        $area_str   = '';
        $area_all   = $db->select_table_data('ex_area','id,name',array(array(0,'city_id','=',275)));
        foreach ($area_all as $key => $value) {
        	$area_arr[$value['id']] = $value['name'];
        }
        foreach ($area as $key => $value) {
        	if(in_array($value,$area_arr)){
        		$flip = array_flip($area_arr);
        		$area_str  .= $flip[$value].",";
        	}
        }
    // 金額
        $price_str   = '';
        $min = $small = $large = $max = 0;
        $price_arr   = array();
        foreach ($price as $key => $value) {
            $var_strpos = strpos($value,"萬以上");

            if($var_strpos){
                $value = str_replace("萬以上", '', $value);
                $max   = $value;
                $price_arr[] = 2001;
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
                    $price_arr[] = $val_arr[1];
                }else{
                    $min   = $val_arr[0];
                    $price_arr[] = $val_arr[0];
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
        $type_arr 	= array();
        $type_str   = '';
        $type_all   = $db->select_table_data('ex_type','id,name');
        foreach ($type_all as $key => $value) {
        	$type_arr[$value['id']] = $value['name'];
        }
        foreach ($type as $key => $value) {
        	if(in_array($value,$type_arr)){
        		$flip = array_flip($type_arr);
        		$type_str  .= $flip[$value].",";
        	}
        }
    // 房數
        $room_str   = '';
        $max        = 0;
        $room_arr   = array();
        foreach ($room as $key => $value) {
            $var_strpos = strpos($value,"及以上");

            if($var_strpos){
                $value = str_replace("房及以上", '', $value);
                $max   = $value;
                $room_arr[] = $value;
            }elseif($value != ''){
                $value = str_replace("房", '', $value);
                $room_str .= $value.',';
                $room_arr[] = $value;
            }
        }

        $room_str = ($max != '')?"`room` IN (".rtrim($room_str,',').") OR `room` >= $max ":(($room_str != '')?"`room` IN (".rtrim($room_str,',').") ":'');
    // 坪數
        $ping_str   = '';
        $min = $small = $large = $max = 0;
        $ping_arr   = array();
        foreach ($ping as $key => $value) {
            $var_strpos = strpos($value,"坪及以上");

            if($var_strpos){
                $value = str_replace("坪及以上", '', $value);
                $max   = $value;
                $ping_arr[] = 51;
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
                    $ping_arr[] = $val_arr[1];
                }else{
                    $min   = $val_arr[0];
                    $ping_arr[] = $val_arr[0];
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
                'age','floor','type','parking','unit','view_num','price'),
            $select_arr,
            array('update_time' => 'DESC'),
            1,4,1);
        foreach ($main_data as $key => $value) {
        	$tpl->newBlock('search_row');

            $house_img  = $db->select_table_data('ex_images','img_url',array(array(0,'number','=',$value['number'])),array(),2);
            $tpl->assign(array(
            	'search_uuid' 	=> $value['unid'],
				'search_img' 	=> ($house_img != '')?$house_img:"img/EdPhoto.jpg",
				'search_title' 	=> $value['title'],
				'search_area' 	=> $area_arr[$value['area']],
				'search_type' 	=> $type_arr[$value['type']],
				'search_room' 	=> $value['room'].'房',
				'search_ping' 	=> $value['ping'].'坪',
				'search_view' 	=> $value['view_num'].'人瀏覽',
				'search_price' 	=> $value['price'].'萬元'
			));
        }

$add_record_arr = array(
            $_SESSION['uid'] => array(
                    explode(',', rtrim($area_str,',')), // 區域
                    $ping_arr,  // 坪數
                    $price_arr,     // 金額
                    explode(',', rtrim($type_str,',')), // 類型
                    $room_arr,      // 房數
            ),
        );

    // 儲存搜尋紀錄
        /*
        $add_record_sql =
		"INSERT INTO `ex_record` (`user_unid`,`area`,`price`,`ping`,`style`,`type`,`times`)  values (?,?,?,?,?,?,?) ";

		$up_record_sql 	=
			"UPDATE `ex_record` SET `times` = `times` + 1 WHERE `user_id`= ? AND `area` = ? AND `price` = ? AND `ping` = ? AND `style` = ? AND `type` = ? ";

		$add_record_arr = array(
			$_SESSION['uid'] => array(
					explode(',', rtrim($area_str,',')), // 區域
					$ping_arr, 	// 坪數
					$price_arr, 	// 金額
					explode(',', rtrim($type_str,',')), // 類型
					$room_arr, 		// 房數
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
    $tpl->gotoBlock( "_ROOT" );
    $tpl->assign("url","index.php?op=search_view&area=".rtrim($area_str,',')."&ping=".implode(',', $ping_arr)."&price=".implode(',', $price_arr)."&type=".rtrim($type_str,',')."&roon=".implode(',', $room_arr));
    $tpl->printToScreen();
?>