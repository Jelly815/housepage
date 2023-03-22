<?php
    session_start();
	include_once('./lib/handling.php');
	include_once('./lib/lang.php');
	$db 	= new db_function();
	$tpl  	= new  TemplatePower(THEMES.'search_results.tpl');
	$tpl->prepare();

    // 呼叫推薦引擎
        if(isset($_SESSION['uid']) && $_SESSION['uid'] != ''){
            $params = $_SESSION['uid'];
        }else{
            $params = $_SESSION['uid'] = CUSTOMERID;
        }

        $command    = escapeshellcmd(PYTHONPATH.'.py '.$params);
        $output     = shell_exec($command);
        $output     = str_replace(']','',str_replace('[', '', $output));
        $output     = explode(',', $output);

        $main_str   = '';
        foreach ($output as $key => $value) {
            $main_str .= trim($value).',';
        }

        $area_all   = $db->select_table_data('ex_area','id,name',array(array(0,'city_id','=',275)));
        foreach ($area_all as $key => $value) {
            $area_arr[$value['id']] = $value['name'];
        }
        $type_all   = $db->select_table_data('ex_type','id,name');
        foreach ($type_all as $key => $value) {
            $type_arr[$value['id']] = $value['name'];
        }

        $main_data  = $db->select_table_data('ex_main',
            array('id','unid','number','area','title','road','room','style','ping',
                'age','floor','type','parking','unit','view_num','price'),
            array(array(2,'id','IN ('.rtrim($main_str,',').')','')),
            array('update_time' => 'DESC'));

        foreach ($main_data as $key => $value) {
        	$tpl->newBlock('search_row');

            $house_img  = $db->select_table_data('ex_images','img_url',array(array(0,'number','=',$value['number'])),array(),2);
            $tpl->assign(array(
            	'search_uuid' 	=> $value['unid'],
				'search_img' 	=> ($house_img != '')?$house_img:"img/EdPhoto.jpg",
				'search_title' 	=> $value['title'],
				'search_area' 	=> isset($area_arr[$value['area']])?$area_arr[$value['area']]:'',
				'search_type' 	=> isset($type_arr[$value['type']])?$type_arr[$value['type']]:'',
				'search_room' 	=> $value['room'].'房',
				'search_ping' 	=> $value['ping'].'坪',
				'search_view' 	=> $value['view_num'].'人瀏覽',
				'search_price' 	=> $value['price'].'萬元',
                'search_click'  => 'onclick="click_recommend(\''.$params.'\',\''.$value['id'].'\',\'like\')"',
                'search_page'   => '&page=like'
			));
        }

    $tpl->printToScreen();
?>