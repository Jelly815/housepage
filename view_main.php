<?php
$main   = (isset($_GET['main']) && $_GET['main'] != '')?filter_var($_GET['main'], FILTER_SANITIZE_STRING):'';

$tpl->prepare ();

// 儲存搜尋紀錄
/*
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
*/

// 查詢開始
	$area_arr   = $type_arr = $around_arr = $direction_arr = array();
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
    $direction_all = $db->select_table_data('ex_direction','id,name');
    foreach ($direction_all as $key => $value) {
        $direction_arr[$value['id']] = $value['name'];
    }

    $select_arr = array();

    if($main != ''){
        $select_arr[] 	= array(0,'unid','=',$main);
    }

    $main_data  = $db->select_table_data('ex_main',
        array('unid','number','area','title','road','style','style','ping','around','age','floor','type','parking','unit','view_num','price','builder','community','direction','fee','description'),
        $select_arr,
        array('update_time' => 'DESC'));

    foreach ($main_data as $key => $value) {
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
        $house_img  = $db->select_table_data('ex_images','img_url',array(array(0,'number','=',$value['number'])),array(),1,3,1);

        $text['PAGE_TITLE'] = $value['title'];
        $tpl->assign(array(
        	'search_uuid' 	=> $value['unid'],
			'search_img1' 	=> (isset($house_img[0]['img_url']) && $house_img[0]['img_url'] != '')?$house_img[0]['img_url']:"img/EdPhoto.jpg",
            'search_img2'   => (isset($house_img[1]['img_url']) && $house_img[1]['img_url'] != '')?$house_img[1]['img_url']:"img/EdPhoto.jpg",
            'search_img3'   => (isset($house_img[2]['img_url']) && $house_img[2]['img_url'] != '')?$house_img[2]['img_url']:"img/EdPhoto.jpg",
			'search_title' 	=> $value['title'],
			'search_area' 	=> isset($area_arr[$value['area']])?$area_arr[$value['area']]:'',
			'search_type' 	=> isset($type_arr[$value['type']])?$type_arr[$value['type']]:'',
			'search_room' 	=> $style,
			'search_ping' 	=> $value['ping'].'坪',
			'search_view' 	=> $value['view_num'],
			'search_price' 	=> $value['price'].'萬元',
            'search_road'   => $value['road'],
            'search_age'    => $value['age'].'年',
            'search_floor'  => $value['floor'],
            'search_builder'=> ($value['builder'] != '')?$value['builder']:$value['community'],
            'search_arount' => ($value['parking'] == 1)?'有車位 | '.$arount_str:$arount_str,
            'search_direction' => isset($direction_all[$value['direction']])?$direction_all[$value['direction']]:'',
            'search_fee'    => $value['fee'].'元',
            'search_unit'   => $value['unit'].'萬/坪',
            'search_desc'   => $value['description']
		));
    }
?>
