<?php
$main   = (isset($_GET['main']) && $_GET['main'] != '')?filter_var($_GET['main'], FILTER_SANITIZE_STRING):'';
$main_id = 0;
$tpl->prepare ();
echo '<pre>';print_r($_SESSION['uid']);echo '</pre>';
// 查詢開始
    $type_arr = $around_arr = $direction_arr =
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
        array('id','unid','number','area','title','road','style','style','ping','around','age','floor','type','parking','unit','view_num','price','builder','community','direction','fee','description','room'),
        $select_arr,
        array('update_time' => 'DESC'));

    foreach ($main_data as $key => $value) {
        $main_id    = $value['id'];
        // 房間
        $room1 = $room2 = $room3 = $room4 = '';
        if(strchr($value['style'],';')){
            $style  = ($value['style'] != '')?explode(';',$value['style']):array();
        }else{
            $style  = ($value['style'] != '')?explode(':',$value['style']):array();
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
        $house_img  = $db->select_table_data('ex_images','img_url',array(array(0,'number','=',$value['number'])),array());

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
            'search_direction' => isset($direction_arr[$value['direction']])?$direction_arr[$value['direction']]:'',
            'search_fee'    => $value['fee'].'元',
            'search_unit'   => $value['unit'].'萬/坪',
            'search_desc'   => $value['description']
		));

        // other img
        $img_count = count($house_img)-1;
        for ($i = 3; $i <= $img_count; $i++) {
            $tpl->newBlock('view_img');
            $tpl->assign(array(
                'search_img'   => (isset($house_img[$i]['img_url']) && $house_img[$i]['img_url'] != '')?$house_img[$i]['img_url']:"img/EdPhoto.jpg",
                'search_title'  => $value['title']
            ));
        }

        // 儲存搜尋紀錄
        if(isset($value['area']) && $value['area'] != '' &&
            isset($value['ping']) && $value['ping'] != '' &&
            isset($value['price']) && $value['price'] != '' &&
            isset($value['type']) && $value['type'] != '' &&
            isset($value['room']) && $value['room'] != '' &&
            isset($_SESSION['uid'])
        ){
            $add_record_sql =
            "INSERT INTO `ex_record` (`user_id`,`area`,`price`,`ping`,`style`,`type`,`times`)  values (?,?,?,?,?,?,?) ";

            $up_record_sql  =
                "UPDATE `ex_record` SET `times` = `times` + 1 WHERE `user_id`= ? AND `area` = ? AND `price` = ? AND `ping` = ? AND `style` = ? AND `type` = ? ";

            // 坪數
            if($value['ping'] <= 20){
                $ping = 20;
            }elseif($value['ping'] > 20 && $value['ping'] <= 30){
                $ping = 30;
            }elseif($value['ping'] > 30 && $value['ping'] <= 40){
                $ping = 40;
            }elseif($value['ping'] > 40 && $value['ping'] <= 50){
                $ping = 50;
            }elseif($value['ping'] > 50){
                $ping = 51;
            }
            // 金額
            if($value['price'] <= 300){
                $price = 300;
            }elseif($value['price'] > 300 && $value['price'] <= 600){
                $price = 600;
            }elseif($value['price'] > 600 && $value['price'] <= 1000){
                $price = 1000;
            }elseif($value['price'] > 1000 && $value['price'] <= 1500){
                $price = 1500;
            }elseif($value['price'] > 1500 && $value['price'] <= 2000){
                $price = 2000;
            }elseif($value['price'] > 2000){
                $price = 2001;
            }

            $add_record_arr = array(
                $_SESSION['uid'] => array(
                        array($value['area']),  // 區域
                        array($ping),           // 坪數
                        array($price),          // 金額
                        array($value['type']),  // 類型
                        array($value['room']),  // 房數
                ),
            );

            foreach ($add_record_arr as $record_key => $record_value) {
                $user_unid  = $record_key;

                foreach ($record_value[0] as $area_key => $area_value) {
                    foreach ($record_value[1] as $ping_key => $ping_value) {
                        foreach ($record_value[2] as $money_key => $money_value) {
                            foreach ($record_value[3] as $type_key => $type_value) {
                                foreach ($record_value[4] as $style_key => $style_value) {
                                    // 檢查是否有紀錄
                                    $get_record     = $db->get_table_value('ex_record','id',
                                    "`user_id`= '{$user_unid}' AND `area` = '{$area_value}' AND ".
                                    "`price` = '{$money_value}' AND `ping` = '{$ping_value}' AND ".
                                    "`style` = '{$style_value}' AND `type` = '{$type_value}' ");

                                    if(!empty($get_record)){
                                        $vals_arr   = array($user_unid,$area_value,$money_value,$ping_value,$style_value,$type_value);

                                        $result     = $db->update_data($up_record_sql,$vals_arr);

                                        // 檢查是否有item紀錄
                                        $get_record2= $db->get_table_value('ex_record_items','id',
                                        "`user_id`= '".$user_unid."' AND `record_id` = '".$get_record[0]['id']."' AND `main_id` = '".$main_id."' ");
                                        if(!empty($get_record2)){
                                            // 更新item
                                            $up_record_sql  = "UPDATE `ex_record_items` SET `times` = `times` + 1 WHERE `user_id`= ? AND `record_id` = ? AND `main_id` = ? ";
                                            $vals_arr   = array($user_unid,$get_record[0]['id'],$main_id);

                                            $result     = $db->update_data($up_record_sql,$vals_arr);
                                        }else{
                                            // 儲存item
                                            $add_record_sql = "INSERT INTO `ex_record_items` (`user_id`,`record_id`,`main_id`,`times`,`click_map`,`add_favorite`)  values (?,?,?,?,?,?) ";
                                            $vals_arr   = array($user_unid,$result,$main_id,1,0,0);

                                            $result     = $db->insert_data($add_record_sql,$vals_arr);
                                        }
                                    }else{
                                        $vals_arr   = array($user_unid,$area_value,$money_value,$ping_value,$style_value,$type_value,1);
                                        $result     = $db->insert_data($add_record_sql,$vals_arr);
                                        $last_id    = $db->db->execute("SELECT LAST_INSERT_ID() FROM `ex_record`");

                                        // 儲存item
                                        $add_record_sql = "INSERT INTO `ex_record_items` (`user_id`,`record_id`,`main_id`,`times`,`click_map`,`add_favorite`)  values (?,?,?,?,?,?) ";
                                        $vals_arr   = array($user_unid,$last_id->fields[0],$main_id,1,0,0);

                                        $result     = $db->insert_data($add_record_sql,$vals_arr);
                                    }

                                    // 更新house
                                    $up_record_sql  = "UPDATE `ex_main` SET `view_num` = `view_num` + 1 WHERE `id`= ? ";
                                    $vals_arr   = array($main_id);

                                    $result     = $db->update_data($up_record_sql,$vals_arr);
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    $tpl->gotoBlock("_ROOT");
    $tpl->assign(array('main_id'=>$main_id));
?>
