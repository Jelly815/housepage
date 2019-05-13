<?php
$area   = (isset($_GET['area']) && $_GET['area'] != '')?filter_var($_GET['area'], FILTER_SANITIZE_STRING):'';
$price  = (isset($_GET['price']) && $_GET['price'] != '')?explode(',', filter_var($_GET['price'], FILTER_SANITIZE_STRING)):array();
$type   = (isset($_GET['type']) && $_GET['type'] != '')?filter_var($_GET['type'], FILTER_SANITIZE_STRING):'';
$room   = (isset($_GET['room']) && $_GET['room'] != '')?explode(',', filter_var($_GET['room'], FILTER_SANITIZE_STRING)):array();
$ping   = (isset($_GET['ping']) && $_GET['ping'] != '')?explode(',', filter_var($_GET['ping'], FILTER_SANITIZE_STRING)):array();

$tpl->prepare ();

// 儲存搜尋紀錄
    $add_record_sql =
	"INSERT INTO `ex_record` (`user_id`,`area`,`price`,`ping`,`style`,`type`,`times`)  values (?,?,?,?,?,?,?) ";

	$up_record_sql 	=
		"UPDATE `ex_record` SET `times` = `times` + 1 WHERE `user_id`= ? AND `area` = ? AND `price` = ? AND `ping` = ? AND `style` = ? AND `type` = ? ";

	$add_record_arr = array(
        $_SESSION['uid'] => array(
                explode(',', $area), 	// 區域
                $ping,  // 坪數
                $price, // 金額
                explode(',', $type), 	// 類型
                $room, 	// 房數
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
							"`user_id`= '{$user_unid}' AND `area` = '{$area_value}' AND ".
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


// 查詢開始
	$area_arr   = $type_arr = $around_arr = array();
	$area_all   = $db->select_table_data('ex_area','id,name',array(array(0,'city_id','=',275)));
    foreach ($area_all as $key => $value) {
    	$area_arr[$value['id']] = $value['name'];
    }
    $type_all   = $db->select_table_data('ex_type','id,name');
    foreach ($type_all as $key => $value) {
    	$type_arr[$value['id']] = $value['name'];
    }
    $around_all = $db->select_table_data('ex_around','id,name');
    foreach ($around_all as $key => $value) {
        $around_arr[$value['id']] = $value['name'];
    }

    $select_arr = array();
    // 區域
    if($area != ''){
        $select_arr[] 	= array(2,'area','IN ('.rtrim($area,',').')','');
    }
    // 金額
    if(!empty($price)){
    	$val_arr = array(
    		'300' => array(300),
			'600' => array(300,600),
			'1000' => array(600,1000),
			'1500' => array(1000,1500),
			'2000' => array(1500,2000),
			'2001' => array(2001));
    	$min 	= $small = $large = $max = 0;
    	foreach ($price as $key => $value) {
            if(count($val_arr[$value]) == 2){
                if($small != 0){
                    $small = ($val_arr[$value][0] < $small)?$val_arr[$value][0]:$small;
                }else{
                    $small = $val_arr[$value][0];
                }

                if($large != 0){
                    $large = ($val_arr[$value][1] > $large)?$val_arr[$value][1]:$large;
                }else{
                    $large = $val_arr[$value][1];
                }
            }elseif($value == 300){
                $min   = $val_arr[$value][0];
            }elseif($value == 2001){
                $max   = $val_arr[$value][0];
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

        $select_arr[] = array(3,$price_str);
    }
    // 類型
    if($type != ''){
        $select_arr[] 	= array(2,'type','IN ('.rtrim($type,',').')','');
    }
    // 房數
    if(!empty($room)){
    	$max 	= 0;
    	$room_str 		= '';
    	foreach ($room as $key => $value) {
            if($value == 5){
                $max   	= $value;
            }elseif($value != ''){
                $room_str .= $value.',';
            }
        }

        $room_str = ($max != '')?"`room` IN (".rtrim($room_str,',').") OR `room` >= $max ":(($room_str != '')?"`room` IN (".rtrim($room_str,',').") ":'');

        $select_arr[] = array(3,$room_str);
    }
    // 坪數
    if(!empty($ping)){
    	$val_arr = array(
    		'20' => array(20),
			'30' => array(20,30),
			'40' => array(30,40),
			'50' => array(40,50),
			'51' => array(51));
    	$min = $small = $large = $max = 0;
    	foreach ($ping as $key => $value) {
            if(count($val_arr[$value]) == 2){
                if($small != 0){
                    $small = ($val_arr[$value][0] < $small)?$val_arr[$value][0]:$small;
                }else{
                    $small = $val_arr[$value][0];
                }

                if($large != 0){
                    $large = ($val_arr[$value][1] > $large)?$val_arr[$value][1]:$large;
                }else{
                    $large = $val_arr[$value][1];
                }
            }elseif($value == 300){
                $min   = $val_arr[$value][0];
            }elseif($value == 2001){
                $max   = $val_arr[$value][0];
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
        $select_arr[] = array(3,$ping_str);
    }

    $main_data  = $db->select_table_data('ex_main',
        array('unid','number','area','title','road','style','style','ping','around',
            'age','floor','type','parking','unit','view_num','price','builder','community'),
        $select_arr,
        array('update_time' => 'DESC'));

    foreach ($main_data as $key => $value) {
    	$tpl->newBlock('view_search');
        // 房間
        $room1 = $room2 = $room3 = $room4 = '';
        if(strchr($value['style'],';')){
            $style = ($value['style'] != '')?explode(';',$value['style']):array();
        }else{
            $style = ($value['style'] != '')?explode(':',$value['style']):array();
        }


        if(count($style) == 1){
            list($room1)  = $style;
        }elseif(count($style) == 2){
            list($room1,$room2)  = $style;
        }elseif(count($style) == 3){
            list($room1,$room2,$room3)  = $style;
        }elseif(count($style) == 4){
            list($room1,$room2,$room3,$room4)  = $style;
        }

        $style = ($room1 != '')?$room1.'房':'';
        $style .= ($room2 != '')?$room2.'廳':'';
        $style .= ($room3 != '')?$room3.'衛':'';
        $style .= ($room4 != '')?$room4.'陽台':'';

        // 生活機能
        $arount_str = '';
        $around     = ($value['around'] != '')?explode(';',$value['around']):array();

        foreach ($around as $a_key => $a_value) {
            if(isset($around_arr[$a_value])){
                $arount_str .= $around_arr[$a_value].' | ';
            }
        }
        $house_img  = $db->select_table_data('ex_images','img_url',array(array(0,'number','=',$value['number'])),array(),2);
        $tpl->assign(array(
        	'search_uuid' 	=> $value['unid'],
			'search_img' 	=> ($house_img != '')?$house_img:"img/EdPhoto.jpg",
			'search_title' 	=> $value['title'],
			'search_area' 	=> isset($area_arr[$value['area']])?$area_arr[$value['area']]:'',
			'search_type' 	=> isset($type_arr[$value['type']])?$type_arr[$value['type']]:'',
			'search_room' 	=> $style,
			'search_ping' 	=> $value['ping'].'坪',
			'search_view' 	=> $value['view_num'].' 人瀏覽',
			'search_price' 	=> $value['price'].'萬元',
            'search_road'   => $value['road'],
            'search_age'    => $value['age'].'年',
            'search_floor'  => $value['floor'],
            'search_builder'=> ($value['builder'] != '')?$value['builder']:$value['community'],
            'search_arount' => $arount_str
		));
    }
?>
