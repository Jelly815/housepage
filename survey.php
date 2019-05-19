<?php
$tpl->prepare ();

$tpl->assign("survey_title",TITLESURVEY);

// 是否為會員
$is_member = (isset($_SESSION['uid']) && substr($_SESSION['uid'],0,1) == 'm')?1:0;

$survey_data  = $db->select_table_data('ex_survey',
    array('id','title','f_id','sort'),
    array(),
    array('sort' => 'ASC'));
$list_num = 1;
foreach ($survey_data as $key => $value) {
    if($is_member != 1 && $value['f_id'] == 1){
        continue;
    }
    $tpl->newBlock('view_list');
    $html       = '';

    if($value['f_id'] == 2){
        $html   = '<input type="radio" name="ans_'.$value['id'].'" value="1">
                    <label for="1" style="width:10px;">1</label>
                    <input type="radio" name="ans_'.$value['id'].'" value="2">
                    <label for="0" style="width:10px;">2</label>
                    <input type="radio" name="ans_'.$value['id'].'" value="3">
                    <label for="0" style="width:10px;">3</label>
                    <input type="radio" name="ans_'.$value['id'].'" value="4">
                    <label for="0" style="width:10px;">4</label>
                    <input type="radio" name="ans_'.$value['id'].'" value="5">
                    <label for="0" style="width:10px;">5</label>';
    }elseif($value['f_id'] == 3){
        $html   = '<textarea rows="4" cols="40" name="ans_'.$value['id'].'"></textarea>';
    }elseif($value['f_id'] == 0 || $value['f_id'] == 1){
        $html   = '<input type="radio" name="ans_'.$value['id'].'" value="1">
                    <label for="1" style="width:50px;">是</label>
                    <input type="radio" name="ans_'.$value['id'].'" value="0">
                    <label for="0" style="width:50px;">否</label>';
    }

    $tpl->assign(array(
        'list_num'  => $list_num,
    	'title' 	=> $value['title'],
        'html'     => $html,
	));
    $list_num++;
}

$tpl->gotoBlock("_ROOT");
?>
