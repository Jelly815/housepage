<?php
	include_once('./lib/handling.php');
	if( isset( $_POST['start'] ) && isset( $_POST['limit'] ) && !empty( $_POST['start'] ) && !empty( $_POST['limit'] ) ){
		$start = $_POST['start'];
		$limit = $_POST['limit'];
		$indexShow=indexShow($start,$limit);
		$data = array();
		$rowcount = $indexShow->RecordCount();
		$data['count'] = $rowcount;
		$html = '';
		if(!$indexShow){
			echo ALERTXT06;exit;
		}else{
			while($row = $indexShow->fetchRow()) {
				
				$html .= '<div class="grid-item">';
				$html .= '<div class="grid-content">';
				$html .= '<div class="grid-title">【'.strip_tags($row['depatm']).'_'.strip_tags($row['ex_name']).'】<br>'.strip_tags($row['ex_title']).'</div>';
				$html .= '<img src="'.UPLOADPICPATH.strip_tags($row['ex_pic']).'">';
				$html .= '<div class="grid-txt">'.strip_tags($row['ex_txt']).'</div>';
				//$html .= '<div class="grid-title">【'.$row['depatm'].'_'.$row['ex_name'].'】<br>'.$row['ex_title'].'</div>';
				//$html .= '<img src="'.UPLOADPICPATH.$row['ex_pic'].'">';
				//$html .= '<div class="grid-txt">'.$row['ex_txt'].'</div>';
				$html .= '</div>';
				$html .= '</div>';
				
				//$tpl->newBlock('index_row');
		
				//$tpl->assign(array('uname'=>$val['ex_name'],'department'=>$val['depatm'],'title'=>$val['ex_title'],'pic'=>$val['ex_pic'],'txt'=>$val['ex_txt']));
			}
			echo $html;exit;
		}
			
	}
?>

