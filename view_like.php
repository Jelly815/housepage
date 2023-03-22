<?php
$tpl->prepare ();

// 查詢開始
	$type_arr  = $around_arr = array();

    $like_data  = $db->select_table_data('ex_record_items',
        'main_id',
        array(array(0,'user_id','=',$_SESSION['uid']),
            array(0,'add_favorite','=',1)),
        array('last_time' => 'DESC'));
    $like_str   = '';
    foreach ($like_data as $value) {
        $like_str   .= $value['main_id'].',';
    }
    $like_str   = rtrim($like_str,',');

    $main_data  = $db->select_table_data('ex_main',
        array('unid','number','area','title','road','room','style','ping','around',
            'age','floor','type','parking','unit','view_num','price','builder','community'),
        array(array(3,'`id` IN ('.$like_str.')'),array(0,'is_closed','=',0)),
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
            'search_arount' => ($value['parking'] == 1)?'有車位 | '.$arount_str:$arount_str
		));
    }
?>
