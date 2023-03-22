<?php
$tpl->prepare ();

$tpl->assign("survey_title",TITLESURVEY);

// 是否為會員
$is_member = (isset($_SESSION['uid']) && substr($_SESSION['uid'],0,1) == 'm')?1:0;

$survey_data    = $db->select_table_data('ex_survey',
    array('id','title','f_id','sort'),
    array(),
    array('f_id' => 'ASC','sort' => 'ASC'));
$list_num   = 1;
$num        = 0;
foreach ($survey_data as $key => $value) {
    $tpl->newBlock('view_list');
    $html       = $top_title = '';

    if($value['f_id'] > $num && $value['f_id'] == 1){
        $num    = $value['f_id'];
        $top_title  = '<li>
                            <p>
                                <label style="width: 460px;font-weight:bold;">熱門/最新 搜尋</label>
                            </p>
                        </li>';
    }elseif($value['f_id'] > $num && $value['f_id'] == 2){
        $num    = $value['f_id'];
        $top_title  = '<li>
                            <p>
                                <label style="width: 460px;font-weight:bold;">別人喜歡的</label>
                            </p>
                        </li>';
    }elseif($value['f_id'] > $num && $value['f_id'] == 3){
        $num    = $value['f_id'];
        $top_title  = '<li>
                            <p>
                                <label style="width: 460px;font-weight:bold;">您喜歡的內容</label>
                            </p>
                        </li>';
    }elseif($value['f_id'] > $num && $value['f_id'] == 4){
        $num    = $value['f_id'];
        $top_title  = '<li>
                            <p>
                                <label style="width: 460px;font-weight:bold;">依據您不喜歡的預測喜歡的</label>
                            </p>
                        </li>';
    }
    elseif($value['f_id'] > $num && $value['f_id'] == 5){
        $num    = $value['f_id'];
        $top_title  = '<li>
                            <p>
                                <label style="width: 460px;font-weight:bold;">推薦系統</label>
                            </p>
                        </li>';
    }

    if($value['f_id'] == 6){
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
    }elseif($value['f_id'] == 7){
        $html   = '<textarea rows="4" cols="40" name="ans_'.$value['id'].'"></textarea>';
    }else{
        $html   = '<input type="radio" name="ans_'.$value['id'].'" value="1">
                    <label for="1" style="width:50px;">是</label>
                    <input type="radio" name="ans_'.$value['id'].'" value="0">
                    <label for="0" style="width:50px;">否</label>';
    }

    $tpl->assign(array(
        'list_num'  => $list_num,
    	'title' 	=> $value['title'],
        'html'      => $html,
        'top_title' => $top_title

	));
    $list_num++;
}

$tpl->gotoBlock("_ROOT");
?>
